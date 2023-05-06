from random import randint

player_board_with_ships = None
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