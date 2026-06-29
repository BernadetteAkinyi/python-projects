# Number Guessing Game 🎲

A simple command-line number guessing game written in Python.

## Description

The Number Guessing Game is a beginner-friendly Python project that challenges the player to guess a randomly generated number between **1 and 99**.

The player has **7 attempts** to guess the correct number. After each guess, the game provides feedback indicating whether the guess is too high or too low. If the player guesses correctly, the game displays a congratulatory message along with the number of attempts taken. If the player fails to guess the number within 7 attempts, the correct number is revealed.

The program also handles invalid input gracefully using exception handling, preventing the game from crashing when a non-numeric value is entered.

## Features

- Generates a random number between 1 and 99.
- Allows up to 7 guessing attempts.
- Provides hints when a guess is too high or too low.
- Displays the number of attempts used after a successful guess.
- Reveals the correct number if all attempts are exhausted.
- Handles invalid (non-numeric) input using `try` and `except`.
- Uses formatted strings (f-strings) for clean output.

## Concepts Practiced

This project demonstrates the following Python concepts:

- Variables
- User input (`input()`)
- Type conversion (`int()`)
- The `random` module
- `for` loops
- Conditional statements (`if`, `elif`, `else`)
- Boolean variables (`True` and `False`)
- `break` and `continue`
- Exception handling (`try` and `except`)
- Formatted string literals (f-strings)

## Project Structure

```
numberguess.py
README.md
```

## Requirements

- Python 3.x

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python numberguess.py
```

or

```bash
python3 numberguess.py
```

## Example Output

```
Attempt 1 of 7.
Guess a number between 1 and 99: 30
Too low! Try a higher number.

Attempt 2 of 7.
Guess a number between 1 and 99: 80
Too high! Try a lower number.

Attempt 3 of 7.
Guess a number between 1 and 99: 54
Correct!
You guessed the number in 3 attempts!
```

## Future Improvements

Some possible enhancements include:

- Count only valid guesses as attempts.
- Validate that guesses are between 1 and 99.
- Add difficulty levels (Easy, Medium, Hard).
- Allow the player to play multiple rounds without restarting the program.
- Keep track of the best score.
- Add a menu and game instructions.

## Author

**Bernadette Akinyi**

Built as a beginner Python project to practice programming fundamentals, problem-solving, loops, conditionals, exception handling, and user interaction.
