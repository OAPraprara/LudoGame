The sound functionality is enabled by pygame. If you do not have pygame installed on your computer, write this on your command prompt:
## ! pip install pygame

Ludo is a popular game in Ghana. 


# Version 1:

A Ludo game with only two players and with each player having just one piece instead of the usual four pieces. Each player takes turn rolling the dice. They need a Six to start (i.e., get out of home). Whenever a user plays a Six, they get to roll again. There is no kicking of an opponent's piece involved, and one’s piece can only move forward in this version of the game. This game happens on a standard Ludo board. The first player is Blue, and the second player is Red.

Player 1 presses 'L' to roll
Player 2 presses 'R' to roll

The flow of the game is something like this:

Player 1 will begin. Please roll by typing L:
L
Player 1 got a 5.
Player 2, please roll by typing R:
R
Player 2 got a 6. Please roll again by typing R:
R
Player 2 got a 5.
Player 1, please roll by typing L:

The game continueS this way until one player wins. A player wins the game in the standard way by taking their piece all the way round the board and back to their home. In the final stretch, if a player plays more than what is needed to go home, they cannot move. Say you need to play 2 to go home, but you play 5, then you stay put, and your opponent plays.

Demo: https://youtu.be/30Eewl_6aTU

# Version 2:

Version 2 of the game is the same in all respects as Version 1, except that each player now has the standard four pieces. The winner is the player who first takes all their pieces home. Since there are four pieces, each player must specify which piece to move when they roll. A sample interaction looks like this:

Player 1 will begin. Please roll by typing R1:
R1
Player 1 got a 5.
Player 2, please roll by typing R2:
R2
Player 2 got a 6. Which piece would you like to move (P1, P2, P3 or P4)?
P1
Player2, please roll again by typing R2:
R2
Player 2 got a 5. Which piece would you like to move (P1, P2, P3 or P4)?
P1
Player 1, please roll by typing R1:
R1


Only a piece that has already started can be moved by a non-Six roll. For instance, if player 2 had said they wanted to move P2 when they played 5, the program would say that this is not an allowed move. This is because P1 was the only piece out at this point.

# Contributors
Ismail Adam
Jesse Donkor
Amanda Maphosa
Emmanuel Boateng