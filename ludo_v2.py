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
P1_board_1 = Piece(color = 'blue', position = (120,120))
P1_board_2 = Piece(color = 'blue', position = (120,120))
P1_board_3 = Piece(color = 'blue', position = (120,120))
P1_board_4 = Piece(color = 'blue', position = (120,120))
P2_board_1 = Piece(color = 'red', position = (-120,-120))
P2_board_2 = Piece(color = 'red', position = (-120,-120))
P2_board_3 = Piece(color = 'red', position = (-120,-120))
P2_board_4 = Piece(color = 'red', position = (-120,-120))

class LudoGame:
    def __init__(self):
        # Initializing the game with player pieces, turn, and names
        self.player1_pieces = [57, 57, 54, 56]  # Player 1's piece positions
        self.player2_pieces = [57, 57, 57, 52]  # Player 2's piece positions
        self.player1_turn = True  # Player 1 starts the game
        self.player1_piece_names = ["P1", "P2", "P3", "P4"]  # Player 1's piece names
        self.player2_piece_names = ["P1", "P2", "P3", "P4"]  # Player 2's piece names
        self.player_1_board = [P1_board_1, P1_board_2, P1_board_3, P1_board_4] # Player 1's board pieces
        self.player_2_board = [P2_board_1, P2_board_2, P2_board_3, P2_board_4] # Player 2's board pieces

    def playsound(self, sound):
        global sound_on
        if sound_on:
            pygame.mixer.init()
            mix = pygame.mixer.Sound(sound)
            mix.play()
        
    def roll_dice(self):
        # Function to simulate rolling a six-sided dice
        self.playsound(dice_roll)
        if sound_on:
            time.sleep(0.7)
        return random.randint(1, 6)

    def move_piece(self, player_pieces, piece_index, roll, player_piece_names, player_board, positions_on_board):
        # Handles moving a player's piece based on the roll and current positions
        # Checks various conditions and returns messages indicating move status
        # This function manages piece movement logic


    #move_result = self.move_piece(current_player, piece_index, roll, current_piece_names, current_board_pieces)

        position = player_pieces[piece_index]

        # Check if the piece is at the starting position (0)
        if position == 0:
            if roll == 6:
                player_pieces[piece_index] = 1
                return "Piece moved to position 1"  # Valid move made
            else:
                return "You need a 6 to start a piece."

        # Check if the piece can move within the board or reach the final position (57)
        elif position == 1 or (position + roll) <= 57:
            if position + roll == 57:
                player_pieces[piece_index] = 57
                return "You just brought a piece home."
            elif position + roll > 57:
                return f"You need exactly {57 - position} to move that piece."
            else:
                # Increasing the position by the current roll
                player_pieces[piece_index] += roll
                
                if roll == 1:
    
                    self.playsound(player_move_once)
                if roll == 2:
                    
                    self.playsound(player_move_twice)
                if roll == 3:
                    
                    self.playsound(player_move_thrice)
                if roll == 4:
                    
                    self.playsound(player_move_4imes)
                if roll == 5:
                    
                    self.playsound(player_move_5imes)
                if roll == 6:
                    
                    self.playsound(player_move_6imes)
                
                player_board[piece_index].goto(positions_on_board[player_pieces[piece_index]])
                
                
                
                return "Piece moved"  # Valid move made

        # Handle invalid moves beyond position 56 and invalid moves for a roll of 6
        else:
            if position > 57:
                return "Invalid move. Cannot move piece beyond position 57."
            
            invalid_pieces = []
            for idx in range(len(player_pieces)):
                pos = player_pieces[idx]
                if pos != 0 and pos + roll > 57:
                    invalid_pieces.append(idx)

            if roll != 6:
                zero_count = 0
                for index in range(len(player_pieces)):
                    pos = player_pieces[index]
                    if index != piece_index:
                        if pos == 0:
                            zero_count += 1
                if len(invalid_pieces) == 1 and zero_count == 3:
                    playsound(Wrong_key_pressed)
                    return "Invalid move. No pieces can be moved with that roll"
                elif len(invalid_pieces) == 2 and zero_count == 2:
                    return "Invalid move. No pieces can be moved with that roll"
                elif len(invalid_pieces) == 3 and zero_count == 1:
                    return "Invalid move. No pieces can be moved with that roll"
                elif len(invalid_pieces) == 4 and roll <= 6:
                    return "Invalid move. No pieces can be moved with that roll"

            if roll == 6 and piece_index in invalid_pieces and len(invalid_pieces) < 4:
                return "Select another piece. This piece cannot be moved with a roll of 6."

            elif roll == 6 and len(invalid_pieces) == 4:
                self.player1_turn = not self.player1_turn
                return "You cannot move any pieces with that 6. Skipping to the next player"
            while True:
                piece_input = input("Invalid move. Which piece would you like to move (P1, P2, P3, or P4)? ").upper()
                
                
                if piece_input in player_piece_names:
                    piece_index = player_piece_names.index(piece_input)
                    if player_pieces[piece_index] != 0 or roll == 6:
                        break  # Exit the loop if a valid piece is selected
                    else:
                        
                        print("You need to select a piece that has already moved past position 0.")
                        self.playsound(Wrong_key_pressed)
                        continue  # Ask for a new piece selection
                else:
                    
                    print("Invalid input. Please enter P1, P2, P3, or P4.")
                    self.playsound(Wrong_key_pressed)

    
    def check_win(self, player_pieces):
        # Checks if a player has won by checking if all their pieces are at position 57
        return all(position == 57 for position in player_pieces)

    def print_board(self, player1_name, player2_name):
        # Prints the current state of the board showing player positions
        print(f"{player1_name}: {self.player1_pieces}")
        print(f"{player2_name}: {self.player2_pieces}")


    def play_game(self):
        # Controls the entire gameplay flow, including player turns, rolling dice, and win conditions
        # Allows players to roll the dice, move pieces, and checks for a win condition
        # Provides a restart or quit option at the end of the game

        print("Welcome to Ludo Game Version 2!")

        usernames = [input("Enter Player 1's username: "), input("Enter Player 2's username: ")]
        print(f"Welcome {usernames[0]} and {usernames[1]} to Ludo Game Version 2.")

        while True:
            start_or_rule = input("Press 'S' to start the game or 'H' for the rulebook: ").upper()

            if start_or_rule == 'H':
                print("""Ludo Game Version 2 Rulebook:
                Rules:
                1. Each player starts with four pieces.
                2. Players take turns rolling a six-sided die.
                3. A player needs a six to start a piece.
                4. Whenever a player rolls a six, they get to roll again.
                5. Only a piece that has already started can be moved by a non-Six roll.
                6. The winner is the first player who takes all their pieces home.
                7. Players must specify which piece to move when they roll.
                """)
            elif start_or_rule == 'S':
                break
            else:
                
                print("Invalid input. Please press 'S' to start the game or 'H' for the rulebook.")
                self.playsound(Wrong_key_pressed)
        while True:  # Main game loop
            roll = self.roll_dice()
            current_player = self.player1_pieces if self.player1_turn else self.player2_pieces
            current_piece_names = self.player1_piece_names if self.player1_turn else self.player2_piece_names
            positions_on_board = blue_positions if self.player1_turn else red_positions
            current_board_pieces = self.player_1_board if self.player1_turn else self.player_2_board
            current_username = usernames[0] if self.player1_turn else usernames[1]
            roll_prompt = 'R1' if self.player1_turn else 'R2'

            self.print_board(usernames[0], usernames[1])
            print(f"{current_username}, please roll by typing '{roll_prompt}':")
            input_player = input().upper()

            if input_player != roll_prompt:
                print(f"Invalid Input. Enter exactly '{roll_prompt}'")
                self.playsound(Wrong_key_pressed)
                continue

            print(f"{current_username} got a {roll}")

            if not any(current_player) and roll != 6:
                print("You need a 6 to start a piece.")
                self.player1_turn = not self.player1_turn
                continue

            while True:
                piece_input = input(f"Which piece would you like to move ({', '.join(current_piece_names)})? ").upper()
                if piece_input in current_piece_names:
                    piece_index = current_piece_names.index(piece_input)
                    if current_player[piece_index] != 0 or roll == 6:
                        break
                    else:
                        print("You need to select a piece that has already moved past position 0.")
                else:
                    print("Invalid input. Please enter P1, P2, P3, or P4.")
                    self.playsound(Wrong_key_pressed)


            # code to actually move the piece
            move_result = self.move_piece(current_player, piece_index, roll, current_piece_names, current_board_pieces, positions_on_board)
            
            
            while move_result == "Select another piece. This piece cannot be moved with a roll of 6.":
                print(move_result)
                piece_input = input(f"Which piece would you like to move ({', '.join(current_piece_names)})? ").upper()
                if piece_input in current_piece_names:
                    piece_index = current_piece_names.index(piece_input)
                    move_result = self.move_piece(current_player, piece_index, roll, current_piece_names, current_board_pieces, positions_on_board)
                else:
                    print("Invalid input. Please enter P1, P2, P3, or P4.")
            
            print(move_result)

            if roll != 6 and not any(current_player):
                print(f"{current_username} has no available moves.")
                self.player1_turn = not self.player1_turn
                continue

            if self.check_win(self.player1_pieces):
                print(f"{usernames[0]} wins!")
                break
            elif self.check_win(self.player2_pieces):
                print(f"{usernames[1]} wins!")
                break

            if roll != 6:
                self.player1_turn = not self.player1_turn

            if roll == 6:
                print("You got a 6! You get to roll again.")
                
            window.update()

        while True:
            restart_or_quit = input("Press RS to restart the game or Q to quit: ").upper()

            if restart_or_quit == 'Q':
                print("Thanks for playing! Goodbye.")
                break
            elif restart_or_quit == 'RS':
                self.__init__()  # Reset the game
                usernames = [input("Enter Player 1's username: "), input("Enter Player 2's username: ")]
                print(f"Welcome {usernames[0]} and {usernames[1]} to Team 1 Ludo Game Version 2.")
                break
            else:
                print("Invalid input. Please press RS to restart the game or Q to quit.")

# Create an instance of the LudoGame class and start playing the game
ludo_game = LudoGame()
ludo_game.play_game()
