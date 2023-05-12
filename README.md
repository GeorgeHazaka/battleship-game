# Ultimate Battleships


Ultimate Battleships is a python game, which runs in the Code Institute mock terminal on Heroku.

Users can try and sink all of the computer's ships before the computer sinks all of their ships. Each battleship occupies one square on the board. Users try and hit them by calling out the coordinates of one of the squares on the board.

[Here is the live version of my project](https://ultimate-battleship-game.herokuapp.com/)

![Sevelral screen sizes devices showing how the game looks in each of them](documentation/Sk%C3%A4rmbild%20(80).png)

## How to play
----

Ultimate Battleships is based on the classic pen-and-paper game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))

In this version, the player enters their name and the desired amount of ships then two boards are randomly generated.

The player can see where their ships are, indicated by an `@` sign, but cannot see where the computer's ships are.

If guesses miss, they are marked on the board with an `X`.

If guesses hit, they are indicated by `*`.

The player and the computer then take it in turns to make guesses and try to sink each other's battleships.

The winner is the player who sinks all of their opponent's ships first.

## Design
----

### Flow Diagram

To structure and aid tin creating the game, a basic flow diagram was created which is linked below.

[Flow Diagram]()

### Wireframes

Please see below, a link to wireframes for the game layout.

[Wireframes]()

## Features
----

### Existing Features

+ #### Introduction to the game

    ![battleships game introduction](documentation/introduction-battleships.png)
+ #### Accepts user name input

    ![user name input](documentation/input-name-battleships.png)
+ #### Accepts user desired amount of ships (between 5 and 10)

    ![number of battleships input](documentation/input-number-of-ships-battleships.png)

+ #### Random board generation

    + Ships are randomly placed on both the player and the computer boards.
    + The player cannot see where the computer's ships are.

    ![player's board and computer's board](documentation/boards-battleships.png)

+ #### Play against the computer

+ #### Accepts user desired row and column

    ![Player's guess and the computer's guess and showing both of the boards](documentation/row-and-column-battleships.png)

+ #### Maintains scores

    ![Player's and computer's scores](documentation/scores-battleships.png)

+ #### Asks the user after every round if they want to continue playing or quit
    + User have two choices:
        + User enters `n`, in that case the game will quit and restart

            ![game restarts after user entered "n"](documentation/n-quit-the-game-battleships.png)

        + User enters any key other than `n`,  in that case the game will continue

            ![game continues after user entered any key other than "n"](documentation/continue-playing-battleships.png)

+ #### Provides informative message when the game ends
    + Three possible ways that the game would end up with
        + If the player wins the game, the following message appears

            ![player winning message](documentation/win-message-battleships.png)

        + If the player loses the game, the following message appears

            ![player losing message](documentation/losing-message-battleships.png)

        + If both the player and the computer destroy all of each other ships at the same turn, the following message appears

            ![draw message](documentation/draw-message-battleships.png)

+ #### Input validation and error-checking
    + User cannot enter an empty name

        ![empty name error](documentation/error-empty-name-battleships.png)

    + User must enter an integer to the number of ships input

        ![value-error of number of ships](documentation/value-error-number-of-ships-battleships.png)

    + User cannot enter number of ships that is lower than 5 or higher than 10

        ![invalid number error of number of ships](documentation/error-wrong-number-of-ships-battleships.png)

    + User must enter an integer to both the row and column guesses

        ![value-error of row and column](documentation/value-error-row-column-battleships.png)

    + User cannot guess a row or a column that is lower than 1 or higher than 5

        ![invalid guess of row and column](documentation/error-row-column-wrong-number-battleships.png)

    + User cannot enter the same guess (coordinates) twice

        ![cannot guess the same coordinates twice](documentation/error-coordinates-twice.png)