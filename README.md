# Cliff-Walking-Q-Learning
Cliff Walking Q-Learning

This is a standard undiscounted, episodic task, with start and end state, and the usual actions causing movement north (n), south (s), east (e), and west (w). Reward is 1 on all transitions except those into the region marked “The Cliff” Stepping into this region incurs a reward of -100 and sends the agent instantly back to the start. If the agent reachs the end get +100. 

## Q-Learning
Defined by,<br />
![Q-Learning Formula](https://gokseltokur.com/rawimgs/q-learning.png)

![Q-Learning Code](https://gokseltokur.com/rawimgs/q-learning2.png)

### Notation
First Header  | Second Header
------------- | -------------
Q  | Value
S  | State
A  | Action
α  | Learning Rate
r  | Reward
γ  | Discount Factor
t  | Represents the time e.g. (t+1) -> future / t -> old  

## Example output of the 250 rounds of training with exploration rate of 0.2 and learning rate of 0.5

S -> Start point<br />
E -> End point (Goal)<br />
0 -> Plain<br />
X -> Cliff<br />
``#`` -> Path that agent went<br />

![Cliff Walking Q-Learning Example Output](https://gokseltokur.com/rawimgs/output-of-walking.png)

## To Run
You can directly run the __train.py__
`python train.py` 
