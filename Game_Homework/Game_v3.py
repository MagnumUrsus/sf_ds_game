"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Использует менее 20 попыток
"""
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1, 101) # это загадаемое компьютером число
    low = 1
    high = 100
    count = 0
    while True:
        yourvalue = round((low+high)/2) 
        count += 1
        if yourvalue == number:
            break
        elif yourvalue <= number:
            low = low + high - high / 2 
        else:
            high = high - 1 - high / 2
    return (count)

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    return score

print(f"Ваш алгоритм угадывает число в среднем за:{score_game(game_core_v3)} попыток")
