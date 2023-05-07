from random import randint

start_over = True

while start_over:

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


    def check_player_guess():
        """
        Creates a function that checks whether the player
        has already chosen the same coordinates twice
        Checks whether player guess position is uqual to one of the computer ships position
        If it is equal then the Full stop sign "." will become "w"
        Updates the board and prints the updated board
        player_score gets increased by 1
        If it is not equal then the Full stop sign "." will become "X"
        Updates the board and prints the updated board
        """
            
        def indicate_player_duplicate_coordinates():
            """
            Calls player_coordinates_guess() function
            Checks whether the player has already chosen the same coordinates twice
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
        computer_board_list = [dot for dot in computer_board.print_the_computer_board()]

        for x in range(5):
            computer_board_list.remove('\n')
            
        global computer_updated_board_list

        if computer_updated_board_list != None:
            computer_board_list = computer_updated_board_list

        hit = False

        for i in computer_ships_positions_list:
            """
            (y * 5 - (5 - x)) - 1
            This equation is to transform coordinates to a specific position (index)
            y represents the row
            x represents the column
            The number -1 at the end is to make the postion as zero-indexing
            Both the first and the second number 5 represent the amount of columns the board has
            """

            if i == player_guess[0] * 5 - (5 - player_guess[1]):
                print("Player got a hit!")
                computer_board_list[(player_guess[0] * 5 - (5 - player_guess[1])) - 1] = "w"
                computer_updated_board_list = [ch for ch in computer_board_list]

                for y in range(len(computer_board_list)):
                    computer_board_list[y] = "  " + computer_board_list[y]

                for j in range(4, 25, 5):
                    computer_board_list[j] += '\n'

                computer_board_list = "".join(computer_board_list)
                print("-" * 40)
                print(computer_board_list)
                print("-" * 40)

                global player_score
                player_score += 1

                hit = True
                break

                
        if hit == False:
            print("Player missed this time.")
            computer_board_list[(player_guess[0] * 5 - (5 - player_guess[1])) - 1] = "X"
            computer_updated_board_list = [dot for dot in computer_board_list]

            for y in range(len(computer_board_list)):
                computer_board_list[y] = "  " + computer_board_list[y]

            for j in range(4, 25, 5):
                computer_board_list[j] += '\n'

            computer_board_list = "".join(computer_board_list)

            print("-" * 40)
            print(computer_board_list)
            print("-" * 40)


    def check_computer_guess():
        """
        Checks whether computer guess position is uqual to one of the player ships position
        If it is equal then the At sign "@" will become "w"
        Updates the board and prints the updated board
        computer_score gets increased by 1
        If it is not equal then the Full stop sign "." will become "X"
        Updates the board and prints the updated board
        """

        def indicate_computer_duplicate_coordinates():
            """
            Checks whether the computer has already chosen the same coordinates twice
            If so, then the computer will have to guess again
            """
            global computer_guess
            computer_guess = [randint(1, 5), randint(1, 5)]

            for coordinates in computer_all_guesses_list:

                if coordinates == computer_guess:
                    computer_guess = [randint(1, 5), randint(1, 5)]
                    indicate_computer_duplicate_coordinates()
        
        indicate_computer_duplicate_coordinates()

        computer_all_guesses_list.append(computer_guess)

        print(f"Computer guessed ({computer_guess[0]}, {computer_guess[1]})")
        player_board_list = player_board_with_ships.split()

        global player_updated_board_list
        
        if player_updated_board_list != None:
            player_board_list = player_updated_board_list

        if player_board_list[(computer_guess[0] * 5 - (5 - computer_guess[1])) - 1] == "@":
            player_board_list[(computer_guess[0] * 5 - (5 - computer_guess[1])) - 1] = "w"
            player_updated_board_list = [ch for ch in player_board_list]
            print("Computer got a hit!")

            for j in range(4, 25, 5):
                player_board_list[j] += '\n'

            for y in range(len(player_board_list)):
                player_board_list[y] = "  " + player_board_list[y]

            player_board_list = "".join(player_board_list)
            print("-" * 40)
            print(player_board_list)
            print("-" * 40)

            global computer_score
            computer_score += 1

        else:
            player_board_list[(computer_guess[0] * 5 - (5 - computer_guess[1])) - 1] = "X"
            player_updated_board_list = [ch for ch in player_board_list]
            print("Computer missed this time.")

            for j in range(4, 25, 5):
                player_board_list[j] += '\n'

            for y in range(len(player_board_list)):
                player_board_list[y] = "  " + player_board_list[y]

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
        Creates a loop and inside it calls the required functions to play the game, which are:
        - check_player_guess()
        - check_computer_guess()
        - score_results()
        """
        game_details()

        for i in range(25):
            check_player_guess()
            check_computer_guess()
            score_results()

            if player_score == input_number_of_ships and computer_score == input_number_of_ships:
                print("It Is A Tie")
                print("Good Luck Next Time")

            elif player_score == input_number_of_ships:
                print("*" * 40)
                print(f"CONGRATULATIONS {input_name}")
                print("You Destroyed All Of The Enemy Ships")
                print("*" * 40)

            elif computer_score == input_number_of_ships:
                print("*" * 40)
                print("GAME OVER")
                print(f"You Lost {input_name}")
                print("*" * 40)

            continue_or_quit()

        if cont_or_qu.lower() == "n" or player_score == input_number_of_ships or computer_score == input_number_of_ships:

            global start_over
            start_over = True

            break


    start_game()