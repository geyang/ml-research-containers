def gym_render():
    import gym
    from ml_logger import logger

    env = gym.make("Reacher-v2")
    logger.print("gym Reacher-v2 is working!", color="green")
    img = env.render('rgb_array')
    logger.print(f"Reacher-v2 renders <{img.shape}>", color="green")


def gym_dmc_render():
    import gym
    from ml_logger import logger

    env = gym.make("dmc:Cartpole-balance-v1")
    logger.print(f"dmc Cartpole starts!", color="green")
    img = env.render('rgb_array')
    logger.print(f"dmc:Cartpole renders <{img.shape}>", color="green")


if __name__ == '__main__':
    print('Testing imports')
    import os

    print(">>>> working directory:", os.getcwd())

    import numpy as np
    import torch
    import torchvision
    import jax
    import jax.numpy as jnp
    import flax

    import gym
    import d4rl
    import mujoco_py
    import dm_control

    import ml_logger, jaynes, params_proto

    gym_dmc_render()
    gym_render()

    print('Done')
