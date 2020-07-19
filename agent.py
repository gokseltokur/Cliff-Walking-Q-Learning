from board import *

class Agent:
    def __init__(self, exploration_rate, lr):
        self.board = Board()
        self.exploration_rate = exploration_rate
        self.lr = lr
        self.x = self.board.x
        self.y = self.board.y
        self.states = []
        # Dictionary
        self.possible_actions = {}

        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                self.possible_actions[(i, j)] = {}
                for k in self.possible_actions:
                    self.possible_actions[(i, j)][k] = 0
        


if __name__ == "__main__":
    agent = Agent(0.3, 0.1)
    agent.board.print()