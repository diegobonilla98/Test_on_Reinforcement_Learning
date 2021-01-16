from Agent import Agent
from Environment import Environment

env = Environment()
agent = Agent()

while not env.is_done():
    agent.step(env)

print(f"Total reward got: {agent.total_reward}")

