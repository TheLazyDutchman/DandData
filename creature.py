from dataclasses import dataclass, field
from typing import Callable, Optional
import uuid

from .action import Action, actionFactory

@dataclass
class Creature:
    name: str
    hit_points: int
    health: int
    actions: list[Action]
    id: Optional[uuid.UUID] = field(default_factory=uuid.uuid4)
    rollList: dict[str, Callable] = field(default_factory=dict)

    def Damage(self, amount: int) -> None:
        self.health -= amount
        
        if self.health < 0:
            self.health = 0

class CreatureFactory:
    actionFactory = actionFactory

    def __call__(self, data: dict):
        actions = [self.actionFactory(action) for action in data['actions']]
        return Creature(
            name = data["name"],
            hit_points = data["hit_points"],
            health = data["hit_points"],
            actions = [action for action in actions if action != None])

creatureFactory = CreatureFactory()