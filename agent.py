from board import *
import numpy as np
import queue
q = queue.Queue(maxsize=20)

class Agent:
    def __init__(self, exploration_rate, learning_rate):
        self.board = Board()
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        self.x = self.board.x
        self.y = self.board.y
        self.actions = ["n", "s", "w", "e"]

        self.states = []
        # Dictionary
        self.state_actions = {}


        for i in range(len(self.board.board)):
            for j in range(len(self.board.board[0])):
                self.state_actions[(i, j)] = {}
                for k in self.actions:
                    self.state_actions[(i, j)][k] = 0

        #print(self.state_actions)
        
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def reset(self):
        self.states = []
        self.board = Board()
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
                #print(currentx, currenty, i)
                reward = self.state_actions[(currentx, currenty)][i]
                if reward >= threshold_reward:
                    action = i
                    threshold_reward = reward
        return action

    def train(self, rounds):
        for i in range(rounds):
            number_of_steps = 0
            print('Round: ' + str(i))
            sum_reward = 0
            max_reward = -99999
            while 1:
                current_state = (self.x, self.y)
                current_reward = self.board.reward()
                action = self.decide_action()

                # Calculate actions' reward
                move_tuple = self.board.move(action)
                self.board.x = move_tuple[0]
                self.board.y = move_tuple[1]
                self.x = self.board.x
                self.y = self.board.y
                
                
                number_of_steps += 1

                self.states.append([current_state, action, current_reward])

                # Calculate total reward of the round
                sum_reward += sum_reward + self.board.reward()

                # Get maximum of the rounds' reward
                if sum_reward > max_reward:
                    max_reward = sum_reward

                if self.board.is_agent_die or self.board.is_agent_reach:
                    break
            
            if(q.full()):
                q.get()
            print(number_of_steps)
            q.put(int(number_of_steps))

            print("QUEUE:", q.queue[0])
            

            reward = self.board.reward()
            print("REWARD ", sum_reward)


            for j in self.actions:
                self.state_actions[(self.x, self.y)][j] = reward

            for s in reversed(self.states):
                position = s[0]
                action = s[1]
                r = s[2]
                current_value = self.state_actions[position][action]
                reward = current_value + self.learning_rate * (r + reward - current_value)
                self.state_actions[position][action] = round(reward, 3)
                reward = np.max(list(self.state_actions[position].values()))
            

            if self.exploration_rate > 0.005:
                self.exploration_rate -= 0.0001

            
            sum_of_queue = 0
            if(q.full()):
                for e in list(q.queue):
                    sum_of_queue += e

                mean_of_queue = sum_of_queue / q.qsize()

                sum_variance = 0
                for e in list(q.queue):
                    sum_variance += pow((e - mean_of_queue),2)
                    
                variance = sum_variance / (q.qsize() - 1)


                print(q.queue)
                print("MEAN:" , mean_of_queue)
                print("VARIANCE:" , variance)
                if(variance < 10):
                    break

            self.reset()
        print("Maximum Reward of the training of " + str(rounds) + " rounds :" + str(max_reward))

    def render(self, states):
        for i in range(0, len(self.board.board)):
            for j in range(0, len(self.board.board[0])):
                p = ' 0'
                if self.board.board[i, j] == -1:
                    p = ' X'
                if (i, j) in states:
                    p = ' #'
                if i == self.board.endx and j == self.board.endy:
                    p = ' E'
                if i == self.board.startx and j == self.board.starty:
                    p = ' S'
                print(p, end='')
            print()