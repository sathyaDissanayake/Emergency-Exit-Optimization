import numpy as np
import sys

from agent_interactions import Differential_Equation
from display_model import display_events
from display_model import display_graph
from room_layout import Room
import differential_equation_solver
from differential_equation_solver import leap_frog

class Simulation:
    def __init__(self, num_individuals, num_steps, method="leap_frog", tau=0.1, v_des=1.5, room="square_room_with_1_exit", room_size=25):
        # Initialization of simulation parameters and agent characteristics
        std_deviation = 0.07  # Standard deviation used for generating variation in agent size and weight
        variation = np.random.normal(loc=1, scale=std_deviation, size=(1, num_individuals))

        # Constants
        self.L = room_size  # Size of the simulation room
        self.N = num_individuals  # Number of individuals/agents in the simulation
        self.tau = tau  # Time step for the simulation
        self.num_steps = num_steps  # Number of simulation steps

        # Agent information
        self.radii = 0.4 * (np.ones(self.N) * variation).squeeze()  # Radii of agents
        self.v_des = v_des * np.ones(self.N)  # Desired velocity of agents
        self.m = 80 * (np.ones(self.N) * variation).squeeze()  # Mass of agents
        self.forces = None  # Forces acting on agents during simulation
        self.agents_escaped = None  # Number of agents that have escaped the room
        self.v = np.zeros((2, self.N, self.num_steps))  # Velocities of agents
        self.y = np.zeros((2, self.N, self.num_steps))  # Positions of agents

        self.room = Room(room, room_size)  # Definition of the simulation room
        self.method = getattr(differential_equation_solver, method)  # Method for solving differential equations
        self.diff_equ = Differential_Equation(self.N, self.L, self.tau, self.room, self.radii, self.m)  # Differential equation for agent interactions

    def set_steps(self, steps):
        # Set the number of simulation steps
        self.num_steps = steps

    def set_method(self, method):
        # Set the method for solving differential equations
        self.method = getattr(differential_equation_solver, method)

    def dont_touch(self, i, x):
        # Check if an agent touches another agent
        for j in range(i - 1):
            if np.linalg.norm(x - self.y[:, j, 0]) < 3 * self.radii[i]:
                return True
        return False

    def fill_room(self):
        # Fill the spawn zone with agents having random positions
        spawn = self.room.get_spawn_zone()
        len_right = spawn[0, 1] - spawn[0, 0]
        len_left = spawn[1, 1] - spawn[1, 0]
        max_len = max(len_left, len_right)

        # Check if the area is too small for the agents to fit in
        area_people = 0
        for i in range(self.N):
            area_people += 4 * self.radii[i] ** 2
        if area_people >= 0.7 * max_len ** 2:
            sys.exit('Too many people! Please change the size of the room/spawn-zone or the number of people.')

        # Check if the agent touches another agent/wall and if so, give it a new random position in the spawn-zone
        for i in range(self.N):
            # The pedestrians don't touch the wall
            x = len_right * np.random.rand() + spawn[0, 0]
            y = len_left * np.random.rand() + spawn[1, 0]
            pos = [x, y]

            # The pedestrians don't touch each other
            while self.dont_touch(i, x):
                x = len_right * np.random.rand() + spawn[0, 0]
                y = len_left * np.random.rand() + spawn[1, 0]
                pos = [x, y]
            self.y[:, i, 0] = pos

        self.v[:, :, 0] = self.v_des * self.diff_equ.e_t(self.y[:, :, 0])

    def run(self):
        # Run the simulation by calling the method of integration with the starting positions, differential equation,
        # number of steps, and delta t = tau
        self.y, self.agents_escaped, self.forces = self.method(self.y[:, :, 0], self.v[:, :, 0], self.diff_equ.f,
                                                               self.num_steps, self.tau, self.room)

    def show(self, wait_time, sim_size):
        # Display the simulation in pygame
        display_graph(self.agents_escaped, self.forces, self.m)
        display_events(self.y, self.room, wait_time, self.radii, sim_size, self.agents_escaped)
