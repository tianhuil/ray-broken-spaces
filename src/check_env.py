from gymnasium.utils.env_checker import check_env

from src.chase_sequence import ChaseSequence
from src.chase_working import ChaseWorking
from src.chase_multi_discrete import ChaseMultiDiscrete

if __name__ == "__main__":
    check_env(ChaseWorking(10))
    check_env(ChaseSequence(10))
    check_env(ChaseMultiDiscrete(10))
