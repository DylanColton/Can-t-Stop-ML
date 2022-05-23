import numpy as np
import random as rnd


def roll(low, high, num_die=1):
    die = np.zeros(num_die)

    for i in range(num_die):
        die[i] = rnd.randint(low, high)

    return die


def cant_stop_combos(num_die=4, low=1, high=6):
    die = roll(low, high, num_die)
    combo_table = [[0, 0, 1, 1],
                   [0, 1, 0, 1],
                   [0, 1, 1, 0]]

    combos = np.zeros([3, 2])

    for i in range(len(combo_table)):
        for j in range(len(combo_table[i])):
            combos[i][combo_table[i][j]] += die[j]

    return combos
