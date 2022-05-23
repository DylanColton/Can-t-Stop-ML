import matplotlib.pyplot as plt
import numpy as np
import intelligence
import player
import common
import board


def play(game_board=board.Board(1), ai_player=intelligence.RandomPlayer()):
    turns = 0

    while True:
        ai_player.start_turn()
        while True:
            turns += 1
            valid = ai_player.get_valid_combos()
            # print(valid)

            if len(valid) == 0:
                continue

            pair_choice = ai_player.choose_a_pair(valid)
            move_choice = int(ai_player.choose_a_move(pair_choice))

            ai_player.update_neutral_pieces(move_choice)

            m = ai_player.get_recently_updated(move_choice)
            game_board.update_board_state(ai_player.neutralPieces[m])

            if ai_player.stop_playing():
                ai_player.finalise_moves()
                break

        if game_board.column_captured():
            # print("Game Complete")
            return turns


def play_games_for_rounds(games, rounds, ai):
    total_games = []
    bo = board.Board(1)

    for i in range(rounds):
        n_t = []  # Number of turns it took until victory
        for j in range(games):
            bo.reset()
            ai.reset()
            n_t.append(play(bo, ai))
        n_t = sorted(n_t)
        total_games.append(n_t)
    return total_games


def repeat_trials(times, games, rounds, ai):
    data = []

    hold, counter = [], []

    for i in range(times):
        data = play_games_for_rounds(games, rounds, ai)
        # print(len(data[0]))

        low, high = 100, 0
        for j in range(len(data)):
            for k in range(len(data[j])):
                if low > data[j][k]:
                    low = data[j][k]
                if high < data[j][k]:
                    high = data[j][k]

        hold.append(np.arange(low, high + 1, 1))
        counter.append(np.zeros(len(hold[i])))

        for j in range(len(data)):
            for k in range(len(data[j])):
                for l in range(len(hold[i])):
                    if hold[i][l] == data[j][k]:
                        counter[i][l] += 1

    max_len = 0
    for i in range(len(hold)):
        if len(hold[i]) > max_len:
            max_len = len(hold[i])

    nHold, nCounter = [], []

    for i in range(len(hold)):
        nHold.append([])
        nCounter.append([])
        for j in range(max_len):
            nHold[i].append(low + j)
            if j < len(counter[i]):
                nCounter[i].append(counter[i][j])
            else:
                nCounter[i].append(0)

    hold = np.zeros([len(nHold), len(nHold[0])])
    counter = np.zeros([len(nCounter), len(nCounter[0])])
    for i in range(len(hold)):
        for j in range(len(nHold[0])):
            hold[i, j] = nHold[i][j]
            counter[i, j] = nCounter[i][j]

    return hold, counter
