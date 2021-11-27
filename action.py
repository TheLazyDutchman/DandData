from dataclasses import dataclass
from typing import Optional

from .dice import Roll, rollFactory

from .damage import Damage, damageFactory




@dataclass
class DifficultyClass:
    abilityType: str
    value: int
    successType: str


@dataclass
class Usage:
    pass
@dataclass
class RechargeOnRoll(Usage):
    dice: Roll
    minValue: int

@dataclass
class Action:
    name: str
    desc: str
    damage: list[Damage]
    dc: Optional[DifficultyClass]
    usage: Optional[Usage]
    

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
    rollFactory = rollFactory

    def __call__(self, data: dict) -> Action:
        data["damage"] = [self.damageFactory(dmg) for dmg in data["damage"]]

        if "usage" in data:
            usage = data["usage"]
            if not usage["type"] == "recharge on roll":
                print(data, "we don't handle a usage other than 'recharge on roll' yet")
                return

            data["usage"] = RechargeOnRoll(
                dice = rollFactory(usage["dice"]), 
                minValue = usage["min_value"])
        else:
            data["usage"] = None # the action dataclass expects to get a Usage at initialization, but most actions don't have one

        if "dc" in data:
            data["dc"] = DifficultyClass(
                abilityType = data["dc"]["dc_type"]["name"],
                value = data["dc"]["dc_value"],
                successType = data["dc"]["success_type"])
        else:
            data["dc"] = None # the action dataclass expects to get a dc at initialization, but most actions don't have one

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