# takes an active roll, implements a policy. Must decide an action on every step given some observations
import random


class Agent:
    def __init__(self):
        self.total_reward = 0.

    def step(self, env):
        # observe environment, make a decision, change the environment, get a reward
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward
