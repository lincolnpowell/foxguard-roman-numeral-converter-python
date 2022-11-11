# Roman Numeral to Integer Converter

## Description

Write a program that will accept a string of roman numerals and return the corresponding integer representation.

Valid Roman numerals are I, V, X, L, C, D, M

Standard subtractive notation will be used for 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM)

**Examples**:<br/>
XIII -> 13<br/>
LV -> 55<br/>
XLIX -> 49<br/>
DCCLXXXIX -> 789

## Tutorial

### Dependencies
- [Python](https://www.python.org/downloads/) (_latest_ version **preferred**)

### Command Line Execution
1. Open your terminal of choice
2. Verify Python is on your PATH via `py --version`
3. Execute the program via `py main.py`

**NOTE**: If you receive "Inputted string contains invalid characters", ensure you are inputting valid Roman numeral values I, V, X, L, C, D, M.

## Developer Notes

### Linting and Testing
1. In a terminal, ensure your `pip` is updated via `python -m pip install --upgrade pip`
2. Install necessary local dependencies via `pip install -r requirements.txt`
3. To lint your changes locally, run `flake8 .`
4. To run unit tests locally, run `pytest`