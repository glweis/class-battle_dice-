import random
from character import Character

class Game :
    """Manages the Dice Battle Game Logic."""

    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self.player1 = player1
        self.player2 = player2
    
    def attack(self, attacker: Character, defender: Character):
        """Performs an attack where the attacker rolls a die to determine damage dealt."""
        pass 
        #TODO: Implement die roll (1-6) and apply scaled attack power to defender
    
    def startbattle(self):
        """Starts a turn-based battle between two players."""
        pass
        #TODO: Implement the battle loop where players take turns attacking 


from charactertype import CharacterType

mycharactertype = CharacterType.WARRIOR
print(mycharactertype)
print(mycharactertype.name)
print(mycharactertype.value)