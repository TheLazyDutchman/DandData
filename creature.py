from dataclasses import dataclass, field
from typing import Callable, Optional
import uuid

from .action import Action, actionFactory
from .damage import damageType

@dataclass
class Creature:
    name: str
    armorClass: int
    hitPoints: int
    health: int
    actions: list[Action]
    id: Optional[uuid.UUID] = field(default_factory=uuid.uuid4)
    rollList: dict[str, Callable] = field(default_factory=dict)

    def Damage(self, amount: int, dmgType: damageType) -> None:
        self.health -= amount
        
        if self.health < 0:
            self.health = 0

class CreatureFactory:
    actionFactory = actionFactory

    def __call__(self, data: dict):
        if "actions" in data:
            actions = [self.actionFactory(action) for action in data['actions']]
        else:
            actions = []
            
        return Creature(
            name = data["name"],
            armorClass = data["armor_class"],
            hitPoints = data["hit_points"],
            health = data["hit_points"],
            actions = [action for action in actions if action != None])

creatureFactory = CreatureFactory()



import requests, json
base_url = "https://www.dnd5eapi.co/api/"

def getInfo(request):
    sub_url = "/".join(request.split(" "))
    if sub_url.startswith('/api/'):
        sub_url = sub_url[5:]

    url = base_url + sub_url

    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
monsterList = getInfo("monsters")['results']
monsterList : list[str] = [x['index'] for x in monsterList]

for monster in monsterList:
    data = getInfo(f"monsters {monster}")
    print(data["name"])
    creature = creatureFactory(data)

print("had all creatures")