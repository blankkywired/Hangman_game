# Hangman Game - Python Project

Welcome to the Hangman Game project! 🎮 This is a simple implementation of the classic word-guessing game, built using Python.

## Purpose

This project was created as part of the **100DaysOfCode Python Bootcamp** by **Angela Yu**. The goal is to learn and practice Python programming concepts, such as loops, conditionals, functions, and working with data structures like lists and strings.

The purpose of the Hangman game is to guess a hidden word by suggesting letters within a limited number of attempts. Each incorrect guess brings the player closer to losing the game, while correct guesses help reveal the hidden word.

## How to Play

1. A random word is selected from a list of words(animals).
2. The player must guess the letters of the word, one at a time.
3. The game displays a series of underscores (`_`) representing the unguessed letters.
4. If the guessed letter is correct, it replaces the corresponding underscore.
5. If the guessed letter is incorrect, the player loses an attempt.
6. The player wins if they guess the word correctly within the allowed number of attempts.
7. The player loses if they run out of attempts before guessing the word.

## Features

- Random word selection.
- Dynamic display of the word with underscores for unguessed letters.
- A limited number of incorrect guesses before the player loses.
- Easy-to-follow prompts for the player.

## Installation

To run this project locally, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone the repository:

   ```bash
   git clone https://github.com/blankkywired/Hangman_game.git

## Run
    ```bash
    cd Hangman_game
    python hangmanProject.py
