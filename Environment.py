# model of the world. Gives observations and rewards. Changes state based on actions.
import random


class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self):
        # current observation to the agent
        return [0., 0., 0.]

    def get_actions(self):
        # get the actions the agent can execute
        return [0, 1]

    def is_done(self):
        # episode is over
        return self.steps_left == 0

    def action(self, action):
        # handles the actions and returns the rewards
        if self.is_done():
            raise Exception("Game is Over")
        self.steps_left -= 1
        return random.random()
