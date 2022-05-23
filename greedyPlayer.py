import numpy as np
import random as rnd
import player
import common


class GreedyPlayer(player.Player):
    def __init__(self):
        super().__init__()
        self.deltaTurns = 0

    def start_turn(self):
        for i in range(len(self.neutralPieces)):
            self.neutralPieces[i, 0], self.neutralPieces[i, 1] = self.solidPieces[i, 0], self.solidPieces[i, 1]
        self.deltaTurns = 0

    def update_neutral_pieces(self, move):
        for i in range(len(self.neutralPieces)):
            if self.neutralPieces[i, 1] == move or self.neutralPieces[i, 1] == -1:
                self.neutralPieces[i, 0] += 1
                self.neutralPieces[i, 1] = move
                if self.neutralPieces[i, 0] == (12-2*np.abs(move-7)):
                    self.neutralPieces[i, 0] = self.neutralPieces[i, 0] - 1
                break

        self.deltaTurns += 1

    def evaluate_reward(self, col):
        ind = 0
        for i in range(len(self.neutralPieces)):
            if self.neutralPieces[i, 1] == col:
                ind = i

        return float((self.neutralPieces[ind, 0] + 1)) / float((12 - 2 * np.abs(col - 7)))

    def choose_a_pair(self, valid):
        eval_pairs = [0] * len(valid)

        for i in range(len(valid)):
            for j in range(len(valid[i])):
                eval_pairs[i] += self.evaluate_reward(valid[i][j])

        if common.is_zero_list(eval_pairs):
            if len(valid) == 0:
                return valid
            return valid[int(rnd.randint(0, len(valid)-1))]
        return valid[int(common.index_of_largest_value(eval_pairs))]

    def choose_a_move(self, pair):
        eval_moves = [0] * len(pair)

        for i in range(len(pair)):
            eval_moves[i] = self.evaluate_reward(pair[i])

        if common.is_zero_list(eval_moves):
            return pair[0] if rnd.random() < 0.5 else pair[1]
        return pair[int(common.index_of_largest_value(eval_moves))]

    def stop_playing(self):
        # Let's say that after 4 turns we should really stop
        return True if rnd.random() < (0.5 + self.deltaTurns/8) else False