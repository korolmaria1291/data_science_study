import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1  # Нижняя граница нашего диапазона
    high = 100  # Верхняя граница нашего диапазона

    while True:
        count += 1
        guess = (low + high) // 2  # Делим наш диапазон пополам
        if guess == number:
            break  # Выход из цикла если угадали
        elif guess < number:
            low = guess + 1  # Прибавляем один к нижней границе
        else:
            high = guess - 1  # Вычитаем один от верхней границы

    return count

# RUN
if __name__ == '__main__':
    game_core_v3