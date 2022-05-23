import numpy as np
import common


class Board:
    def __init__(self, num_players):
        self.boardState = [0] * 11
        for i in range(len(self.boardState)):
            self.boardState[i] = [0] * (12 - np.abs(i - 5) * 2)

        self.players = [0] * num_players
        self.tO = common.roll_turn_order(num_players)
        self.currPlay = 0

    def show_board(self):
        for i in range(len(self.boardState)):
            for j in range(3 * np.abs(i-5)):
                print(" ", end="")
            print(self.boardState[i])

    def display_game_info(self):
        print("Number of Players: " + str(len(self.players)))
        print("Turn Order: " + str(self.tO))
        print("Current Player's Turn: Player " + str(self.currPlay))
        print("Board State:")
        self.show_board()

    def update_board_state(self, player_piece):
        self.boardState[int(player_piece[1]-2)][int(player_piece[0] - 1)] = 0
        # print("Column: " + str(player_piece[1]-2))
        # print("Distan: " + str(player_piece[0]))
        self.boardState[int(player_piece[1]-2)][int(player_piece[0])] = 1

    def column_captured(self):
        for i in range(len(self.boardState)):
            if self.boardState[i][-1] > 0:
                return True
        return False

    def reset(self):
        self.boardState = [0] * 11
        for i in range(len(self.boardState)):
            self.boardState[i] = [0] * (12 - np.abs(i - 5) * 2)

        self.players = [0] * len(self.players)
        self.tO = common.roll_turn_order(len(self.players))
        self.currPlay = 0

