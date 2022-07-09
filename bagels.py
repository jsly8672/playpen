# """Bagels, by Al Sweigart al@inventwithpython.com 2. A deductive logic game where you must guess a
# number based on clues. View this code at https://nostarch.com/bigbook-small-python-projects 4.
# A version of this game is featured in the book "Invent Your Own 5. Computer Games with Python"
# https://nostarch.com/inventwithpython 6. Tags: short, game, puzzle.

import random

NUM_DIGITS = 3
MAX_GUESSES = 10
def main():
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:
    That means:
    Pico
    One digit is correct but in the wrong position.
    Fermi
    One digit is correct and in the right position.
    Bagels
    No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

