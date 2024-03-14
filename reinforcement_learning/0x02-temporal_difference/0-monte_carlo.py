#!/usr/bin/env python3
"""
module containing function monte_carlo
"""
import numpy as np


def monte_carlo(env, V, policy, episodes=5000,
                max_steps=100, alpha=0.1, gamma=0.99):
    """
    function that performs the Monte Carlo algorithm
    Args:
        env: openAI environment instance
        V: numpy.ndarray of shape (s,) containing the value estimate
        policy: function that takes in a state
            and returns the next action to take
        episodes: total number of episodes to train over
        max_steps: maximum number of steps per episode
        alpha: learning rate
        gamma: discount rate
    Return: V, the updated value estimate
    """
    for ep in range(episodes):
        state = env.reset()
        episode = []
        done = False
        G = 0

        for step in range(max_steps):
            action = policy(state)
            new_state, reward, done, info = env.step(action)
            episode.append([state, reward])

            if done:
                break

            state = new_state

        episode = np.array(episode, dtype=int)

        for s in reversed(range(len(episode))):
            state, reward = episode[s]
            G = gamma * G + reward
            # first visit
            if state not in episode[:ep, 0]:
                V[state] = V[state] + alpha * (G - V[state])

    return V
