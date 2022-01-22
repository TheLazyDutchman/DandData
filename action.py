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
class PerDay(Usage):
    times: int

@dataclass
class Action:
    name: str
    desc: str
    damage: list[Damage]
    dc: Optional[DifficultyClass]
    usage: Optional[Usage]
    

@dataclass
class AttackOptions(Action):
    amount: int
    options: list[Action]

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


@dataclass
class LairAttack:
    name: str
    dc: DifficultyClass

@dataclass
class LairActions(Action):
    attacks: list[LairAttack]

class ActionFactory:
    damageFactory = damageFactory
    rollFactory = rollFactory

    def __call__(self, data: dict) -> Action:
        if not "desc" in data:
            data["desc"] = ""

        if not "damage" in data:
            data["damage"] = []

        data["damage"] = [self.damageFactory(dmg) for dmg in data["damage"]]

        if "usage" in data:
            usage = data["usage"]
            if usage["type"] == "recharge on roll":
                data["usage"] = RechargeOnRoll(
                    dice = rollFactory(usage["dice"]), 
                    minValue = usage["min_value"])

            elif usage["type"] == "per day":
                data["usage"] = PerDay(usage["times"])

            else:
                print(data, "we don't handle this type of usage yet\n\n")
                return
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
            data["amount"] = data["attack_options"]["choose"]
            data["options"] = [self(x) for x in data["attack_options"]["from"]]
            data.pop("attack_options")

            return AttackOptions(**data)

        if "attacks" in data:
            data["attacks"] = [
                LairAttack(x["name"], 
                DifficultyClass(
                    abilityType = x["dc"]["dc_type"]["name"],
                    value = x["dc"]["dc_value"],
                    successType = x["dc"]["success_type"])
                ) for x in data["attacks"]]

            return LairActions(**data)

        if "attack_bonus" in data:
            return Attack(**data)

        return Action(**data)

actionFactory = ActionFactory()