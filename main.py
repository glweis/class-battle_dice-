from game import Game
from character import Character
from character import CharacterType

#Create characters
alice = Character(name = "Alice", charactertype = CharacterType.WARRIOR, health = 100, attackpower = 2)
bob = Character(name = "Bob", characterType = CharacterType.MAGE, health = 70, attackpower = 1)

#Start Game
game = Game(alice, bob)
game.startbattle()
