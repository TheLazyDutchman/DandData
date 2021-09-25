from dataclasses import dataclass
from enum import Enum, auto

from .dice import Roll, rollFactory



class damageType(Enum):
    Acid: auto()
    Bludgeoning: auto()
    Cold: auto()
    Fire: auto()
    Force: auto()
    Lightning: auto()
    Necrotic: auto()
    Piercing: auto()
    Poison: auto()
    Psychic: auto()
    Radiant: auto()
    Slashing: auto()
    Thunder: auto()

class DamageTypeUndefined(ValueError):

    def __init__(self, damageType: str, message: str) -> None:
        super().__init__(message)
        self.damageType = damageType

@dataclass
class Damage:
    dmgType: damageType
    dice: Roll

class DamageFactory:

    def __call__(self, data: dict) -> Damage:
        dmgType = data["damage_type"]["name"]
        if not dmgType in damageType:
            raise DamageTypeUndefined(dmgType, f"damageType enum does not have a definition for {dmgType}")

        return Damage(damageType[dmgType], rollFactory(data["damage_dice"]))

damageFactory = DamageFactory()