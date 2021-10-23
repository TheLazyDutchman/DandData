from dataclasses import dataclass, field
from typing import Optional
import uuid

from .action import Action, actionFactory

numCreatures = 0

@dataclass
class Creature:
    name: str
    actions: list[Action]
    id: Optional[uuid.UUID] = field(default_factory=uuid.uuid4)

class CreatureFactory:
    actionFactory = actionFactory

    def __call__(self, data: dict):
        actions = [self.actionFactory(action) for action in data['actions']]
        return Creature(data["name"], [action for action in actions if action != None])

creatureFactory = CreatureFactory()