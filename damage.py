from dataclasses import dataclass
from enum import Enum, auto

from .dice import Roll, rollFactory



class damageType(Enum):
    Acid = auto()
    Bludgeoning = auto()
    Cold = auto()
    Fire = auto()
    Force = auto()
    Lightning = auto()
    Necrotic = auto()
    Piercing = auto()
    Poison = auto()
    Psychic = auto()
    Radiant = auto()
    Slashing = auto()
    Thunder = auto()

class DamageTypeUndefined(KeyError):

    def __init__(self, damageType: str, message: str) -> None:
        super().__init__(message)
        self.damageType = damageType

@dataclass
class Damage:
    dmgType: damageType
    dice: Roll

class DamageFactory:

    def __call__(self, data: dict) -> Damage:
        dmgTypeStr = data["damage_type"]["name"]
        try:
            dmgType = damageType[dmgTypeStr]
        except KeyError as e:
            raise DamageTypeUndefined(dmgTypeStr, f"damagetype enum does not have a definition for {dmgTypeStr}")

        return Damage(dmgType, rollFactory(data["damage_dice"]))

damageFactory = DamageFactory()