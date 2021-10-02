from dataclasses import dataclass

from .action import Action, actionFactory



@dataclass
class Creature:
    name: str
    actions: list[Action]

class CreatureFactory:
    actionFactory = actionFactory

    def __call__(self, data: dict):
        actions = [self.actionFactory(action) for action in data['actions']]
        return Creature(data["name"], [action for action in actions if action != None])

creatureFactory = CreatureFactory()