#!/usr/bin/env python3
"""
module containing function sarsa_lambtha
"""
import numpy as np


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1,
                  epsilon_decay=0.05):
    """
    function that performs the SARSA(λ) algorithm
    Args:
        env: openAI environment instance
        Q: numpy.ndarray of shape (s, a) containing the Q table
        lambtha: eligibility trace factor
        episodes: total number of episodes to train over
        max_steps: maximum number of steps per episode
        alpha: learning rate
        gamma: discount rate
        epsilon: initial threshold for epsilon greedy
        min_epsilon: minimum value that epsilon should decay to
        epsilon_decay: decay rate for updating epsilon between episodes
    Return: Q, the updated Q table
    """
    states, actions = Q.shape
    max_epsilon = epsilon

    def epsilon_greedy(epsilon, Qs):
        # Epsilon-greedy policy to choose actions
        p = np.random.uniform()
        if p > epsilon:
            return np.argmax(Qs)
        else:
            return np.random.randint(0, actions)

    for ep in range(episodes):
        eligibility = np.zeros(shape=(states, actions))
        s_prev = env.reset()
        # Choose the initial action using epsilon-greedy
        action_prev = epsilon_greedy(epsilon, Q[s_prev])

        for step in range(max_steps):
            s, reward, done, info = env.step(action_prev)
            # Choose the next action using epsilon-greedy
            action = epsilon_greedy(epsilon, Q[s])
            # Calculate the temporal difference error
            delta = reward + (gamma * Q[s, action]) - Q[s_prev, action_prev]
            # Update the eligibility trace
            eligibility[s_prev, action_prev] += 1
            # Decay the eligibility trace
            eligibility = eligibility * gamma * lambtha
            # Update the Q-values using the SARSA(λ) update rule
            Q = Q + (alpha * delta * eligibility)

            if done:
                break

            s_prev = s
            action_prev = action

        # Decay epsilon for exploration-exploitation trade-off
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(
            -epsilon_decay * ep)

    return Q
