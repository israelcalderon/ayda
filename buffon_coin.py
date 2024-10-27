import random
from typing import Tuple


def coin_drop() -> Tuple[float, float]:
    """Returns coin drop pseudo random position x, y"""
    return random.random(), random.random()


def coin_droped_in_circle(x: float, y: float) -> bool:
    """Returns True if point x,y is inside a circle with radius 1"""
    return (x**2 + y**2) <= 1


def pi_probability(tries: int) -> float:
    counter = 0  # 2

    for _ in range(tries):
        x, y = coin_drop()  # 3

        if coin_droped_in_circle(x, y):  # 4
            counter += 1  # 5

    return 4 * (counter / tries)  # 6


if __name__ == '__main__':
    tries = int(input('How many tries do you want? '))  # 1
    print(pi_probability(tries))
