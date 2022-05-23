import numpy as np
import matplotlib.pyplot as plt
import random as rnd

import rolls


def roll_turn_order(num_players):
    if num_players == 1:
        return [0]

    t_o = np.arange(0, num_players, 1)
    for i in range(len(t_o)):
        t_o[i] = rolls.roll(1, 6)
        while unique_in_list(t_o[i], t_o, i):
            t_o[i] = rolls.roll(1, 6)

    return t_o


def unique_in_list(value, array, ignore):
    for i in range(len(array)):
        if i == ignore:
            continue
        if value == array[i]:
            return True
    return False


def scramble(array):
    for i in range(3 * len(array)):
        j = rnd.randint(0, len(array)-1)
        array[np.mod(i, len(array))], array[j] = array[j], array[np.mod(i, len(array))]
    return array


def sorted_index(array, asc=True):
    sor, hold = np.zeros(len(array)), np.zeros(len(array))

    for i in range(len(array)):
        hold[i] = array[i]
        for j in range(i):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]

    for i in range(len(hold)):
        for j in range(len(array)):
            if array[j] == hold[i]:
                sor[j] = i

    return sor


def not_in_array(value, array):
    for i in range(len(array)):
        if value == array[i]:
            return False
    return True


def get_index_from_key(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1


def is_zero_list(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            return False
    return True


def index_of_largest_value(array):
    ind, largest = 0, 0

    for i in range(len(array)):
        if largest < array[i]:
            largest, ind = array[i], i

    return ind
