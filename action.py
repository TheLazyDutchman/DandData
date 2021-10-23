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

class ActionFactory:
    damageFactory = damageFactory

    def __call__(self, data: dict) -> Action:
        data["damage"] = [self.damageFactory(dmg) for dmg in data["damage"]]

        if "usage" in data:
            print(data, "usage", "we don't handle usage of actions yet")
            return

        if "dc" in data:
            print(data, "dc", "we don't handle dc of actions yet")
            return

        if "options" in data:
            print(data, "options", "we don't handle multi attacks yet")
            return

        if "attack_options" in data:
            print(data, "attack_options", "we don't handle attack options yet")
            return

        if "attack_bonus" in data:
            return Attack(**data)

actionFactory = ActionFactory()