# Ultimate Battleships


Ultimate Battleships is a python game, which runs in the Code Institute mock terminal on Heroku.

Users can try and sink all of the computer's ships before the computer sinks all of their ships. Each battleship occupies one square on the board. Users try and hit them by calling out the coordinates of one of the squares on the board.

[Here is the live version of my project](https://ultimate-battleship-game.herokuapp.com/)

![Sevelral screen sizes devices showing how the game looks in each of them](documentation/respnsive-battleships.png)

## Table Of Contents
----

+ [How To Play](#how-to-play "How To Play")
+ [Design](#design "Design")
    + [Flow Diagram](#flow-diagram "Flow Diagram")
    + [Wireframes](#wireframes "Wireframes")
+ [Features](#features "Features")
    + [Existing Features](#existing-features "Existing Features")
        + [Introduction To The Game](#introduction-to-the-game "Introduction To The Game")
        + [Accepts User Name Input](#accepts-user-name-input "Accepts User Name Input")
        + [Accepts User Desired Board Size](#accepts-user-desired-board-size "Accepts User Desired Board Size")
        + [Accepts User Desired Amount Of Ships](#accepts-user-desired-amount-of-ships "Accepts User Desired Amount Of Ships")
        + [Random Board Generation](#random-board-generation "Random Board Generation")
        + [Play Against The Computer](#play-against-the-computer "Play Against The Computer")
        + [Accepts User Desired Row And Column](#accepts-user-desired-row-and-column "Accepts User Desired Row And Column")
        + [Maintains Scores](#maintains-scores "Maintains Scores")
        + [Asks The User To Continue Playing Or Quit](#asks-the-user-to-continue-playing-or-quit "Asks The User To Continue Playing Or Quit")
        + [Provides Informative Message When The Game Ends](#provides-informative-message-when-the-game-ends "Provides Informative Message When The Game Ends")
        + [Input Validation And Error-checking](#input-validation-and-error-checking "Input Validation And Error-checking")
    + [Features Left to Implement](#features-left-to-implement "Features Left to Implement")
+ [User Experience](#user-experience "User Experience")
+ [Data Model](#data-model "Data Model")
+ [Testing](#testing "Testing")
    + [Manual Testing](#manual-testing "Manual Testing")
        + [Input Testing](#input-testing "Input Testing")
        + [Input Errors Testing](#input-errors-testing "Input Errors Testing")
            + [Name Input Error Testing](#name-input-error-testing "Name Input Error Testing")
            + [Board Size Input Error Testing](#board-size-input-error-testing "Board Size Input Error Testing")
            + [Number Of Ships Error Testing](#number-of-ships-error-testing "Number Of Ships Error Testing")
            + [Guess A Row Error Testing](#guess-a-row-error-testing "Guess A Row Error Testing")
            + [Guess A Column Error Testing](#guess-a-column-error-testing "Guess A Column Error Testing")
    + [Validator Testing](#validator-testing "Validator Testing")
    + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
    + [Content](#content "Content")

## How to play
----

Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, the player enters their name, the board size and the desired amount of ships, then two boards are randomly generated.

The player can see where their ships are, indicated by an `@` sign, but cannot see where the computer's ships are.

If guesses miss, they are marked on the board with an `X`.

If guesses hit, they are indicated by `*`.

The player and the computer then take it in turns to make guesses and try to sink each other's battleships.

The winner is the player who sinks all of their opponent's ships first.

## Design
----

### Flow Diagram

To structure and aid in creating the game, a basic flow diagram was created which is linked below.

[Flow Diagram](documentation/battleships-diagram.pdf)

### Wireframes

Please see below, a link to wireframes for the game layout.

[Wireframes](documentation/battleships-wireframe.pdf)

## Features
----

### Existing Features

+ #### Introduction To The Game

    ![battleships game introduction](documentation/introduction-battleships.png)
+ #### Accepts User Name Input

    ![user name input](documentation/input-name-battleships.png)

+ #### Accepts User Desired Board Size
    + User can choose a board size between 3 and 10

    ![board size input](documentation/board-size-input-battleships.png)
+ #### Accepts User Desired Amount Of Ships
    + The amount of ships is based on the size of the board.
    + The amount of ships must be between x and (x * x - x), where x represents the size of the board.

    ![number of battleships input](documentation/number-of-ships-input-battleships.png)

+ #### Random Board Generation

    + Ships are randomly placed on both the player and the computer boards, the board size and the amount of ships are chosen by the user.
    + The player cannot see where the computer's ships are.

    ![player's board and computer's board](documentation/boards-battleships.png)

+ #### Play Against The Computer

+ #### Accepts User Desired Row And Column

    ![Player's guess and the computer's guess and showing both of the boards](documentation/row-and-column-battleships.png)

+ #### Maintains Scores

    ![Player's and computer's scores](documentation/scores-battleships.png)

+ #### Asks The User To Continue Playing Or Quit

    + After every round the user is asked whether they want to continue playing or quit the game.
    + User have two choices:
        + User enters `n`, in that case the game will quit and restart

            ![game restarts after user entered "n"](documentation/n-quit-the-game-battleships.png)

        + User enters any key other than `n`,  in that case the game will continue

            ![game continues after user entered any key other than "n"](documentation/continue-playing-battleships.png)

+ #### Provides Informative Message When The Game Ends
    + Three possible ways that the game would end up with
        + If the player wins the game, the following message appears

            ![player winning message](documentation/win-message-battleships.png)

        + If the player loses the game, the following message appears

            ![player losing message](documentation/lose-message-battleships.png)

        + If both the player and the computer destroy all of each other ships at the same turn, the following message appears

            ![draw message](documentation/draw-message-battleships.png)

+ #### Input Validation And Error-checking
    + User cannot enter an empty name

        ![empty name error](documentation/error-empty-name-battleships.png)

    + User must enter an integer to the board size input

        ![value-error of board size input](documentation/value-error-board-size-battleships.png)

    + User cannot enter board size number that is:
        + Lower than 3
        + Higher than 10

        ![invalid number error of board size input](documentation/error-board-size-battleships.png)

    + User must enter an integer to the number of ships input

        ![value-error of number of ships input](documentation/value-error-number-of-ships-battleships.png)

    + User cannot enter number of ships that is:
        + Lower than the board size.
        + Higher than board size * board size - board size or (x * x - x)

        ![invalid number error of number of ships input](documentation/error-number-of-ships-battleships.png)

    + User must enter an integer to both the row and column guesses

        ![value-error of row and column](documentation/value-error-row-column-battleships.png)

    + User cannot guess a row or a column that is lower than 1 or higher than 5

        ![invalid guess of row and column](documentation/error-row-column-wrong-number-battleships.png)

    + User cannot enter the same guess (coordinates) twice

        ![cannot guess the same coordinates twice](documentation/error-coordinates-twice.png)

### Features Left To Implement

+ Allow player to position ships themselves.
+ Have ships larger than 1x1.
+ Allow players to change diffulty by changing the size of each board separately.

## User Experience
----
+ **User Story 001:** as a user I want to enter my name.
    + **Tasks:** when the game starts, it will welcome you to the game with basic information, then it is going to ask you "Please enter your name:" that's when you can type your name and press `Enter` when you are done.
+ **User Story 002:** as a user I want to choose the board size.
    + **Tasks:** after you type your name, the game will ask you "Please enter the board size between 3 and 10:". That's when you can type the desired board size between 3 and 10 and press `Enter` when you are done.
+ **User Story 002:** as a user I want to choose the amount of ships.
    + **Tasks:** after choosing the board size, the game will ask you "Please choose the number of ships, between (board size) and (board size * board size - board size)". That's when you can type the desired number of ships and press `Enter` when you are done.
+ **User Story 003:** as a user I want to choose a row and a column.
    + **Tasks:** after choosing the desired amount of ships, the game will ask you "Guess a row:" that's when you can type the desired raw number between 1 and 5 and press `Enter` when you are done. After that the game will ask you "Guess a column" that's when you can type the desired column number between 1 and 5 and press `Enter` when you are done.
+ **User Story 004:** as a user I want to see both of my board and the computer's board.
    + **Tasks:** after choosing the desired row and column, the game will show you both of your board and the computer's board, providing information whether you and the computer have missed or got a hit.
+ **User Story 005:** as a user I want to know what is my score and the computer's score.
    + **Tasks:** after each turn/guess, the game will say "After this round, the scores are: " "You: ?, Computer: ?".
+ **User Story 006:** as a user I want to know when I am able to quit the game.
    + **Tasks:** after each turn/guess and after the game showing you the scores, the game will ask you "Enter any key to continue or "n" to quit". Type `n` and press `Enter`, that will make the game quit and restart. Typing anything else than `n` and pressing `Enter` will make the game continue.

## Data Model
----
+ I decided to use a Board class as my model. The game creates two instances of the Board class to hold the player's and the computer's board.

+ The Board class stores the player's name, the board size and number of ships on the board.

+ The class also has 5 methods which are:
    1. `get_player_name()` is to ask the user to type their name
    2. `get_board_size()` is to ask the user to choose a board size
    3. `get_number_of_ships()` is to ask the user to choose number of ships
    4. `print_the_player_board()` is to create the player's board and print it
    5. `print_the_computer_board()` is to create the computer's board and print it

## Testing
----
+ I have tested that the game works in different browsers: Firefox, Brave, Chrome, Microsoft Edge.
+ I have tested that the game works in my local terminal and the Code Institute Heroku terminal
+ I confirm that all inputs work properly.

### Manual Testing

+ #### Input Testing

    | Feature                    | When The Following Message Appears | Expect | Action | Result |
    | -------------------------- | ---------------------------------- | ------ | ------ | ------ |
    | **Name Input**             | Please enter your name | Whatever is written in the field, becomes the player's name | Entered a name | Player's name became the entered name |
    | **Board Size Input**       | Please enter the board size between 3 and 10 | The number written in the field, becomes the board size | Entered a number | Board size became the entered number |
    | **Number Of Ships Input**  | Please choose the number of ships, between ? and ? | The number written in the field, becomes the number of ships | Entered a number | Number of ships became the entered number |
    | **Continue Or Quit Input** | Enter any key to continue or n to quit | If `n` is entered, the game quits and restarts | Entered `n` | Game quitted and restarted |
    | **Continue Or Quit Input** | Enter any key to continue or n to quit | If anything else than `n` is entered, the game continues | Entered anything else than `n` | Game continued |
    | **Play Again Input** | Enter any key to continue | Game starts again | Entered anything | Game started again |

+ #### Input Errors Testing

    + ##### Name Input Error Testing

        | Error                | When The Following Message Appears | Expected Error | Action | Result |
        | -------------------- | ---------------------------------- | ------ | ------ | ------ |
        | **Empty Name Error** | Please enter your name: | Invalid Data: Name field must not remain empty, please enter your name | Entered an empty space or entered nothing | Invalid Data: Name field must not remain empty, please enter your name |

    + ##### Board Size Input Error Testing

        | Error                         | When The Following Message Appears | Expected Error | Action | Result |
        | ----------------------------- | ---------------------------------- | ------ | ------ | ------ |
        | **Value Error**               | Please enter the board size between 3 and 10: | Value error: You must enter an integer, please try again | Entered anything but an integer | Value error: You must enter an integer, please try again |
        | **Out Of Bounds Input Error** | Please enter the board size between 3 and 10: | Invalid Data: You must enter an integer between 3 and 10, please try again | Entered an integer out of bounds | Invalid Data: You must enter an integer between 3 and 10, please try again |

    + ##### Number Of Ships Error Testing

        | Error                         | When The Following Message Appears | Expected Error | Action | Result |
        | ----------------------------- | ---------------------------------- | ------ | ------ | ------ |
        | **Value Error**               | Please choose the number of ships, between ? and ?: | Value error: You must enter an integer, please try again | Entered anything but an integer | Value error: You must enter an integer, please try again |
        | **Out Of Bounds Input Error** | Please choose the number of ships, between ? and ?: | Invalid Data: You must enter an integer between ? and ?, please try again | Entered an integer out of bounds | Invalid Data: You must enter an integer between ? and ?, please try again |

    + ##### Guess A Row Error Testing

        | Error                         | When The Following Message Appears | Expected Error | Action | Result |
        | ----------------------------- | ---------------------------------- | ------ | ------ | ------ |
        | **Value Error**               | Guess a row: | Value error: You must enter an integer, please try again | Entered anything but an integer | Value error: You must enter an integer, please try again |
        | **Out Of Bounds Input Error** | Guess a row: | Invalid Data: You must enter an integer between 1 and ?, please try again | Entered an integer out of bounds | Invalid Data: You must enter an integer between 1 and ?, please try again |

    + ##### Guess A Column Error Testing

        | Error                         | When The Following Message Appears | Expected Error | Action | Result |
        | ----------------------------- | ---------------------------------- | ------ | ------ | ------ |
        | **Value Error**               | Guess a column: | Value error: You must enter an integer, please try again | Entered anything but an integer | Value error: You must enter an integer, please try again |
        | **Out Of Bounds Input Error** | Guess a column: | Invalid Data: You must enter an integer between 1 and ?, please try again | Entered an integer out of bounds | Invalid Data: You must enter an integer between 1 and ?, please try again |

### Validator Testing

+ Passed the code through a [PEP8 linter](https://pep8ci.herokuapp.com/) and confirmed that no errors were found.

    ![PEP8 validator](documentation/validator-battleships.png)

### Unfixed Bugs

+ No unfixed bugs.

## Deployment
----
This project was deployed using Code Institute's mock terminal for Heroku

+ Steps for deployment:
    + Fork or clone this repository
    + Create a new Heroku app
    + Set the buildbacks to `python` and `NodeJS` in that order
    + Link the Heroku app to the repository
    + Click on **Deploy**

## Credits
----

### Content

+ The idea of the Battleships game was taken from [Portfolio 3: Project Submission](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
+ The idea of the Board Class was also taken from [Portfolio 3: Project Submission](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)