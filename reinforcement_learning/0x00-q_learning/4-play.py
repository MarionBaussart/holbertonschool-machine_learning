#!/usr/bin/env python3
"""
module containing function play
"""
import numpy as np


def play(env, Q, max_steps=100):
    """
    function that has the trained agent play an episode
    Args:
        env: FrozenLakeEnv instance
        Q: numpy.ndarray containing the Q-table
        max_steps: maximum number of steps in the episode
    Return: the total rewards for the episode
    """
    state = env.reset()
    done = False
    env.render()

    for step in range(max_steps):
        action = np.argmax(Q[state, :])
        new_state, reward, done, info = env.step(action)
        env.render()

        if done:
            return reward

        state = new_state

    env.close()
    return reward
