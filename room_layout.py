# Import the NumPy library to work with numerical operations and arrays
import numpy as np

# Define a class named Room that represents different room configurations
class Room:
    def __init__(self, room, room_size):
        # Initialize the Room object with a given room type and room size

        self.room_size = room_size  # Store the room size

        if room == "square_room_with_1_exit":
            # Configuration for a square room with a single exit
            self.wall_shear = False  # No walls in this configuration
            self.door_size = room_size / 10  # Width of the exit
            self.destination = np.array([[-0.5, room_size / 2]])  # Position of the destination
            self.number_of_walls = 5  # Number of walls in the room.
            self.walls = np.array([[[0, 0], [0, room_size / 2 - self.door_size / 2]],  # Wall coordinates
                                  [[0, room_size / 2 + self.door_size / 2], [0, room_size]],  
                                  [[0, room_size], [room_size, room_size]],             
                                  [[room_size, room_size], [room_size, 0]],             
                                  [[room_size, 0], [0, 0]]])                 
                                  
            self.spawn_zone = np.array([[room_size / 2, room_size - 1], [1, room_size - 1]])  # Agent spawn zone

        if room == "square_room_with_1_exit_1_additional_wall":
            # Configuration for a square room with one exit and an additional wall
            self.wall_shear = True  # Walls are present in this configuration
            self.door_size = room_size / 15  # Width of the exit
            self.destination = np.array([[-0.5, room_size / 2]])  # Position of the destination
            self.number_of_walls = 6  # Number of walls in the room
            self.walls = np.array([[[0, 0], [0, room_size / 2 - self.door_size / 2]],  # Wall coordinates
                                  [[0, room_size / 2 + self.door_size / 2], [0, room_size]],  
                                  [[0, room_size], [room_size, room_size]],             
                                  [[room_size, room_size], [room_size, 0]],             
                                  [[room_size, 0], [0, 0]],                             
                                  [[room_size / 4, room_size * 0.3], [room_size / 4, room_size * 0.7]]])  # Wall coordinates
                                  
            self.spawn_zone = np.array([[room_size / 2, room_size - 1], [1, room_size - 1]])  # Agent spawn zone

        if room == "square_room_with_2_exits":
            # Configuration for a square room with a single exit
            self.wall_shear = False  # No walls in this configuration
            self.door_size = room_size / 15  # Width of the exit
            self.destination = np.array([[-0.5, self.room_size / 2], [self.room_size + 0.5, self.room_size / 2]])  # Positions of the destinations
            self.number_of_walls = 6  # Number of walls in the room
            self.walls = np.array([[[0, 0], [0, self.room_size / 2 - self.door_size / 2]],  # Wall coordinates
                                   [[0, self.room_size / 2 + self.door_size / 2], [0, self.room_size]],
                                   [[0, self.room_size], [self.room_size, self.room_size]],
                                   [[self.room_size, self.room_size],
                                    [self.room_size, self.room_size / 2 + self.door_size / 2]],
                                   [[self.room_size, self.room_size / 2 - self.door_size / 2],
                                    [self.room_size, 0]],
                                   [[self.room_size, 0], [0, 0]]])

            self.spawn_zone = np.array([[1, room_size - 1], [1, room_size - 1]])  # Agent spawn zone

        if room == "square_room_with_2_exits_1_additional_wall_1":
            # Configuration for a square room with one exit and an additional wall
            self.wall_shear = True  # Walls are present in this configuration
            self.door_size = room_size / 15  # Width of the exit
            self.destination = np.array([[-0.5, room_size / 2]])  # Position of the destination
            #self.destination = np.array([[room_size + 0.5, room_size / 2], [-0.5, room_size / 2]])
            self.number_of_walls = 7  # Number of walls in the room
            self.walls = np.array([[[0, 0], [0, self.room_size / 2 - self.door_size / 2]],  # Wall coordinates
                                   [[0, self.room_size / 2 + self.door_size / 2], [0, self.room_size]],
                                   [[0, self.room_size], [self.room_size, self.room_size]],
                                   [[self.room_size, self.room_size], [self.room_size, self.room_size / 2 + self.door_size / 2]],
                                   [[self.room_size, self.room_size / 2 - self.door_size / 2], [self.room_size, 0]],
                                   [[self.room_size, 0], [0, 0]],
                                   [[self.room_size / 4, self.room_size * 0.3], [self.room_size / 4, self.room_size * 0.7]]])

            self.spawn_zone = np.array([[room_size / 2, room_size - 1], [1, room_size - 1]])   # Agent spawn zone

        if room == "square_room_with_2_exits_1_additional_wall_2":
            # Configuration for a square room with one exit and an additional wall
            self.wall_shear = True  # Walls are present in this configuration
            self.door_size = room_size / 15  # Width of the exit
            #self.destination = np.array([[-0.5, room_size / 2]])  # Position of the destination
            #self.destination = np.array([[room_size + 0.5, room_size / 2]])
            self.destination = np.array([[-0.5, self.room_size / 2], [self.room_size + 0.5, self.room_size / 2]])
            self.number_of_walls = 7  # Number of walls in the room
            self.walls = np.array([[[0, 0], [0, self.room_size / 2 - self.door_size / 2]],  # Wall coordinates
                                   [[0, self.room_size / 2 + self.door_size / 2], [0, self.room_size]],
                                   [[0, self.room_size], [self.room_size, self.room_size]],
                                   [[self.room_size, self.room_size], [self.room_size, self.room_size / 2 + self.door_size / 2]],
                                   [[self.room_size, self.room_size / 2 - self.door_size / 2], [self.room_size, 0]],
                                   [[self.room_size, 0], [0, 0]],
                                   [[self.room_size / 4, self.room_size * 0.3], [self.room_size / 4, self.room_size * 0.7]]])

            self.spawn_zone = np.array([[room_size / 2, room_size - 1], [1, room_size - 1]])   # Agent spawn zone

    def get_wall(self, n):
        # Get the coordinates of the nth wall
        return self.walls[n, :, :]

    def get_num_walls(self):
        # Get the total number of walls in the room
        return self.number_of_walls

    def get_spawn_zone(self):
        # Get the coordinates of the agent spawn zone
        return self.spawn_zone

    def get_room_size(self):
        # Get the size of the room
        return self.room_size

    def get_destination(self):
        # Get the positions of the destination(s) in the room
        return self.destination
