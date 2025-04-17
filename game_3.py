import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        guess = (low + high) // 2
        if guess == number:
            break
        elif guess < number:
            low = guess + 1
        else:
            high = guess - 1

    return count

# RUN
if __name__ == '__main__':
    game_core_v3