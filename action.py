from dataclasses import dataclass

from .damage import Damage, damageFactory




@dataclass
class Action:
    name: str
    desc: str
    damage: list[Damage]
    

@dataclass
class Attack(Action):
    attack_bonus: int

class FactoryDataUnimplemented(Exception):

    def __init__(self, data: dict, dataType: str, message: str) -> None:
        super().__init__(message)
        self.data = data
        self.dataType = dataType

class ActionFactory:
    damageFactory = damageFactory

    def __call__(self, data: dict) -> Action:
        data["damage"] = [self.damageFactory(dmg) for dmg in data["damage"]]
        if "damage_dice" in data:
            print("api data has a separate damage_dice: ", data["damage_dice"])
            data["damage"].append(Damage(damage_type = "", damage_dice = data["damage_dice"]))
            data.pop("damage_dice")

        if "usage" in data:
            raise FactoryDataUnimplemented(data, "usage", "we don't handle usage of actions yet")

        if "dc" in data:
            raise FactoryDataUnimplemented(data, "dc", "we don't handle dc of actions yet")

        if "options" in data:
            raise FactoryDataUnimplemented(data, "options", "we don't handle multi attacks yet")

        if "attack_bonus" in data:
            return Attack(**data)

actionFactory = ActionFactory()