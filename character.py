from dataclasses import dataclass
from charactertype import CharacterType

@dataclass
class Character:
    name: str
    charactertype: CharacterType
    health: int
    attackpower: int
