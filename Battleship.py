# BattleShip

# importing random package
import random


# -------------------- main function ---------------------- #

# this is the main function which holds the functionality of the game
def main():
    # setting grid_size
    grid_size = 6

    # setting the ship size
    ship_size = 3

    # creating a blank board
    board = []

    # intro print statement
    print("Let's play a riveting game of Battleship!")

    # inputting player's name
    player = input("Enter player's name: ")

    # good luck to player
    pregame_cheer = ("\nGood luck " + player + "!")
    print(pregame_cheer)

    # gives the player info on how many rounds they have
    if player == player:
        message = ("Let's start the game!\n"
                   "(You have 20 missles, make them count ;))\n")
        print(message)

    # list of 'missed ship' phrases to be chosen at random
    missed_phrases = ["\nOof, bad aim.\n",
                      "\nLol, you missed!\n",
                      "\nBro.. terrible guess..\n",
                      "\nJust, pathetic..\n",
                      "\nBad bad, not good.\n"]

    # list similarly for when successfully hitting the ship
    hit_phrases = ["\nOoh, right in the kisser!\n",
                   "\nNice hit!\n",
                   "\nYou're annihilating them!\n",
                   "\nFabulous hit to the enemy!\n",
                   "\nOo lala, keep it up!\n"]

    # setting the board
    board = make_board(grid_size)

    # prints the board
    print_board(board)
    print("\nDirect your first missile\n")

    # setting the ship randomly on board
    secret_board = place_ships_rand(board, ship_size)

    # starts the game
    message = guess_ship_pos(board,
                             ship_size,
                             secret_board,
                             hit_phrases,
                             missed_phrases,
                             grid_size)
    print(message)


# -------------------- functions that make up the game ---------------------- #


# creating a board of size x
def make_board(grid_size):
    board = []
    # creating the board
    for i in range(0, grid_size):
        board.append(["O"] * grid_size)
    return board


# printint out the dimensional board
def print_board(board):
    for row in board:
        print(row)


# pics a random position for the ship to be hidden
def place_ships_rand(board, ship_size):
    board_length = len(board) - 1
    max_ship_placement = board_length - ship_size
    random_row = random.randint(0, max_ship_placement)
    for col in range(ship_size):
        board[random_row][col] = '+'
    return board


# for loop within a function which starts the guesses in the game
def guess_ship_pos(board,
                   ship_size,
                   secret_board,
                   hit_phrases,
                   missed_phrases,
                   grid_size):
    hit_count = 0
    for missile in range(1, 21):
        guessing = True
        while guessing:
            # input for user to place guessed on ship position
            guess_col = int(input(
                "Guess x-coord (only enter values from 0 to 5): "))
            guess_row = int(input(
                "Guess y-coord (only enter values from 0 to 5): "))

            if guess_col > grid_size or guess_row > grid_size:
                print("Please enter values only from 0 - 5")
            else:
                guessing = False

        # if the guess hits the ship increase hit_count
        if secret_board[guess_row][guess_col] == "+":

            hit_count += 1

            # you have hit the ship and marked it with a *
            board[guess_row][guess_col] = "*"
            print_board(board)
            print(random.choice(hit_phrases))  # picks a random phrase

            # sunken ship statements (once all parts of ship are sunk)
            if hit_count == ship_size:
                print("\nYou have annihilated your opponent's ship!\n")
                print_board(board)
                break
        else:

            # if input is out of bounds or misses
            if guess_row < 0 or guess_row > grid_size \
                    or guess_col < 0 or guess_col > grid_size:
                print("\nThe war has made you dazed, you are out of bounds.\n")

            # for instances of repeated input
            elif (board[guess_row][guess_col] == "*") \
                    or board[guess_row][guess_col] == "X":
                print("\nYou've already stricken this area.\n")

            # marks the spot of past hits for trackability
            else:
                board[guess_row][guess_col] = "X"
                print_board(board)
                print(random.choice(missed_phrases))  # picks a random phrase

        # display the next missile
        print("Direct missile", missile + 1)

    # end game line
    print("\nThere has been enough blood shed in this battle.\nGame over!\n")


# -------------------- line that runs the game ---------------------- #

# runs the game
if __name__ == "__main__":
    main()
