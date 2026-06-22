# AI Tic-Tac-Toe (Unbeatable Edition)

A classic Tic-Tac-Toe game with a twist — the AI opponent never loses.
Built with Python's Tkinter for the interface and the Minimax algorithm 
for decision-making, this project was created as part of my AI internship 
training to apply core game-theory and search-algorithm concepts hands-on.

## How It Works
- The game board is represented as a list of 9 cells.
- The AI uses the **Minimax algorithm** to simulate every possible future 
  move and choose the one that guarantees the best outcome for itself — 
  meaning it will win or draw, but never lose.
- The interface is built with Tkinter, with click-based moves and a 
  restart button to play again instantly.

## Features
- Play as X against an unbeatable AI (O)
- Win, loss, and draw detection
- One-click restart
- Simple, clean GUI

## Tech Stack
- Python
- Tkinter (GUI)
- Minimax algorithm (decision-making logic)

## Run It Yourself
```bash
python tic_tac_toe.py
```
(Requires Python 3 — Tkinter comes built-in with most installations.)

## What I Learned
Building this helped me understand recursive game-tree search, how to 
evaluate game states, and how to translate an AI decision-making concept 
into actual working code rather than just theory.

---
*Built as part of my AI internship training with WeIntern.*
