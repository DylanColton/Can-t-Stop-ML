import random as rnd
import player
import rolls


class RandomPlayer(player.Player):
    def __init__(self):
        super().__init__()

    def choose_a_pair(self, valid):
        choose = rolls.roll(0, len(valid)-1, 1)

        return valid[int(choose)]

    def choose_a_move(self, pair):
        return pair[0] if rnd.random() < 0.5 else pair[1]

    def stop_playing(self):
        return True if rnd.random() < 0.5 else False