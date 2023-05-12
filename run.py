from random import randint

while True:

    input_name = None
    input_number_of_ships = None

    player_board_with_ships = None
    player_guess = None
    player_updated_board_list = None
    computer_updated_board_list = None

    player_score = 0
    computer_score = 0

    computer_ships_positions_list = []
    player_all_guesses_list = []
    computer_all_guesses_list = []

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
            self.type = type

        def print_the_player_board(self, size):
            """
            Creates the player board based on the given size
            """
            row = ""
            rows_and_columns = ""

            for x in range(0, self.size):
                row += "."

            for y in range(0, self.size):
                rows_and_columns += row

            board_list = [dot for dot in rows_and_columns]

            while True:
                board_list[randint(0, self.size ** 2 - 1)] = "@"

                """
                This if statement is to break the loop when
                the amount of "@" (ships) are equal to the
                amount of the number of ships given by the user
                """
                if board_list.count("@") == input_number_of_ships:
                    break
            
            """
            This for loop is to transform a list to a board
            by adding a new line after the required amount
            of columns in each row
            Except for the last row, no need to add a new line after it
            """
            for i in range(
                self.size - 1, self.size ** 2 - self.size, self.size
            ):
                board_list[i] += "\n"

            for i in range(0, self.size ** 2):
                board_list[i] = "  " + board_list[i]

            player_final_board = "".join(board_list)

            return player_final_board

        def print_the_computer_board(self, size):
            """
            Creates the computer board based on the given size
            """
            row = ""
            rows_and_columns = ""

            for x in range(0, self.size):
                row += "."

            for y in range(0, self.size):
                rows_and_columns += row + "\n"

            return rows_and_columns

    player_board = Board(5, input_name, "player")
    computer_board = Board(5, "Computer", "computer")

    def game_details():
        """
        Gives information about the game when the user starts playing
        Asks the user to enter their name
        Raises an error if name was empty
        Asks the user to enter the number of ships between 5 and 10,
        Raises an error otherwise
        """
        print("-" * 40)
        print("Welcome to BATTLESHIPS game\n")
        print("The top left corner is Row: 1, Column: 1\n")
        print("-" * 40)

        """
        This while loop is to make sure that
        the name of the player is not empty
        """
        while True:

            try:
                global input_name
                input_name = input("Please enter your name:\n")

                if len(input_name.strip()) == 0:
                    raise Exception(
                        "Invalid Data: Name field must not remain empty"
                    )

            except Exception as e:
                print(f"{e}, please enter your name\n")

            else:
                break
        

        """
        This while loop is to makre sure that
        the user enters a number between 5 and 10
        """
        while True:

            try:
                global input_number_of_ships

                input_number_of_ships = int(input(
                    ("Please choose the number of ships, "
                     "between 5 and 10:\n")
                ))

                if input_number_of_ships > 10 or input_number_of_ships < 5:
                    raise Exception(
                        ("Invalid Data: You must enter "
                         "an integer between 5 and 10")
                    )

                print(f"The board has {input_number_of_ships} ships\n")
                print("-" * 40)

            except ValueError:
                print(
                    ("Value Error: You must enter "
                     "an integer, please try again.\n")
                )

            except Exception as e:
                print(f"{e}, please try again.\n")
                print("-" * 40)

            else:
                break

    def show_the_boards():
        """
        Shows both the player's board and the computer's board
        """
        global player_board_with_ships
        player_board_with_ships = (
            player_board.print_the_player_board(player_board.size)
        )

        print(f"\n{input_name}'s Board:")
        print(player_board_with_ships)

        fixed_computer_board = (
            ["  " + dot for dot in
             computer_board.print_the_computer_board(computer_board.size)]
        )
        fixed_computer_board = "".join(fixed_computer_board)

        print(f"\n{computer_board.name}'s Board:")
        print(fixed_computer_board)

    def computer_ships():
        """
        Creates a specific amount of computer ships
        based on the input_number_of_ships given by the user
        """
        while True:
            random_num = randint(1, computer_board.size ** 2)

            """
            This if statement is to avoid having
            multiple ships at the same position
            """
            if computer_ships_positions_list.count(random_num) == 0:
                computer_ships_positions_list.append(random_num)

            """
            This if statement is to break the loop when
            the number of computer ships are equal to
            the given number of ships by the user
            """
            if len(computer_ships_positions_list) == input_number_of_ships:
                break

    def player_coordinates_guess():
        """
        Makes the user to guess a row between
        1 and the size of the computer_board (5),
        raises an error otherwise
        Makes the user to guess a column between
        1 and the size of the computer_board (5),
        raises an error otherwise
        Prints the chosen row and column
        Returns a list of the chosen row and column [row, column]
        """
        while True:

            try:
                guess_a_row = int(input("Guess a row:\n"))

                if guess_a_row < 1 or guess_a_row > computer_board.size:
                    raise Exception(
                        ("Invalid Data: You must enter "
                         f"an integer between 1 and {computer_board.size}")
                    )

            except ValueError:
                print(
                    ("Value Error: You must enter "
                     "an integer, please try again.\n")
                )

            except Exception as e:
                print(f"{e}, please try again.\n")

            else:
                break

        while True:

            try:
                guess_a_column = int(input("Guess a column:\n"))

                if guess_a_column < 1 or guess_a_column > computer_board.size:
                    raise Exception(
                        ("Invalid Data: You must enter "
                         "an integer between 1 and 5")
                    )

            except ValueError:
                print(
                    ("Value Error: You must enter "
                     "an integer, please try again.\n")
                )

            except Exception as e:
                print(f"{e}, please try again.\n")

            else:
                break

        print(f"Player guessed: ({guess_a_row}, {guess_a_column})")

        return [guess_a_row, guess_a_column]

    def check_player_guess():
        """
        Creates a function that checks whether the player
        has already guessed the same coordinates twice
        Checks whether player guess position is uqual
        to one of the computer ships position
        If it is equal then:
        - The Full stop sign "." will become "*"
        - Updates the board and prints the updated board
        - player_score variable gets increased by 1
        If it is not equal then:
        - The Full stop sign "." will become "X"
        - Updates the board and prints the updated board
        """

        def indicate_player_duplicate_coordinates():
            """
            Calls player_coordinates_guess() function
            Creates a loop that checks whether the player
            has already guessed the same coordinates twice
            If so, then the player will have to guess again
            """
            global player_guess
            player_guess = player_coordinates_guess()

            for coordinates in player_all_guesses_list:

                if player_guess == coordinates:
                    print("You can't guess the same coordinates twice!")
                    indicate_player_duplicate_coordinates()

        indicate_player_duplicate_coordinates()

        player_all_guesses_list.append(player_guess)
        computer_board_list = (
            [dot for dot in
             computer_board.print_the_computer_board(computer_board.size)]
        )

        for j in range(computer_board.size):
            computer_board_list.remove('\n')

        global computer_updated_board_list

        if computer_updated_board_list is not None:
            computer_board_list = computer_updated_board_list

        hit = False

        for position in computer_ships_positions_list:

            """
            (y * z - (z - x)) - 1
            This equation is to transform coordinates
            to a specific position (index) in a list
            - y represents the row
            - x represents the column
            - z represents the amount of columns the board has
            - The number -1 at the end is to make the postion as zero-indexing
            """
            if position == (
                player_guess[0] * computer_board.size -
                (computer_board.size - player_guess[1])
            ):
                print("Player got a hit!")
                computer_board_list[(player_guess[0] *
                                    computer_board.size -
                                    (computer_board.size - player_guess[1])) -
                                    1] = "*"
                computer_updated_board_list = (
                    [ch for ch in computer_board_list]
                )

                for x in range(len(computer_board_list)):
                    computer_board_list[x] = "  " + computer_board_list[x]

                for y in range(
                    computer_board.size - 1,
                    computer_board.size ** 2,
                    computer_board.size
                ):
                    computer_board_list[y] += '\n'

                computer_board_list = "".join(computer_board_list)
                print("-" * 40)
                print(computer_board_list)
                print("-" * 40)

                global player_score
                player_score += 1

                hit = True
                break

        if hit is False:
            print("Player missed this time.")
            computer_board_list[(player_guess[0] *
                                computer_board.size -
                                (computer_board.size - player_guess[1])) -
                                1] = "X"
            computer_updated_board_list = [ch for ch in computer_board_list]

            for x in range(len(computer_board_list)):
                computer_board_list[x] = "  " + computer_board_list[x]

            for y in range(
                computer_board.size - 1,
                computer_board.size ** 2,
                computer_board.size
            ):
                computer_board_list[y] += '\n'

            computer_board_list = "".join(computer_board_list)

            print("-" * 40)
            print(computer_board_list)
            print("-" * 40)

    def check_computer_guess():
        """
        Creates a function that checks whether the computer
        has already guessed the same coordinates twice
        Checks whether computer guess position is uqual
        to one of the player ships position
        If it is equal then:
        - The At sign "@" will become "*"
        - Updates the board and prints the updated board
        - computer_score variable gets increased by 1
        If it is not equal then:
        - The Full stop sign "." will become "X"
        - Updates the board and prints the updated board
        """

        def indicate_computer_duplicate_coordinates():
            """
            Checks whether the computer has already
            guessed the same coordinates twice
            If so, then the computer will have to guess again
            """
            global computer_guess
            computer_guess = [
                randint(1, player_board.size),
                randint(1, player_board.size),
            ]

            for coordinates in computer_all_guesses_list:

                if coordinates == computer_guess:
                    computer_guess = [
                        randint(1, player_board.size),
                        randint(1, player_board.size),
                    ]
                    indicate_computer_duplicate_coordinates()

        indicate_computer_duplicate_coordinates()

        computer_all_guesses_list.append(computer_guess)

        print(f"{computer_board.name} guessed ({computer_guess[0]}, {computer_guess[1]})")
        player_board_list = player_board_with_ships.split()

        global player_updated_board_list

        if player_updated_board_list is not None:
            player_board_list = player_updated_board_list

        if player_board_list[(computer_guess[0] *
           player_board.size -
           (player_board.size - computer_guess[1])) -
           1] == "@":
            player_board_list[(computer_guess[0] *
                              player_board.size -
                              (player_board.size - computer_guess[1])) -
                              1] = "*"
            player_updated_board_list = [ch for ch in player_board_list]
            print(f"{computer_board.name} got a hit!")

            for y in range(
                player_board.size - 1,
                player_board.size ** 2,
                player_board.size
            ):
                player_board_list[y] += '\n'

            for x in range(len(player_board_list)):
                player_board_list[x] = "  " + player_board_list[x]

            player_board_list = "".join(player_board_list)
            print("-" * 40)
            print(player_board_list)
            print("-" * 40)

            global computer_score
            computer_score += 1

        else:
            player_board_list[(computer_guess[0] *
                              player_board.size -
                              (player_board.size - computer_guess[1])) -
                              1] = "X"
            player_updated_board_list = [ch for ch in player_board_list]
            print(f"{computer_board.name} missed this time.")

            for y in range(
                player_board.size - 1,
                player_board.size ** 2,
                player_board.size
            ):
                player_board_list[y] += '\n'

            for x in range(len(player_board_list)):
                player_board_list[x] = "  " + player_board_list[x]

            player_board_list = "".join(player_board_list)
            print("-" * 40)
            print(player_board_list)
            print("-" * 40)

    def score_results():
        """
        Prints player's score
        Prints computer's score
        """
        print("After this round, the scores are:")
        print(f"{input_name}: {player_score}")
        print(f"{computer_board.name}: {computer_score}")

    def continue_or_quit():
        """
        Asks the user if they want to continue playing the game or quit
        """
        global cont_or_qu
        cont_or_qu = input("Enter any key to continue or n to quit:\n")

    def start_game():
        """
        Calls game_details() function
        Calls show_the_boards() function
        Calls computer_ships() function
        Creates a loop and inside it calls the required
        functions to play the game, which are:
        - check_player_guess()
        - check_computer_guess()
        - score_results()
        """
        game_details()
        show_the_boards()
        computer_ships()

        for i in range(player_board.size ** 2):
            check_player_guess()
            check_computer_guess()
            score_results()

            """
            - This if statement is for when both the player and
            the computer destroy all the ships at the same round
            - The first elif statement is for when the player
            destroys all the computer ships before the computer does
            - The second elif statement is for when the computer
            destroys all of the player ships before the player does
            """
            if player_score == input_number_of_ships and\
               computer_score == input_number_of_ships:
                print("*" * 40)
                print("It Is A Tie")
                print("Good Luck Next Time")
                print("*" * 40)

            elif player_score == input_number_of_ships:
                print("*" * 40)
                print(f"CONGRATULATIONS {input_name}")
                print(f"You Destroyed All Of The {computer_board.name} Ships")
                print("*" * 40)

            elif computer_score == input_number_of_ships:
                print("*" * 40)
                print("GAME OVER")
                print(f"Sorry {input_name} You Lost")
                print("*" * 40)

            continue_or_quit()

            """
            This if statement is for when one of the following
            conditions occur, the game wiill restart
            1st condition: When the user enters "n" or "N"
            when they are asked if they want to
            continue the game or quit it
            2nd condition: When the user wins
            3rd condition: When the computer wins
            """
            if cont_or_qu.lower() == "n" or\
               player_score == input_number_of_ships or\
               computer_score == input_number_of_ships:
                break

    start_game()
