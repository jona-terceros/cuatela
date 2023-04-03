# Assignment 3 - Sistemas Inteligentes
# Cuatela

# Project Description

- The board starts with the black pieces positioned on the diagonal of the board and the white ones on the opposite diagonal of the board, in this way:

<div align="center">
    <img src="./img/game.PNG" alt="Logo" width="80" height="80">
  </a>

- In the game always start playing the black pieces, Each piece can be moved in 8 directions horizontally, vertically or diagonally (N,S,E,O, NE, NO, SE, SW) when possible and there is no obstruction. You always move the maximum number of free places you have in that direction and the player who arranges his four chips horizontally, vertically, forming a square or positioning his chips in the four corners wins.

- To implement the program and make its own decisions, you must define a heuristic that determines the utility value of a state, define a maximum height to expand the game tree that will decide how far said tree should be explored, and Implement the algorithm MinMax + α − βpruning and MinMaxW ithDepth(cut − off).

# how to run the code

- make a git clone:

https://github.com/jona-terceros/cuatela.git

- run: python main.py

# Solution description

- Describing the solution to the problem, the first thing that was done was to create the board on which the games will be played.
We define the rules that are required which is explained in assignment 3.
We create a function which allows us to know the format of the tab.
We create a function choose_piece that chooses which piece to start the game with.
From the main.py a validation is made for which player starts first, the bot or the human.
To understand the heuristics a bit, basically you should maximize the probability of winning in the game.
Implemented the algorithm MinMax + α −β pruning and MinMaxWithDepth(cut −off) to find the best possible move in the game tree.


# Heuristics used.






