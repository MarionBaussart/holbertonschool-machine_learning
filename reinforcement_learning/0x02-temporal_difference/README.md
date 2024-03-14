# Temporal Difference
- What is Monte Carlo?

Monte Carlo methods are applied to evaluate and optimize policies in episodic environments.
- What is Temporal Difference?

A learning method that updates its value estimates by considering the difference between the current estimate and the estimate at a subsequent time step.
- What is bootstrapping?

N-step bootstrapping is a concept commonly used in the context of Temporal Difference (TD) learning methods. It extends the idea of TD learning, which uses a one-step look-ahead, to a multi-step look-ahead to estimate values or Q-values.
- What is n-step temporal difference?

Monte Carlo executes entire traces and then backpropagate the reward. Basic TD look at the reward in the next step, estimating the future rewards. N-step methods instead look steps ahead for the reward before updating the reward, and then estimate the remainder.
- What is TD(λ)?

The problem with n-step TD is that picking “n” could be challenging and won’t generalize to different environments. TD(λ): Temporal Difference Lambda combine elements of both Monte Carlo methods and Temporal Difference (TD) methods. The lambda (λ) parameter refers to the trace decay parameter, with 0⩽λ⩽1.
TD(λ) is one particular way of averaging n-step updates. This average contains all the n-step updates, each weighted proportional to λ^(n-1).
- What is an eligibility trace?

Eligibility Traces (λ) are used to keep track of which states and actions have been visited by the agent over multiple time steps. These traces allow the algorithm to attribute credit for rewards and outcomes to actions and states encountered earlier in a sequence of interactions.
- What is SARSA? SARSA(λ)? SARSAMAX?

SARSA(λ) is an extension of the SARSA algorithm : a non-policy reinforcement learning algorithm used for estimating action values. SARSA(λ) incorporates eligibility traces(λ) to improve credit assignment within the context of SARSA. It helps the agent learn the value of state-action pairs under a particular policy while considering an extended history of state-action sequences. SARSA(λ) is primarily used for policy evaluation (estimating value functions).
The λ parameter in SARSA(λ) determines the extent to which eligibility traces are used. A value of λ closer to 1 gives more weight to earlier actions and states, while a value closer to 0 emphasizes more recent actions and states. Tuning this parameter allows the agent to find a balance between short-term and long-term credit assignment.
- What is ‘on-policy’ vs ‘off-policy’?

On-policy methods evaluate and improve the same policy used for data collection, while off-policy methods allow for the evaluation of one policy using data collected from another.

## 0. Monte Carlo
Write the function ``def monte_carlo(env, V, policy, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):`` that performs the Monte Carlo algorithm:

- ``env`` is the openAI environment instance
- ``V`` is a ``numpy.ndarray`` of shape ``(s,)`` containing the value estimate
- ``policy`` is a function that takes in a state and returns the next action to take
- ``episodes`` is the total number of episodes to train over
- ``max_step``s is the maximum number of steps per episode
- ``alpha`` is the learning rate
- ``gamma`` is the discount rate
- Returns: ``V``, the updated value estimate

## 1. TD(λ)
Write the function ``def td_lambtha(env, V, policy, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99):`` that performs the TD(λ) algorithm:

- ``env`` is the openAI environment instance
- ``V`` is a ``numpy.ndarray`` of shape ``(s,)`` containing the value estimate
- ``policy`` is a function that takes in a state and returns the next action to take
- ``lambtha`` is the eligibility trace factor
- ``episodes`` is the total number of episodes to train over
- ``max_steps`` is the maximum number of steps per episode
- ``alpha`` is the learning rate
- ``gamma`` is the discount rate
- Returns: ``V``, the updated value estimate

## 2. SARSA(λ)
Write the function ``def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100, alpha=0.1, gamma=0.99, epsilon=1, min_epsilon=0.1, epsilon_decay=0.05):`` that performs SARSA(λ):

- ``env`` is the openAI environment instance
- ``Q`` is a ``numpy.ndarray`` of shape ``(s,a)`` containing the Q table
- ``lambtha`` is the eligibility trace factor
- ``episodes`` is the total number of episodes to train over
- ``max_steps`` is the maximum number of steps per episode
- ``alpha`` is the learning rate
- ``gamma`` is the discount rate
- ``epsilon`` is the initial threshold for epsilon greedy
- ``min_epsilon`` is the minimum value that epsilon should decay to
- ``epsilon_decay`` is the decay rate for updating epsilon between episodes
- Returns: ``Q``, the updated Q table

# Versions
Python 3.9

numpy 1.23.5

gym 0.25.2
