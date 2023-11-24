# Import the Simulation class from the model_simulation module
from model_simulation import Simulation

# Create a simulation instance with the following parameters:
# - number of individuals (agents)
# - number of simulation steps
# - Leap frog method for integration
# - Room size
# - Room layout
simulation = Simulation(num_individuals=30, num_steps=1000, method="leap_frog"
                        , velocity_factor=1.25, room_size=25
                        , room="square_room_with_1_exit_1_additional_wall")

# Fill the simulation room's spawn zone with random individuals
simulation.fill_room()

# Run the simulation to calculate the agent trajectories, forces, and escape events
simulation.run()

# Display the simulation using Pygame with the following settings:
# - Wait for n milliseconds between each time step
# - Set the size of the simulation display to m pixels
simulation.show(wait_time=10, sim_size=600)
