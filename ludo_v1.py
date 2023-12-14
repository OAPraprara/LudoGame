'''
Amanda Maphosa
Jesse Donkor
Emmanuel Boateng
Praprara Owodeha-Ashaka
Ismail Adam
'''




import random
import time
from corredtLudoBoard import *
# need to pip install pygame.
# go to command prompt and just type this: pip install pygame

#from playsound import playsound
import pygame

dice_roll = r"dice_roll.wav"
Wrong_key_pressed = r"Wrong_key_pressed.wav"
player_move_once = r"1 knock.wav"
player_move_twice = r"2 knocks.wav"
player_move_thrice = r"3 knocks.wav"
player_move_4imes = r"4 knocks.wav"
player_move_5imes = r"5 knocks.wav"
player_move_6imes = r"6 knocks.wav"
player1_wins = r"Player 1 wins.wav"
player2_wins = r"Player 2 wins.wav"

sound_on = True

player_1_piece = Piece(color = 'blue', position = (120,120))
player_2_piece = Piece(color = 'red', position = (-120,-120))

def playsound(sound):
    global sound_on
    if sound_on:
        pygame.mixer.init()
        mix = pygame.mixer.Sound(sound)
        mix.play()
        
        
def roll_dice():
    # Function to simulate rolling a six-sided dice
    
        
    playsound(dice_roll)
    #small delay before piece starts moving
    if sound_on:
        time.sleep(0.7)
    return random.randint(1, 6)

def move_piece(player, position, roll):
    while  True:
        if position + roll > 57:
            roll_needed = 57 - position
            print(f"You need exactly {roll_needed} to complete the game")
            
            return position
        elif roll == 6 and position >=52:
            continue   
        else:
            if roll == 1:
        
                playsound(player_move_once)
            if roll == 2:
                
                playsound(player_move_twice)
            if roll == 3:
                
                playsound(player_move_thrice)
            if roll == 4:
                
                playsound(player_move_4imes)
            if roll == 5:
                
                playsound(player_move_5imes)
            if roll == 6:
                
                playsound(player_move_6imes)
                
            return position + roll


def check_win(player, position):
    # Function to check if the player has reached the winning position (57)
    return position == 57

def display_table(player1_name, player1_position, player2_name, player2_position):
    # Function to display the current positions of both players
    print("+-------------------+-------------------+")
    print(f"| {player1_name:<17} | {player2_name:<17} |")
    print("+-------------------+-------------------+")
    print(f"| {player1_position:<17} | {player2_position:<17} |")
    print("+-------------------+-------------------+")

def display_rulebook():
    # Function to display the rules of the Ludo game
    rules = """RULEBOOK:
1. This is a Ludo game with only two players and with each player having just one piece instead of the usual four pieces.
2. Each player takes turn rolling the dice. They need a Six to start (i.e., get out of home). Whenever a user plays a Six, they get to roll again.
3. There is no kicking of an opponent's piece involved, and one’s piece can only move forward in this version of the game.
4. The game continues until one player wins. A player wins by taking their piece all the way round the board and back to their home on position 57.
5. In the final stretch, if a player plays more than what is needed to go home, they cannot move.
   For example, if you need to play 2 to go home, but you play 5, then you stay put, and your opponent plays."""
   
    print("RULEBOOK:\n")
    print(rules)

