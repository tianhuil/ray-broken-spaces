import ray
from ray import tune
import gymnasium as gym

ENV_NAME = "ChaseEnv-v0"

def train(Env: gym.Env):
    ray.init()

    def create_env(env_config):
        return Env(**env_config)

    tune.register_env(ENV_NAME, create_env)

    config = {
        "env": ENV_NAME,
        "num_gpus": 0,
        "num_workers": 1,
        "env_config": {"grid_size": 15},
    }

    stop = {
        "training_iteration": 200,
        "timesteps_total": 10000,
    }

    tune.run(
        "APPO",
        config=config,
        stop=stop,
        max_failures=0,
    )

    ray.shutdown()
