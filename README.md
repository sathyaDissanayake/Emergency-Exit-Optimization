# Agent-Based Implementation for Optimizing Emergency Exit to Identify Bottlenecks

## Introduction
The simulation of the model focuses on the emergency exiting scenario in diverse room configurations that are densely populated with individuals. Additionally, the model helps to study the impact of introducing the barriers within the environment.

This repository contains the source code, documentation, and other resources related to the project.

## Features
**room_layout.py:** Implements a "Room" class using Numpy to simulate varied room structures, allowing customization for different evacuation scenarios.

**differential_equation_solver.py:** Features a "leap_frog" function for simulating agent escape dynamics, tracking positions, velocities, and accelerations, with key parameters influencing evacuation effectiveness.

**agent_interactions.py:** Defines a "Differential_Equation" class modeling agent dynamics, calculating accelerations based on forces between agents and walls.

**display_model.py:** Utilizes Pygame to visualize simulation events and graphs, with functions displaying individual movements, walls, destinations, and key graphs.

**model_simulation.py:** Introduces a "Simulation" class to simulate agent movements and interactions, customizable for various experiments by adjusting parameters.

**run.py:** Sets up and runs a simulation of agents in a confined environment, utilizing the leapfrog method and Pygame for visualization, with customizable parameters for different scenarios.

## Getting Started
Follow below instructions to get a copy of the project and run it on a local machine.

### Prerequisites
Below are required to run the project
- Python 3.6
- Python libraries
  - numpy
  - pygame
  - matplotlib

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/sathyaDissanayake/Emergency-Exit-Optimization.git

2. Install python libraries listed in the requirements.txt

3. Execute 'run.py' to run the program