#!/usr/bin/env python3
"""
playing Atari Breakout
"""
import gym
import tensorflow.keras as K

build_model = __import__('train').build_model
build_agent = __import__('train').build_agent

INPUT_SHAPE = (84, 84)
WINDOW_LENGTH = 4


if __name__ == '__main__':
    env = gym.make('Breakout-v4', render_mode='human')
    observation, info = env.reset()
    actions = env.action_space.n

    model = build_model(actions)

    dqn = build_agent(model, actions)
    dqn.compile(K.optimizers.Adam(lr=1e-4), metrics=['mae'])

    dqn.load_weights('policy.h5')

    dqn.test(env, nb_episodes=10, visualize=False)
