# DandData
a library to store information from D&D in python dataclasses
## Supported API's
 - [x] [dnd5eapi]("http://www.dnd5eapi.co")
 - [ ] the [dndbeyond]("https://www.dndbeyond.com") api (they had this as a planned feature for years, but I doubt they will make it any time soon)
## Creatures
```python
from DandData.creature import Creature
```
currently handled:
- [x] name
- [ ] desc - (not all monsters have a description)
- [ ] size
- [ ] type
- [ ] subtype
- [ ] alignment
- [ ] AC
- [ ] HP
- [ ] hit dice
- [ ] speed
- [ ] ability scores
    - [ ] strength
    - [ ] dexterity
    - [ ] constitution
    - [ ] intelligence
    - [ ] wisdom
    - [ ] charisma
- [ ] proficiencies
- [ ] proficiencies
- [ ] vulnerabilites
- [ ] resistances
- [ ] immunities
- [ ] senses
- [ ] languages
- [ ] CR
- [ ] XP
- [ ] special abilities
- [x] [actions](#Actions)
- [ ] legendary actions - (not all creatures have legendary actions)
## Actions
```python
from DandData.action import Action
```
currently handled:
 - [x] name
 - [x] desc
 - [x] damage
 - [x] attack bonus - (not all actions have this)
 - [ ] usage - (not all actions have this)
 - [ ] dc - (not all actions have this)
 - [ ] options - (only for multi attacks)
 - [ ] attack options - (not all actions have this)