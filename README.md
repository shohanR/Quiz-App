# Quiz App

## Version 1

For the `v1` of the `Quiz App`, the software must meet the following requirements. Those are grouped into two areas:

1. Management
1. Game

Let's take a closer look at what we mean.

### Management

Always by selecting voices in a CLI menu, the user should be able to:

1. Add players to the players list. For each player, we need to track only the `username`
1. Add questions to the questions list. The questions consist of:

    - The statement
    - The right answer

Both the players and the questions will be kept in memory (no persistence as of now).

### Game

Within the same menu (along with the administration tasks), we need to present to the user the options to start and play the Quiz game. The features to forecast are:

1. The user can start to play. In this case, there will be a sub-menu that helps the user to set the game up. You can select the following options:

    1. Single player. It asks to select the user.
    1. Multiplayer. It asks to select the two users that face each other.

1. In Single-player mode, it will ask all of the recorded questions to the user
1. In Multiplayer mode, it asks questions randomly to both users. A question cannot be repeated.
1. If a user types in the right answer, it gets a point that sums up the eventual previous ones.
1. When all of the questions have been asked, the game finishes and it reports the winner, if any.

### Technical Specs

1. Preload some questions so you don't have to type in a question every time
1. Preload some users so you can go straight to the game
1. Handle all of the errors that might happen throughout the application
1. If some specs are missing from the doc, feel free to follow what you think it's best as long as you justify it

## Implementation

Please adjust this section by aligning it with the new specs.

```
Quiz App is a simple CLI (Command Line Interface) game that can be run directly from the terminal.
<p>
  <b>At the beginning of the game,</b> a user stores questions and answers against those questions in the program. After every question, user is asked to continue adding question or proceed to the game. Depending on the choice of the user, the program will store Q/A, or proceed to the game.
  <br>
  <br>
  <b>In the second part of the game,</b> user is given choices to play as a solo player, or with multiple players. A game termination choice is present there too. Depending on the choice, player(s) can add his/her (their) username(s), or, terminate the game.
  <br>
  <br>
  <b>In the third part of the game,</b> the program asks who wants to answer question. Then, the user who wants to answer, enters his user name and a random question is shown in the screen. If the answer is correct he receives 10 points. For every correct answer, the user is rewarded with 10 points.
  <br>
  <br>
  The game termination option is always there. Depending on the choice, the game will continue.
  <br>
  <br>
  <b>After the game ends,</b> all points are calculated and the winner is chosen based on accumulated points.
</p>
```
