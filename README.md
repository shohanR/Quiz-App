# Quiz App

## Version 1

For the `v1` of the `Quiz App`, the software must meet the following requirements. Those are grouped into two areas:

1. Management
1. Game

Let's take a closer look at what we mean.

### Management

#### Add Player Page

The user must be able to add a player through a form. On the right side of the page, the user can see the users already added. For each player, we need to track only the `username`.

#### Add Question Page

The user must be able to add a question to a list through a form. The questions consist of:

    - The statement
    - The right answer

On the right side, you can see the already-added questions.  
Both the players and the questions will be kept in memory (no persistence as of now).

### Game

#### Single-Player

It starts by asking you to select a user. Then it asks you all of the questions that have been recorded so far. In the end, it will give you the score.

> When you give an answer, it won't let you know whether the answer is right or not. In the end, the game will give you the ratio of the right answers (e.g. 13/15).  

#### Multi-Player

It lets you select two players. Then it starts asking the questions to the first user. On the last question, you'll see a button that says "Start Player 2". When you click it, the second player starts to answer. In the end, it reports the actual scores of the players.

Within the same menu (along with the administration tasks), we need to present to the user the options to start and play the Quiz game. The features to forecast are:

### Technical Specs

1. Preload some questions so you don't have to type in a question every time
1. Preload some users so you can go straight to the game
1. Handle all of the errors that might happen throughout the application
1. If some specs are missing from the doc, feel free to follow what you think is best as long as you justify it
