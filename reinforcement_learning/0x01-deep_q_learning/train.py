#!/usr/bin/env python3
"""
training model
"""
import gym
import numpy as np
from PIL import Image

import tensorflow as tf
import tensorflow.keras as K
from keras import __version__
tf.keras.__version__ = __version__

from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from rl.processors import Processor

INPUT_SHAPE = (84, 84)
WINDOW_LENGTH = 4


class AtariProcessor(Processor):
    """
    Atari env for Breakout
    """
    def process_observation(self, observation):
        """
        Resizes and grayscale
        """
        if isinstance(observation, tuple):
            observation = observation[0]
        assert observation.ndim == 3
        img = Image.fromarray(observation)
        img = img.resize(INPUT_SHAPE).convert('L')
        processed_observation = np.array(img)
        assert processed_observation.shape == INPUT_SHAPE
        return processed_observation.astype('uint8')

    def process_state_batch(self, batch):
        """
        Process size of batch
        """
        # We could perform this processing step in `process_observation`.
        # In this case, however, we would need to store a `float32` array
        # instead, which is 4x more memory intensive than an `uint8` array.
        # This matters if we store 1M observations.
        processed_batch = batch.astype('float32') / 255.
        return processed_batch

    def process_reward(self, reward):
        """
        Normalizes reward
        """
        return np.clip(reward, -1., 1.)


def build_model(actions):
    """
    build QNN model
    """
    input_shape = (WINDOW_LENGTH,) + INPUT_SHAPE
    model = K.models.Sequential()
    model.add(K.layers.Permute(
        dims=(2, 3, 1),
        input_shape=input_shape))
    model.add(K.layers.Convolution2D(
        filters=32,
        kernel_size=(8, 8),
        strides=(4, 4),
        activation='relu'))
    model.add(K.layers.Convolution2D(
        filters=64,
        kernel_size=(4, 4),
        strides=(2, 2),
        activation='relu'))
    model.add(K.layers.Convolution2D(
        filters=64,
        kernel_size=(3, 3),
        strides=(1, 1),
        activation='relu'))
    model.add(K.layers.Flatten())
    model.add(K.layers.Dense(256, activation='relu'))
    model.add(K.layers.Dense(actions, activation='linear'))

    return model


def build_agent(model, actions):
    """
    Build Keras RL Agent
    """
    memory = SequentialMemory(
        limit=1000000,
        window_length=WINDOW_LENGTH)
    policy = LinearAnnealedPolicy(
        EpsGreedyQPolicy(),
        attr='eps',
        value_max=1.,
        value_min=.1,
        value_test=.2,
        nb_steps=40000)
    processor = AtariProcessor()

    dqn = DQNAgent(
        model=model,
        nb_actions=actions,
        memory=memory,
        policy=policy,
        processor=processor,
        gamma=0.99,
        train_interval=5,
        nb_steps_warmup=10000,
        target_model_update=1000,
        delta_clip=1.0)

    return dqn


if __name__ == '__main__':
    env = gym.make('Breakout', render_mode='human')
    env.reset()
    window_length = 4
    actions = env.action_space.n

    model = build_model(actions)

    model.summary()

    dqn = build_agent(model, actions)
    dqn.compile(K.optimizers.legacy.Adam(lr=1e-4), metrics=['mae'])
    dqn.fit(env,
            nb_steps=1000000,
            log_interval=10000,
            visualize=False,
            verbose=1)

    dqn.save_weights('policy.h5', overwrite=True)
