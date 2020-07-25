# Cliff-Walking-Q-Learning
Cliff Walking Q-Learning

This is a standard undiscounted, episodic task, with start and end state, and the usual actions causing movement north (n), south (s), east (e), and west (w). Reward is 1 on all transitions except those into the region marked “The Cliff” Stepping into this region incurs a reward of -100 and sends the agent instantly back to the start. If the agent reachs the end get +100. 

Example output of the 250 rounds of training with exploration rate of 0.2 and learning rate of 0.5

![Cliff Walking Q-Learning Example Output](https://gokseltokur.com/output-of-walking.png)