def start_new_game():
    global sound_on
    # Function to start a new game of Ludo
    print("Welcome to Team 1 Ludo Game Version 1.")
    
    # Loop to display rulebook or start the game based on user input
    while True:
        
        print("Press 'S' to start the game or 'H' for the rule book.")
        user_choice = input().upper()

        if user_choice == 'S':
            break
        elif user_choice == 'H':
            display_rulebook()
        else:
            print("Invalid choice. Please press 'S' to start or 'H' for the rule book.")
            if sound_on:
                playsound(Wrong_key_pressed)
                    
    # Loop to input player names and start the game
    while True:
        #window.update()
        print("Enter the username for Player 1:")
        player1_name = input()
        print("Enter the username for Player 2:")
        player2_name = input()

        '''
        print(f"Press 'S' to begin rolling, {player1_name} and {player2_name}!")
        start_game = input().upper()

        if start_game != 'S':
            print ('Invalid choice')
            break
        '''
        
        player1_position = 0
        player2_position = 0
        player1_turn = True  # Flag to keep track of player turns

        # Loop to play the game until a player wins or decides to quit
        while True:
            #window.update()
            display_table(player1_name, player1_position, player2_name, player2_position)
            
            if player1_turn:
                print(f"{player1_name}, press 'R' to roll:")
                input_player = input()
                if input_player.upper() == "R":
                    roll = roll_dice()
                    print(f"{player1_name} got a {roll}")
                    
                    # Logic for moving the player's piece based on the dice roll
                    if roll == 6 and player1_position == 0:
                        player1_position = 1  # Move to position 1 if initial roll is 6
                    elif roll != 6 and player1_position == 0:
                        print(f"{player1_name}, you need a 6 to start")
                    elif player1_position > 0:
                        new_position = move_piece(1, player1_position, roll)

                        # make the piece move on board
                        player_1_piece.goto(blue_positions[new_position])
                        
                        # Handling situations where the move exceeds the winning position
                        if player1_position + roll > 57:
                            print(f"{player1_name}, your position exceeds 57. Skipping your turn.")
                            player1_turn = False  # Skip turn if position exceeds 57
                        else:
                            player1_position = new_position
                            
                    elif player1_position >= 52 and roll == 6:
                        player1_turn = False
                    
                    # Check if player 1 has won the game
                    if check_win(1, player1_position):
                        display_table(player1_name, player1_position, player2_name, player2_position)
                        print(f"{player1_name} wins!")

                        # play player 1 wins sound
                        playsound(player1_wins)
                        
                        while True:
                            choice = input(f"Do you want to restart (RS) or quit (Q)? ").upper()
                            if choice == 'RS':
                                break  # Break inner loop to restart
                            elif choice == 'Q':
                                return  # Quit the game
                            else:
                                print("Invalid choice. Please enter 'RS' to restart or 'Q' to quit.")
                                continue  # Ask again for a valid choice
                        break  # Break outer loop to restart
                    elif roll != 6:
                        player1_turn = False
                elif input_player.upper() == "Q":
                    return

                # options to toggle sound on/off
                elif input_player.upper() == "SILENT":
                    #global sound_on
                    sound_on = False
                
                elif input_player.upper() == "SOUND":
                
                    sound_on = True
                else:
                    print(f"Invalid Input, {player1_name}. Press 'R' to roll or 'Q' to quit")

                    #play wrong key pressed sound
                    
                    playsound(Wrong_key_pressed)
                        
            # player 2 playing sequence
            else:
                print(f"{player2_name}, press 'L' to roll:")
                input_player = input()
                if input_player.upper() == "L":
                    roll = roll_dice()
                    print(f"{player2_name} got a {roll}")
                    
                    # Logic for player 2's turn to move their piece
                    if roll == 6 and player2_position == 0:
                        player2_position = 1  # Move to position 1 if initial roll is 6
                    elif roll != 6 and player2_position == 0:
                        print(f"{player2_name}, you need a 6 to start")
                    elif player2_position > 0:
                        new_position = move_piece(2, player2_position, roll)

                        # make the piece move on board
                        player_2_piece.goto(red_positions[new_position])
                        
                        # Handling situations where the move exceeds the winning position
                        if player1_position + roll > 57:
                            print(f"{player2_name}, your position exceeds 57. Skipping your turn.")
                            player1_turn = True  # Skip turn if position exceeds 57
                        else:
                            player2_position = new_position
                    elif player2_position >= 52 and roll == 6:
                        player1_turn = True
                    
                    # Check if player 2 has won the game
                    if check_win(2, player2_position):
                        display_table(player1_name, player1_position, player2_name, player2_position)
                        print(f"{player2_name} wins!")

                        # play player 2 wins sound
                        
                        playsound(player2_wins)
                        while True:
                            choice = input(f"Do you want to restart (RS) or quit (Q)? ").upper()
                            if choice == 'RS':
                                break  # Break inner loop to restart
                            elif choice == 'Q':
                                return  # Quit the game
                            else:
                                print("Invalid choice. Please enter 'RS' to restart or 'Q' to quit.")
                                #play wrong key pressed sound
                                
                                playsound(Wrong_key_pressed)
                                continue  # Ask again for a valid choice
                        break  # Break outer loop to restart
                    elif roll != 6:
                        player1_turn = True
                elif input_player.upper() == "Q":
                    return

                # sound toggle
                elif input_player.upper() == "SILENT":
                    sound_on = False
                
                elif input_player.upper() == "SOUND":
                    sound_on = True
                else:
                    print(f"Invalid Input, {player2_name}. Press 'L' to roll or 'Q' to quit")
                    #play wrong key pressed sound
                    
                    playsound(Wrong_key_pressed)
            window.update()
start_new_game()
