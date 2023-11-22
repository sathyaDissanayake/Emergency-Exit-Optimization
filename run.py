# Import the Simulation class from the model_simulation module
from model_simulation import Simulation

# Create a simulation instance with the following parameters:
# - number of individuals (agents)
# - number of simulation steps
# - Leap frog method for integration
# - Room size
# - Room layout
sim = Simulation(num_individuals=50, num_steps=1000, method="leap_frog", room_size=25, room="square_room_with_1_exit")

# Fill the simulation room's spawn zone with random individuals
sim.fill_room()

# Run the simulation to calculate the agent trajectories, forces, and escape events
sim.run()

# Display the simulation using Pygame with the following settings:
# - Wait for n milliseconds between each time step
# - Set the size of the simulation display to m pixels
sim.show(wait_time=10, sim_size=600)
