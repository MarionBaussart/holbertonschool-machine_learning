# Deep Q-learning

Versions used:
|            |        |
| -----------|------- |
| Python     | 3.9.0  |
| gym        | 0.25.2 |
| h5py       | 3.10.0 |
| keras      | 2.13.1 |
| keras-rl2  | 1.0.4  |
| numpy      | 1.23.5 |
| Pillow     | 10.0.1 |
| tensorflow | 2.13.0 |


## 0. Breakout
Write a python script train.py that utilizes keras, keras-rl, and gym to train an agent that can play Atari’s Breakout:

- Your script should utilize keras-rl‘s DQNAgent, SequentialMemory, and EpsGreedyQPolicy
- Your script should save the final policy network as policy.h5

Write a python script play.py that can display a game played by the agent trained by train.py:

- Your script should load the policy network saved in policy.h5
- Your agent should use the GreedyQPolicy
