import numpy as np


# Define a function named leap_frog that simulates the motion of agents in a room_type.
# The function takes the following parameters:
# - init_position: Initial positions of the agents (a NumPy array).
# - init_velocity: Initial velocities of the agents (a NumPy array).
# - f: A function that represents the forces acting on the agents.
# - number_of_steps: Number of simulation steps to perform.
# - dt: Time step size for the simulation.
# - room_type: An object representing the room_type and agent destinations.

def leap_frog(init_position, init_velocity, f, number_of_steps, dt, room_type):
    escaped_counter = 0  # Initialize a variable to keep track of the number of escaped agents.

    # Create an array to store the number of agents that have escaped at each time step.
    agents_escaped = np.zeros(number_of_steps)

    # Create arrays to store the positions (y), velocities (v), and accelerations (a) of the agents at each time step.
    y = np.zeros((init_position.shape[0], init_position.shape[1], number_of_steps))
    v = np.zeros((init_position.shape[0], init_position.shape[1], number_of_steps))
    a = np.zeros((init_position.shape[0], init_position.shape[1], number_of_steps))

    # Initialize the initial positions and velocities at the first time step.
    y[:, :, 0] = init_position
    v[:, :, 0] += 0.5 * dt * f(y[:, :, 0], v[:, :, 0])

    # Iterate through time steps from 0 to number_of_steps - 2.
    for k in range(number_of_steps - 1):
        # Update agent positions using the leap-frog integration scheme.
        y[:, :, k + 1] = y[:, :, k] + dt * v[:, :, k]

        # Calculate accelerations at the current time step.
        a[:, :, k] = f(y[:, :, k], v[:, :, k])

        # Update agent velocities using the leap-frog integration scheme.
        v[:, :, k + 1] = v[:, :, k] + dt * f(y[:, :, k + 1], v[:, :, k] + dt * a[:, :, k])

        # Check if any agent has reached its destination in the room_type.
        for i in range(y.shape[1]):
            destination = np.zeros(len(room_type.get_destination()))
            for count, des in enumerate(room_type.get_destination()):
                # Calculate the distance of each agent to the destinations.
                destination[count] = np.linalg.norm(y[:, i, k + 1] - des)
            # Find the minimum distance to determine if an agent has reached its destination.
            distance = np.amin(destination)

            # If the distance is less than 0.1, consider the agent to have reached its destination.
            if distance < 0.1:
                # Randomly reposition the agent far from the destinations.
                y[:, i, k + 1] = 10 ** 6 * np.random.rand(2)
                escaped_counter += 1  # Increment the count of escaped agents.

        # Store the count of escaped agents at the current time step.
        agents_escaped[k + 1] = escaped_counter

    # Return the updated positions, the count of escaped agents at each time step, and the accelerations.
    return y, agents_escaped, a
