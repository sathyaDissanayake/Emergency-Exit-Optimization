import numpy as np
import pygame
import matplotlib.pyplot as plt

# Example positions for test purposes
movement_data = np.random.randint(20, 700, (2, 5, 5))
objects_pos = np.random.randint(100, 700, (2, 10))


def display_events(movement_data, room, wait_time, radii, sim_size, agents_escaped):
    """Displays the simulation events using the Pygame library.

    Args:
        movement_data (numpy.ndarray): Matrix with shape (x, y, z).
            x=2 are the number coordinates, y is the number of individuals,
            and z is the number of time steps.
        room (Room): Instance of the room. Used to draw the walls.
        wait_time (int): Time that the simulation waits between each time step.
        radii (numpy.ndarray): The radii of the individuals.
        sim_size (int): The size of the image on the screen.
        agents_escaped (numpy.ndarray): Number of agents that have escaped at each time step.
    """
    # Colors
    background_color = (250, 250, 250)  # Grey
    people_color = (250, 0, 0)  # Red
    destination_color = (0, 128, 0)  # Green
    object_color = (0, 0, 0)  # Black

    # Variables for initializing Pygame
    normalizer = int(sim_size / room.get_room_size())  # The ratio (size of image) / (size of actual room)
    map_size = (room.get_room_size() * normalizer + 100, room.get_room_size() * normalizer + 100)
    wait_time = wait_time
    wait_time_after_sim = 3000
    movement_data_dim = movement_data.shape
    num_persons = movement_data_dim[1]
    num_time_iterations = movement_data_dim[2]
    num_walls = room.get_num_walls()

    pygame.init()
    simulate = False
    font = pygame.font.Font(None, 32)
    worldmap = pygame.display.set_mode(map_size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                simulate = True
            elif event.type == pygame.QUIT:
                pygame.quit()
        worldmap.fill(0)
        text = font.render('Press any key to start the simulation', True, (255, 255, 255))
        worldmap.blit(text, (100, 100))
        pygame.display.update()

        if simulate == True:
            for t in range(num_time_iterations):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                worldmap.fill(background_color)

                for person in range(num_persons):
                    pygame.draw.circle(worldmap, people_color,
                                       ((normalizer * movement_data[0, person, t] + 50).astype(int),
                                        (normalizer * movement_data[1, person, t] + 50).astype(int)),
                                       int(normalizer * radii[person]), 0)

                for wall in range(num_walls):
                    pygame.draw.lines(worldmap, object_color, True,
                                      normalizer * room.get_wall(wall) + 50, 2)

                for des in room.get_destination():
                    pygame.draw.circle(worldmap, destination_color,
                                       ((normalizer * des[0] + 50).astype(int),
                                        (normalizer * des[1] + 50).astype(int)),
                                       7, 0)

                strf = "Number of People Escaped: " + str(int(agents_escaped[t]))
                text = font.render(strf, True, (0, 0, 0))
                worldmap.blit(text, (10, 10))

                strd = "Number of People: " + str(num_persons)
                textd = font.render(strd, True, (0, 0, 0))
                worldmap.blit(textd, (400, 10))

                pygame.display.update()
                pygame.time.wait(wait_time)
            simulate = False
            text = font.render('Simulation Completed', True, (0, 0, 0))
            worldmap.blit(text, (100, 100))
            pygame.display.update()
            pygame.time.wait(wait_time_after_sim)



def display_graph(agents_escaped, acceleration, mass):
    """Draws three graphs related to the simulation:
    1. The number of people who escaped the room at each time step.
    2. The number of people who experienced a force higher than "tol" and therefore died.
    3. The forces one random agent experiences.

    Args:
        agents_escaped (numpy.ndarray): Number of people who escaped at each time step.
        acceleration (numpy.ndarray): Acceleration data for each person at each time step.
        mass (numpy.ndarray): Mass of each person.
    """
    tol = 700  # Force at which people die (in Newton)

    _, num_persons, num_steps = np.shape(acceleration)
    forces_new = np.zeros((num_persons, num_steps - 1))
    num_dead = np.zeros(num_steps - 1)

    # Get force by multiplying the acceleration with the mass
    for person in range(num_persons):
        for t in range(num_steps - 1):
            forces_new[person, t] = np.linalg.norm(acceleration[:, person, t]) * mass[person]
            if forces_new[person, t] > tol:
                num_dead[t] += 1

    f = plt.figure(figsize=(10, 10))
    f.subplots_adjust(hspace=0.3)

    f1 = f.add_subplot(3, 1, 1)
    f1.plot(range(len(agents_escaped)), agents_escaped, 'g')
    f1.set_ylabel("Number of Escaped people")
    f1.set_xlabel("Timestep")
    f1.set_title("Escape Scenario")

    f2 = f.add_subplot(3, 1, 2)
    f2.plot(range(num_steps - 1), num_dead, 'r')
    f2.set_ylabel("Number of Dead people")
    f2.set_xlabel("Timestep")

    f3 = f.add_subplot(3, 1, 3)
    chosen_agent = int(num_persons / 2)
    f3.plot(range(num_steps - 1), forces_new[chosen_agent, :], 'b')
    f3.set_ylabel("Forces on Agent")
    f3.set_xlabel("Timestep")

    plt.show()
