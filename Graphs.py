import matplotlib.pyplot as plt
import compare_players
import random as rnd
import intelligence
import numpy as np
import common
import board
import rolls
import hold


def get_lower_and_upper(arr):
    lower = (arr[0] + 1) * 50
    upper = (arr[0] + 1) * (-50)

    for i in range(len(arr)):
        if arr[i] < lower:
            lower = arr[i]
        if arr[i] > upper:
            upper = arr[i]

    return lower, upper


def gain_data(trails, games, rounds, player, confidence):
    dataX, dataY = compare_players.repeat_trials(trails + 5, games, rounds, player)
    # Exclude a trail to use for a bar graph

    lower = np.zeros(len(dataY[0]))
    median = np.zeros(len(dataY[0]))
    upper = np.zeros(len(dataY[0]))

    for i in range(len(dataY[0])):
        median[i] = np.median(dataY[:, i])
        lower[i] = median[i] - np.percentile(dataY[:, i], 100 - confidence)
        upper[i] = np.percentile(dataY[:, i], confidence) - median[i]

    #
    barY = np.zeros(len(dataY[0]))

    for i in range(len(dataY[0])):
        barY[i] = np.mean(dataY[0:5, i])

    # for i in range(len(dataY[0])):
    #     dataY[0][i] /= (numTrails * numGames * numRounds)
    #
    # for i in range(len(median)):
    #     median[i] /= (numTrails * numGames * numRounds)
    #     lower[i] /= (numTrails * numGames * numRounds)
    #     upper[i] /= (numTrails * numGames * numRounds)

    return dataX[0], barY, lower, median, upper, dataY