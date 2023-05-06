from random import randint

class Board:
    """
    Main board class. Sets board size, the player's name
    and the board type (player board or computer board)
    It has two methods: First is to print the player board
    and second is to print the computer board
    """
    def __init__(self, size, name, type):
        self.size = size
        self.name = name
        self.yupe = type

    def print_the_player_board(self):
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

        final_board = "".join(board_list)

        return final_board


    def print_the_computer_board(self):
        rows = ""
        rows_and_columns = ""
        for x in range(0, 5):
            rows += "."
        for y in range(0, 5):
            rows_and_columns += rows + "\n"

        return rows_and_columns