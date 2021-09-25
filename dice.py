from dataclasses import dataclass
from enum import Enum


class diceType(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

@dataclass
class Roll:
    amount: int
    dice_type: diceType
    bonus: int

class RollFactory:

    def __call__(self, data: str) -> Roll:
        dice, bonus = data.split('+')
        amount, dice = dice.split('d')

        return Roll(int(amount), diceType[dice], int(bonus))

rollFactory = RollFactory()