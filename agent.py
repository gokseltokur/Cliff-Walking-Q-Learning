from board import *
import numpy as np

class Agent:
    def __init__(self, exploration_rate, learning_rate):
        self.board = Board()
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.x = self.board.x
        self.y = self.board.y
        self.actions = ['n', 's', 'w', 'e']

        self.states = []
        # Dictionary
        self.state_actions = {}

        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                self.state_actions[(i, j)] = {}
                for k in self.state_actions:
                    self.state_actions[(i, j)][k] = 0
        
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def reset(self):
        if self.board[(self.x, self.y)] == -1:
            self.x = self.board.startx
            self.y = self.board.starty

    def decide_action(self):
        action = None
        threshold_reward = -1000
        if self.exploration_rate >= np.random.uniform(0, 1):
            return np.random.choice(self.actions)
        else:
            for i in self.actions:
                currentx = self.x
                currenty = self.y
                reward = self.state_actions[(self.x, self.y)][a]
                if reward >= threshold_reward:
                    action = i
                    threshold_reward = reward
        return action

    def play(self, rounds):
        for i in range(rounds):
            while 1:
                current_state = (self.x, self.y)
                current_reward = self.board.reward()
                action = self.decide_action()

                # Calculate actions' reward
                self.board.x = self.board.move(action)
                self.x = self.board.x
                self.y = self.board.y





    




if __name__ == "__main__":
    agent = Agent(0.3, 0.1)
    agent.board.print()