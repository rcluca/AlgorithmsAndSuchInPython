

"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import math
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        visited = self._cells #[[0 for dummy_col in self._cells[0]]for dummy_row in self._cells[1]]
        distance_field = [[self._grid_width * self._grid_height for dummy_col in range(self._grid_width)]for dummy_row in range(self._grid_height)]

        boundary = poc_queue.Queue()
        if entity_type == HUMAN:
            for each in self._human_list:
                boundary.enqueue(each)
        elif entity_type == ZOMBIE:
            for each in self._zombie_list:
                boundary.enqueue(each)

        if boundary.__len__() > 0:
            for each in boundary:
                visited[each[0]][each[1]] = FULL
                distance_field[each[0]][each[1]] = 0

        while boundary.__len__() > 0:
            current_cell = boundary.dequeue()
            neighbors = self.four_neighbors(current_cell[0], current_cell[1])
            for neighbor_cell in neighbors:
                if self.is_empty(neighbor_cell[0], neighbor_cell[1]):
                    self.set_full(neighbor_cell[0], neighbor_cell[1])
                    boundary.enqueue(neighbor_cell)
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = min(distance_field[neighbor_cell[0]][neighbor_cell[1]], distance_field[current_cell[0]][current_cell[1]] + 1)

        return distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """

        temp_human_list = []

        for human in self._human_list:
            moveto_cell_value = 0
            temp_list = ()
            neighbors = self.eight_neighbors(human[0], human[1])
            for neighbor_cell in neighbors:
                if zombie_distance[neighbor_cell[0]][neighbor_cell[1]] > moveto_cell_value:
                    moveto_cell_value = zombie_distance[neighbor_cell[0]][neighbor_cell[1]]
                    temp_list = neighbor_cell
            temp_human_list.append(temp_list)

        self._human_list = temp_human_list

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        temp_zombie_list = []

        for zombie in self._zombie_list:
            if zombie not in self._human_list:
                moveto_cell_value = self._grid_height * self._grid_width
                temp_list = ()
                neighbors = self.four_neighbors(zombie[0], zombie[1])
                for neighbor_cell in neighbors:
                    if human_distance[neighbor_cell[0]][neighbor_cell[1]] < moveto_cell_value:
                        moveto_cell_value = human_distance[neighbor_cell[0]][neighbor_cell[1]]
                        temp_list = neighbor_cell
                temp_zombie_list.append(temp_list)
            else:
                temp_zombie_list.append(zombie)

        self._zombie_list = temp_zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Zombie(30, 40))
