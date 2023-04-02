import random


def dice_roll(dice_size=6):
    """
    Takes dice size as input (default value = 6), returns the result of the random roll.
    :param dice_size: int - size of the dice
    :return: int - result of a single dice roll
    """
    return random.randint(1, dice_size)


def user_input():
    """
    Prompts used to input string data defining parameters of dice rolls.
    Takes string in format: xDy+z
    where:
    x - number of dice (optional, default = 1)
    y - size of the single dice from set [3, 4, 6, 8, 10, 12, 20, 100]
    z - modifier (optional, default = 0)
    :return: tuple of int values (number, dice_size, modifier)
    """
    while True:
        input_str = input("Enter a dice you'd like to roll in format xDy+z: ").lower()

        # Test for empty input
        if not input_str:
            print('Invalid input.')
            continue

        # Test for 'd'
        if 'd' not in input_str:
            print('Invalid input.')
            continue

        






user_input()