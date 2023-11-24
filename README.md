# Agent-Based Implementation for Optimizing Emergency Exit to Identify Bottlenecks

## Introduction
The simulation of the model focuses on the emergency exiting scenario in diverse room configurations that are densely populated with individuals. Additionally, the model helps to study the impact of introducing the barriers within the environment.

This repository contains the source code, documentation, and other resources related to the project.

## Features
**room_layout.py:**
The script defines a "Room" class for simulating diverse room structures, incorporating features like door size, wall shear, destination, agent spawn area, and the number of walls. Numerical operations from "Numpy" are utilized to design various room types, allowing easy customization for different evacuation scenarios.

**differential_equation_solver.py:**
The code features a "leap_frog" function for simulating agent escape dynamics within a room, tracking positions, velocities, and accelerations over multiple simulation steps. It monitors the number of escaped agents at each time step, offering insights into evacuation effectiveness and bottleneck influences. Key parameters include initial positions, velocities, force functions, time step size, and room characteristics.

**agent_interactions.py:**
The "Differential_Equation" class models agent movement dynamics, including interactions with walls and other agents, calculating accelerations based on various forces. Key parameters encompass the number of individuals, room size, time steps, and physical characteristics of agents such as weight, velocity, and radius. The class defines methods for force calculations between agents and walls, governing the overall dynamics.

**display-model.py:**
The script includes functions "display_events" and "display_graphs" using Pygame for visualizing simulation events and graphs. The former simulates events, drawing individuals, walls, destinations, and escape information. The latter displays graphs illustrating the number of people escaped over time, those experiencing high forces, and forces on a random agent over time.

**model_simulation.py:**
The "Simulation" class in the code simulates agent movements and interactions in an evacuation environment, considering parameters like the number of individuals, simulation steps, integration method, time step, velocity factor, room layout, and size. It enables customization for various experiments by adjusting these parameters.

**run.py:**
The code orchestrates and executes a simulation of agents in a confined environment using the leapfrog integration method, visualizing results with Pygame. Users can customize parameters such as the number of agents, simulation steps, and room layout to adapt the simulation for different scenarios.

## Getting Started
Follow below instructions to get a copy of the project and run it on a local machine.

### Prerequisites
List the software and tools required to run the project
- Python 3.6
- Python libraries
  - numpy
  - pygame
  - matplotlib

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/your-username/Emergency-Exit-Optimization.git

2. Install python libraries listed in the requirements.txt

3. Execute 'run.py' to run the program