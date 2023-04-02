import random


def dice_roll(dice_size=6):
    """
    Takes dice size as input (default value = 6), returns the result of the random roll.
    :param dice_size: int - size of the dice
    :return: int - result of a single dice roll
    """
    return random.randint(1, dice_size)


