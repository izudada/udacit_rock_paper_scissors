import random
import time


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
player_scores = {
    "player1": 0,
    "player2": 0
}

print("Rock Paper Scissors, Go! ")

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(string):
    print(string)
    time.sleep(1)


def beats(one, two):
    criteria = ''
    if (one == 'rock' and
            two == 'scissors') or (one == 'scissors' and two == 'rock'):
        criteria = 'rock'
    elif (one == 'paper' and
            two == 'scissors') or (one == 'scissors' and two == 'paper'):
        criteria = 'scissors'
    elif (one == 'paper' and
            two == 'rock') or (one == 'rock' and two == 'paper'):
        criteria = 'paper'

    if criteria == one:
        print_pause("** PLAYER ONE WINS **")
        player_scores['player1'] += 1
    elif criteria == two:
        print("** PLAYER TWO WINS **")
        player_scores['player2'] += 1
    elif one == two:
        print_pause("It's a tie")

    print_pause(f"Score: Player One {player_scores['player1']} , "
                "Player Two {player_scores['player2']}")


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        self.opponent_moves = []

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.opponent_moves.append()


class HumanPlayer(RandomPlayer):
    def move(self):
        human_input = input("Rock, paper, scissors? > ")
        return human_input


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1} Opponent played {move2}")
        beats(move1, move2)
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
