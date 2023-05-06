from random import randint

input_name = None
input_number_of_ships = None
player_board_with_ships = None

computer_ships_positions_list = []

class Board:
    """
    Main board class. Sets board size, the player's name
    and the board type (player board or computer board)
    It has two methods: First is to create the player board
    and second is to create the computer board
    """
    def __init__(self, size, name, type):
        self.size = size
        self.name = name
        self.yupe = type

    def print_the_player_board(self):
        """
        Creates the player board
        """
        rows = ""
        rows_and_columns = ""

        for x in range(0, 5):
            rows += "."

        for y in range(0, 5):
            rows_and_columns += rows

        board_list = [dot for dot in rows_and_columns]

        while True:
            board_list[randint(0, 24)] = "@"

            if board_list.count("@") == input_number_of_ships:
                break

        for i in range(4, 20, 5):
            board_list[i] += "\n"

        for i in range(0, 25):
            board_list[i] =  "  " + board_list[i]

        player_final_board = "".join(board_list)

        return player_final_board


    def print_the_computer_board(self):
        """
        Creates the computer board
        """
        rows = ""
        rows_and_columns = ""
        for x in range(0, 5):
            rows += "."
        for y in range(0, 5):
            rows_and_columns += rows + "\n"

        return rows_and_columns

player_board = Board(5, input_name, "player")
computer_board = Board(5, "Computer", "computer")

def show_the_boards():
    """
    Shows both the player's board and the computer's board
    """
    global player_board_with_ships
    player_board_with_ships = player_board.print_the_player_board()

    print(f"\n{input_name}'s Board:")
    print(player_board_with_ships)

    fixed_computer_board = ["  " + dot for dot in computer_board.print_the_computer_board()]
    fixed_computer_board = "".join(fixed_computer_board)

    print("\nComputer's Board:")
    print(fixed_computer_board)


def player_coordinates_guess():
    """
    Makes the user to guess a row between 1-5 and raises an error otherwise
    Makes the user to guess a column between 1-5 and raises an error otherwise
    Prints the chosen row and column
    Returns a list of the chosen row and column [row, column]
    """
    while True:
        try:
            guess_a_row = int(input("Guess a row:\n"))

            if guess_a_row < 1 or guess_a_row > 5:
                raise Exception(
                    "Invalid Data: You must enter an integer between 1 and 5"
                )
                
        except ValueError:
            print("Value Error: You must enter an integer, please try again.\n")

        except Exception as e:
            print(f"{e}, please try again.\n")

        except:
            print("Error: You must enter an integer between 1 and 5, please try again.\n")

        else:
            break

    while True:
        try:
            guess_a_column = int(input("Guess a column:\n"))

            if guess_a_column < 1 or guess_a_column > 5:
                raise Exception(
                    "Invalid Data: You must enter an integer between 1 and 5"
                )
                
        except ValueError:
            print("Value Error: You must enter an integer, please try again.\n")

        except Exception as e:
            print(f"{e}, please try again.\n")

        except:
            print("Error: You must enter an integer between 1 and 5, please try again.\n")

        else:
            break

    print(f"Player guessed: ({guess_a_row}, {guess_a_column})")

    return [guess_a_row, guess_a_column]


def computer_ships():
    """
    Creates a specific amount of computer ships
    and returns a list of the computer ships positions (indexes)
    """
    while True:
        random_num = randint(1, 25)

        if computer_ships_positions_list.count(random_num) == 0:
            computer_ships_positions_list.append(random_num)

        if len(computer_ships_positions_list) == input_number_of_ships:
            break

    return computer_ships_positions_list


def game_details():
    """
    Gives information about the game when the user starts playing
    Asks the user to enter their name
    Asks the user to enter the number of ships between 5-10, raises an error otherwise
    Calls show_the_boards() function
    Calls computer_ships() function
    """
    print("-" * 40)
    print("Welcome to BATTLESHIPS game\n")
    print("The top left corner is Column: 1, Row: 1\n")
    print("-" * 40)
    global input_name
    input_name = input("Please enter your name:\n")

    while True:
        try:
            global input_number_of_ships
            input_number_of_ships = int(input(f"Please choose the number of ships, between 5 and 10:\n"))

            if input_number_of_ships > 10 or input_number_of_ships < 5:
                raise Exception(
                    "Invalid Data: You must enter an integer between 5 and 10"
                )
            print(f"The board has {input_number_of_ships} ships\n")
            print("-" * 40)

        except ValueError:
            print("Value Error: You must enter an integer, please try again.\n")

        except Exception as e:
            print(f"{e}, please try again.\n")
            print("-" * 40)

        except:
            print("Error: You must enter an integer between 5 and 10, please try again.\n")
            
        else:
            break

    show_the_boards()
    computer_ships()