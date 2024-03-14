#!/usr/bin/env python3
"""
module containing function td_lambtha
"""
import numpy as np


def td_lambtha(env, V, policy, lambtha, episodes=5000,
               max_steps=100, alpha=0.1, gamma=0.99):
    """
    function that performs the TD(λ) algorithm
    Args:
        env: openAI environment instance
        V: numpy.ndarray of shape (s,) containing the value estimate
        policy: function that takes in a state
            and returns the next action to take
        lambtha: eligibility trace factor
        episodes: total number of episodes to train over
        max_steps: maximum number of steps per episode
        alpha: learning rate
        gamma: discount rate
    Return: V, the updated value estimate
    """
    for ep in range(episodes):
        state = env.reset()
        done = False
        eligibility = np.zeros(shape=V.shape[0])

        for step in range(max_steps):
            action = policy(state)
            new_state, reward, done, info = env.step(action)

            # TD error for bootstrapping
            delta = reward + (gamma * V[new_state]) - V[state]

            eligibility *= gamma * lambtha
            eligibility[state] += 1

            V = V + alpha * delta * eligibility

            if done:
                break

            state = new_state

    return V
