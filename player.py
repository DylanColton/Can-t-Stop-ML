import numpy as np
import rolls


class Player:
    def __init__(self):
        self.solidPieces = np.zeros([3, 2])
        self.solidPieces[:, :] = -1
        self.neutralPieces = np.zeros([3, 2])
        self.neutralPieces[:, :] = -1

    def start_turn(self):
        for i in range(len(self.neutralPieces)):
            self.neutralPieces[i, 0], self.neutralPieces[i, 1] = self.solidPieces[i, 0], self.solidPieces[i, 1]

    def finalise_moves(self):
        for i in range(len(self.neutralPieces)):
            self.solidPieces[i, 0], self.solidPieces[i, 1] = self.neutralPieces[i, 0], self.neutralPieces[i, 1]

    def get_valid_combos(self):
        # all_in_play = True
        # for i in range(len(self.neutralPieces)):
        #     if self.neutralPieces[i, 1] == -1:
        #         all_in_play = False
        #         break
        #
        # if not all_in_play:
        #     return combos

        combos = rolls.cant_stop_combos()

        if self.neutralPieces[-1][1] == -1:
            return combos

        valid = []
        for i in range(len(self.neutralPieces)):
            for j in range(len(combos)):
                if self.neutralPieces[i, 1] == combos[j][0] or self.neutralPieces[i, 1] == combos[j][1]:
                    valid.append(combos[j])
        return valid

    def update_neutral_pieces(self, move):
        for i in range(len(self.neutralPieces)):
            if self.neutralPieces[i, 1] == move or self.neutralPieces[i, 1] == -1:
                self.neutralPieces[i, 0] += 1
                self.neutralPieces[i, 1] = move
                if self.neutralPieces[i, 0] == (12-2*np.abs(move-7)):
                    self.neutralPieces[i, 0] = self.neutralPieces[i, 0] - 1
                break

    def get_recently_updated(self, value):
        ind = -1
        for i in range(len(self.neutralPieces)):
            if self.neutralPieces[i, 1] == value:
                return i
        return ind

    def reset(self):
        self.solidPieces = np.zeros([3, 2])
        self.solidPieces[:, :] = -1
        self.neutralPieces = np.zeros([3, 2])
        self.neutralPieces[:, :] = -1

    def display_neutral_positions(self):
        print("Neutral Pieces:")
        for i in range(len(self.neutralPieces)):
            print(self.neutralPieces[i])

    def display_solid_positions(self):
        print("Solid Pieces:")
        for i in range(len(self.solidPieces)):
            print(self.solidPieces[i])
