#!/usr/bin/env python3
"""
module containing function train
"""
import numpy as np
epsilon_greedy = __import__('2-epsilon_greedy').epsilon_greedy


def train(env, Q, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99,
          epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):
    """
    function that performs Q-learning
    Args:
        env: FrozenLakeEnv instance
        Q: numpy.ndarray containing the Q-table
        episodes: total number of episodes to train over
        max_steps: maximum number of steps per episode
        alpha: learning rate
        gamma: discount rate
        epsilon: initial threshold for epsilon greedy
        min_epsilon: minimum value that epsilon should decay to
        epsilon_decay: decay rate for updating epsilon between episodes
    Return: Q, total_rewards
        Q: updated Q-table
        total_rewards: list containing the rewards per episode
    """
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        episode_rewards = 0

        for step in range(max_steps):
            action = epsilon_greedy(Q, state, epsilon)
            new_state, reward, done, _ = env.step(action)

            if done and reward == 0:
                reward = -1

            Q[state, action] = (1 - alpha) * Q[state, action] + alpha * \
                (reward + gamma * np.max(Q[new_state, :]))

            state = new_state
            episode_rewards += reward

            if done:
                break

        epsilon = min_epsilon + (1 - min_epsilon) * \
            np.exp(-epsilon_decay * episode)

        total_rewards.append(episode_rewards)

    return Q, total_rewards
