from typing import Any
import gymnasium as gym

from src.train import train


class ChaseSequence(gym.Env):
    def __init__(self, grid_size=10):
        super(ChaseSequence, self).__init__()

        self.grid_size = grid_size

        # Define action space (up, down, left, right)
        self.action_space = gym.spaces.Discrete(4)

        # Define observation space (agent's position and ball's position)
        self.observation_space = gym.spaces.Dict(
            {
                "agent_position": gym.spaces.Tuple(
                    (gym.spaces.Discrete(grid_size), gym.spaces.Discrete(grid_size))
                ),
                "ball_position": gym.spaces.Tuple(
                    (gym.spaces.Discrete(grid_size), gym.spaces.Discrete(grid_size))
                ),
                "random": gym.spaces.Sequence(gym.spaces.Discrete(5)),
            }
        )

        # Initialize state
        self.state, _ = self.reset()

    def step(self, action):
        # Execute one time step within the environment
        agent_position = list(self.state["agent_position"])
        ball_position = list(self.state["ball_position"])

        # Update agent's position based on action
        if action == 0:  # up
            agent_position[1] = min(agent_position[1] + 1, self.grid_size - 1)
        elif action == 1:  # down
            agent_position[1] = max(agent_position[1] - 1, 0)
        elif action == 2:  # left
            agent_position[0] = max(agent_position[0] - 1, 0)
        elif action == 3:  # right
            agent_position[0] = min(agent_position[0] + 1, self.grid_size - 1)

        # Update state
        self.state["agent_position"] = tuple(agent_position)

        # Calculate reward and done
        reward = -1  # each step costs -1
        done = agent_position == ball_position  # episode is done when agent reaches the ball

        return self.state, reward, done, False, {}

    def reset(self, seed: int | None = None, options: dict[str, Any] | None = None):
        super().reset(seed=seed, options=options)
        # Reset the state of the environment to an initial state
        initial_state = {
            "agent_position": (0, 0),  # agent starts at the top-left corner
            "ball_position": (
                self.grid_size - 1,
                self.grid_size - 1,
            ),  # ball is at the bottom-right corner
            "random": (3, 4, 4, 3, 2, 2, 3),
        }
        return initial_state, {}

    def render(self, mode="human"):
        # Render the environment to the screen
        grid = [[" " for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        grid[self.state["agent_position"][1]][self.state["agent_position"][0]] = "A"
        grid[self.state["ball_position"][1]][self.state["ball_position"][0]] = "B"
        print("\n".join("".join(row) for row in grid))

if __name__ == '__main__':
    train(ChaseSequence)
