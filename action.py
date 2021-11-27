from dataclasses import dataclass
from typing import Optional

from .damage import Damage, damageFactory




@dataclass
class DifficultyClass:
    abilityType: str
    value: int
    successType: str


@dataclass
class Action:
    name: str
    desc: str
    damage: list[Damage]
    dc: Optional[DifficultyClass]
    

@dataclass
class Attack(Action):
    attack_bonus: int

@dataclass
class MultiAttackOption:
    name: str
    count: int
    actionType: str

@dataclass
class MultiAttack(Action):
    options: list[MultiAttackOption]

class ActionFactory:
    damageFactory = damageFactory

    def __call__(self, data: dict) -> Action:
        data["damage"] = [self.damageFactory(dmg) for dmg in data["damage"]]

        if "usage" in data:
            print(data, "usage", "we don't handle usage of actions yet")
            return

        if "dc" in data:
            data["dc"] = DifficultyClass(
                abilityType = data["dc"]["dc_type"]["name"],
                value = data["dc"]["dc_value"],
                successType = data["dc"]["success_type"])
        else:
            data["dc"] = None # the attack dataclass expects to get a dc at initialization, but most actions don't have one

        if "options" in data:
            if data["options"]["choose"] != 1:
                print("\n", data, "\n we don't handle multi attacks with multiple options to choose from")
                return
            
            options = data["options"]["from"][0]
            data["options"] = [MultiAttackOption(x["name"], x["count"], x["type"]) for x in options]

            return MultiAttack(**data)

        if "attack_options" in data:
            print(data, "attack_options", "we don't handle attack options yet")
            return

        if "attack_bonus" in data:
            return Attack(**data)

        return Action(**data)

actionFactory = ActionFactory()