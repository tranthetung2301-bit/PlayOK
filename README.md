# PlayOK
Go Game with Pygame

  A simple desktop Go game built with Python and Pygame. The project supports multiple board sizes, basic stone placement, capturing logic, turn switching, pass/resign actions, and a simple game-over screen.

Features
  -Choose board size: 9x9, 13x13, or 19x19
  -Play as Black and White in alternating turns
  -Place stones by clicking on the board
  -Detect occupied positions
  -Basic capture logic based on liberties
  -Prevent suicide moves
  -Basic KO rule handling
  -PASS button
  -RESIGN button
  -Game-over screen with score display
Technologies Used
  -Python
  -Pygame
  -Object-Oriented Programming

 Project Structure
go-game/
├── real_main.py
└── go_engine/
    ├── __init__.py
    ├── BOARD.py
    ├── GAME.py
    └── STONE.py 
