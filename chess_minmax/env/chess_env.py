import gym
import gym_chess
import chess

def create_env():
    env = gym.make("Chess-v0")
    return env
