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


def game_score():
    print_pause("""Score: Player One {} , Player Two {}
        """.format(player_scores['player1'], player_scores['player2']))


def beats(one, two):
    """
        A function that determines
        who wins and who losses
    """
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

    game_score()


class Player:
    """
        A player blueprint
    """
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    """
        A random player whose move
        is chosen at random
    """
    def move(self):
        return random.choice(moves)


class HumanPlayer(RandomPlayer):
    """
        Human player that enter a move
        to play a round
    """

    def user_input(self):
        human_input = input("Rock, paper, scissors? > ").lower()
        return human_input

    def move(self):
        user_data = self.user_input()
        if user_data not in moves:
            user_data = self.move()

        return user_data


class ReflectPlayer(RandomPlayer):
    """
        A player that makes a move depending
        what the previous oppponent's move was
    """
    def __init__(self):
        self.opponent_moves = ''

    def move(self):
        if self.opponent_moves == '':
            self.opponent_moves = random.choice(moves)

        return self.opponent_moves

    def learn(self, my_move, their_move):
        self.opponent_moves = their_move


class CyclePlayer(RandomPlayer):
    """
        A class with the behaviour to
        recall its previous move and
        choose a different move in
        the following round.
        For the first move, it is chosen
        at random.
    """
    def __init__(self):
        self.moves = []

    def move(self):
        new_move = random.choice(moves)
        if new_move in moves:
            new_move = random.choice(moves)

        return new_move

    def learn(self, my_move, their_move):
        self.moves.append(my_move)


class Game:
    """
        Game class that takes care of the
        sequence of operation of the game
    """
    def __init__(self, p1, p2):
        """
            A constructor that creates two
            player when instantiated
        """
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        """
            Method that executes per round
        """
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1} Opponent played {move2}")
        beats(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """
            Method for for all rounds of
            an entire game session
        """
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        game_score()


#   Code to run if this file was executed directly without importing it
if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
