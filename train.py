from board import *
from agent import *
import numpy as np

EXPLORATION_RATE = 0.2
LEARNING_RATE = 0.1
NUMBER_OF_ROUNDS = 100000


def main():
    agent_train = Agent(EXPLORATION_RATE, LEARNING_RATE)
    agent_train.train(NUMBER_OF_ROUNDS)

    agent = Agent(0, LEARNING_RATE)
    agent.state_actions = agent_train.state_actions

    states = []
    while 1:
        current_state = (agent.x, agent.y)
        action = agent.decide_action()
        states.append(current_state)
        
        print("POSITION: " + str(current_state), end=' ')
        print("ACTION: " + str(action))


        move_tuple = agent.board.move(action)
        agent.board.x = move_tuple[0]
        agent.board.y = move_tuple[1]
        agent.x = agent.board.x
        agent.y = agent.board.y

        
        agent.render(states)

        if agent.board.is_agent_reach:
            break

    print(agent.state_actions)

if __name__ == "__main__":
    main()