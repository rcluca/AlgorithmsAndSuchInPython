"""
Function to generate permutations of outcomes
Repetition of outcomes not allowed
"""

def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item in new_seq:
                    pass
                #if len(new_seq) == 2:
                    #if tuple([new_seq[1],new_seq[0]]) in temp:
                    #if new_seq[0] == new_seq[1]:
                    #    pass
                    #else:
                    #    temp.add(tuple(new_seq))
                else:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))

        ans = temp
    return ans



def run_example():


    outcome = set(["a", "b", "c", "d", "e", "f"])

    permutations = gen_permutations(outcome, 4)
    permutation_list = list(permutations)
    permutation_list.sort()
    print
    print "Answer is", permutation_list[100]


run_example()
print 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1

#my_set = ([(7, 3), (6, 9), (0, 7)])
#my_list = [7, 3]
#my_newlist = [my_list[1], my_list[0]]
#print len(my_list)
#print tuple(my_newlist) in my_set
#print my_set.__contains__(tuple(my_list))


#######################################
# Example output below
#
#Computed 90 permutations of length 2
#Permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])#
#
#Computed 6 permutations of length 2
#Permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green')])
#
#Computed 210 permutations of length 3
#Permutations were set([('Sunday', 'Monday', 'Tuesday'), ('Sunday', 'Monday', 'Wednesday'), ('Sunday', 'Monday', 'Thursday'), ('Sunday', 'Monday', 'Friday'), ('Sunday', 'Monday', 'Saturday'), ('Sunday', 'Tuesday', 'Monday'), ('Sunday', 'Tuesday', 'Wednesday'), ('Sunday', 'Tuesday', 'Thursday'), ('Sunday', 'Tuesday', 'Friday'), ('Sunday', 'Tuesday', 'Saturday'), ('Sunday', 'Wednesday', 'Monday'), ('Sunday', 'Wednesday', 'Tuesday'), ('Sunday', 'Wednesday', 'Thursday'), ('Sunday', 'Wednesday', 'Friday'), ('Sunday', 'Wednesday', 'Saturday'), ('Sunday', 'Thursday', 'Monday'), ('Sunday', 'Thursday', 'Tuesday'), ('Sunday', 'Thursday', 'Wednesday'), ('Sunday', 'Thursday', 'Friday'), ('Sunday', 'Thursday', 'Saturday'), ('Sunday', 'Friday', 'Monday'), ('Sunday', 'Friday', 'Tuesday'), ('Sunday', 'Friday', 'Wednesday'), ('Sunday', 'Friday', 'Thursday'), ('Sunday', 'Friday', 'Saturday'), ('Sunday', 'Saturday', 'Monday'), ('Sunday', 'Saturday', 'Tuesday'), ('Sunday', 'Saturday', 'Wednesday'), ('Sunday', 'Saturday', 'Thursday'), ('Sunday', 'Saturday', 'Friday'), ('Monday', 'Sunday', 'Tuesday'), ('Monday', 'Sunday', 'Wednesday'), ('Monday', 'Sunday', 'Thursday'), ('Monday', 'Sunday', 'Friday'), ('Monday', 'Sunday', 'Saturday'), ('Monday', 'Tuesday', 'Sunday'), ('Monday', 'Tuesday', 'Wednesday'), ('Monday', 'Tuesday', 'Thursday'), ('Monday', 'Tuesday', 'Friday'), ('Monday', 'Tuesday', 'Saturday'), ('Monday', 'Wednesday', 'Sunday'), ('Monday', 'Wednesday', 'Tuesday'), ('Monday', 'Wednesday', 'Thursday'), ('Monday', 'Wednesday', 'Friday'), ('Monday', 'Wednesday', 'Saturday'), ('Monday', 'Thursday', 'Sunday'), ('Monday', 'Thursday', 'Tuesday'), ('Monday', 'Thursday', 'Wednesday'), ('Monday', 'Thursday', 'Friday'), ('Monday', 'Thursday', 'Saturday'), ('Monday', 'Friday', 'Sunday'), ('Monday', 'Friday', 'Tuesday'), ('Monday', 'Friday', 'Wednesday'), ('Monday', 'Friday', 'Thursday'), ('Monday', 'Friday', 'Saturday'), ('Monday', 'Saturday', 'Sunday'), ('Monday', 'Saturday', 'Tuesday'), ('Monday', 'Saturday', 'Wednesday'), ('Monday', 'Saturday', 'Thursday'), ('Monday', 'Saturday', 'Friday'), ('Tuesday', 'Sunday', 'Monday'), ('Tuesday', 'Sunday', 'Wednesday'), ('Tuesday', 'Sunday', 'Thursday'), ('Tuesday', 'Sunday', 'Friday'), ('Tuesday', 'Sunday', 'Saturday'), ('Tuesday', 'Monday', 'Sunday'), ('Tuesday', 'Monday', 'Wednesday'), ('Tuesday', 'Monday', 'Thursday'), ('Tuesday', 'Monday', 'Friday'), ('Tuesday', 'Monday', 'Saturday'), ('Tuesday', 'Wednesday', 'Sunday'), ('Tuesday', 'Wednesday', 'Monday'), ('Tuesday', 'Wednesday', 'Thursday'), ('Tuesday', 'Wednesday', 'Friday'), ('Tuesday', 'Wednesday', 'Saturday'), ('Tuesday', 'Thursday', 'Sunday'), ('Tuesday', 'Thursday', 'Monday'), ('Tuesday', 'Thursday', 'Wednesday'), ('Tuesday', 'Thursday', 'Friday'), ('Tuesday', 'Thursday', 'Saturday'), ('Tuesday', 'Friday', 'Sunday'), ('Tuesday', 'Friday', 'Monday'), ('Tuesday', 'Friday', 'Wednesday'), ('Tuesday', 'Friday', 'Thursday'), ('Tuesday', 'Friday', 'Saturday'), ('Tuesday', 'Saturday', 'Sunday'), ('Tuesday', 'Saturday', 'Monday'), ('Tuesday', 'Saturday', 'Wednesday'), ('Tuesday', 'Saturday', 'Thursday'), ('Tuesday', 'Saturday', 'Friday'), ('Wednesday', 'Sunday', 'Monday'), ('Wednesday', 'Sunday', 'Tuesday'), ('Wednesday', 'Sunday', 'Thursday'), ('Wednesday', 'Sunday', 'Friday'), ('Wednesday', 'Sunday', 'Saturday'), ('Wednesday', 'Monday', 'Sunday'), ('Wednesday', 'Monday', 'Tuesday'), ('Wednesday', 'Monday', 'Thursday'), ('Wednesday', 'Monday', 'Friday'), ('Wednesday', 'Monday', 'Saturday'), ('Wednesday', 'Tuesday', 'Sunday'), ('Wednesday', 'Tuesday', 'Monday'), ('Wednesday', 'Tuesday', 'Thursday'), ('Wednesday', 'Tuesday', 'Friday'), ('Wednesday', 'Tuesday', 'Saturday'), ('Wednesday', 'Thursday', 'Sunday'), ('Wednesday', 'Thursday', 'Monday'), ('Wednesday', 'Thursday', 'Tuesday'), ('Wednesday', 'Thursday', 'Friday'), ('Wednesday', 'Thursday', 'Saturday'), ('Wednesday', 'Friday', 'Sunday'), ('Wednesday', 'Friday', 'Monday'), ('Wednesday', 'Friday', 'Tuesday'), ('Wednesday', 'Friday', 'Thursday'), ('Wednesday', 'Friday', 'Saturday'), ('Wednesday', 'Saturday', 'Sunday'), ('Wednesday', 'Saturday', 'Monday'), ('Wednesday', 'Saturday', 'Tuesday'), ('Wednesday', 'Saturday', 'Thursday'), ('Wednesday', 'Saturday', 'Friday'), ('Thursday', 'Sunday', 'Monday'), ('Thursday', 'Sunday', 'Tuesday'), ('Thursday', 'Sunday', 'Wednesday'), ('Thursday', 'Sunday', 'Friday'), ('Thursday', 'Sunday', 'Saturday'), ('Thursday', 'Monday', 'Sunday'), ('Thursday', 'Monday', 'Tuesday'), ('Thursday', 'Monday', 'Wednesday'), ('Thursday', 'Monday', 'Friday'), ('Thursday', 'Monday', 'Saturday'), ('Thursday', 'Tuesday', 'Sunday'), ('Thursday', 'Tuesday', 'Monday'), ('Thursday', 'Tuesday', 'Wednesday'), ('Thursday', 'Tuesday', 'Friday'), ('Thursday', 'Tuesday', 'Saturday'), ('Thursday', 'Wednesday', 'Sunday'), ('Thursday', 'Wednesday', 'Monday'), ('Thursday', 'Wednesday', 'Tuesday'), ('Thursday', 'Wednesday', 'Friday'), ('Thursday', 'Wednesday', 'Saturday'), ('Thursday', 'Friday', 'Sunday'), ('Thursday', 'Friday', 'Monday'), ('Thursday', 'Friday', 'Tuesday'), ('Thursday', 'Friday', 'Wednesday'), ('Thursday', 'Friday', 'Saturday'), ('Thursday', 'Saturday', 'Sunday'), ('Thursday', 'Saturday', 'Monday'), ('Thursday', 'Saturday', 'Tuesday'), ('Thursday', 'Saturday', 'Wednesday'), ('Thursday', 'Saturday', 'Friday'), ('Friday', 'Sunday', 'Monday'), ('Friday', 'Sunday', 'Tuesday'), ('Friday', 'Sunday', 'Wednesday'), ('Friday', 'Sunday', 'Thursday'), ('Friday', 'Sunday', 'Saturday'), ('Friday', 'Monday', 'Sunday'), ('Friday', 'Monday', 'Tuesday'), ('Friday', 'Monday', 'Wednesday'), ('Friday', 'Monday', 'Thursday'), ('Friday', 'Monday', 'Saturday'), ('Friday', 'Tuesday', 'Sunday'), ('Friday', 'Tuesday', 'Monday'), ('Friday', 'Tuesday', 'Wednesday'), ('Friday', 'Tuesday', 'Thursday'), ('Friday', 'Tuesday', 'Saturday'), ('Friday', 'Wednesday', 'Sunday'), ('Friday', 'Wednesday', 'Monday'), ('Friday', 'Wednesday', 'Tuesday'), ('Friday', 'Wednesday', 'Thursday'), ('Friday', 'Wednesday', 'Saturday'), ('Friday', 'Thursday', 'Sunday'), ('Friday', 'Thursday', 'Monday'), ('Friday', 'Thursday', 'Tuesday'), ('Friday', 'Thursday', 'Wednesday'), ('Friday', 'Thursday', 'Saturday'), ('Friday', 'Saturday', 'Sunday'), ('Friday', 'Saturday', 'Monday'), ('Friday', 'Saturday', 'Tuesday'), ('Friday', 'Saturday', 'Wednesday'), ('Friday', 'Saturday', 'Thursday'), ('Saturday', 'Sunday', 'Monday'), ('Saturday', 'Sunday', 'Tuesday'), ('Saturday', 'Sunday', 'Wednesday'), ('Saturday', 'Sunday', 'Thursday'), ('Saturday', 'Sunday', 'Friday'), ('Saturday', 'Monday', 'Sunday'), ('Saturday', 'Monday', 'Tuesday'), ('Saturday', 'Monday', 'Wednesday'), ('Saturday', 'Monday', 'Thursday'), ('Saturday', 'Monday', 'Friday'), ('Saturday', 'Tuesday', 'Sunday'), ('Saturday', 'Tuesday', 'Monday'), ('Saturday', 'Tuesday', 'Wednesday'), ('Saturday', 'Tuesday', 'Thursday'), ('Saturday', 'Tuesday', 'Friday'), ('Saturday', 'Wednesday', 'Sunday'), ('Saturday', 'Wednesday', 'Monday'), ('Saturday', 'Wednesday', 'Tuesday'), ('Saturday', 'Wednesday', 'Thursday'), ('Saturday', 'Wednesday', 'Friday'), ('Saturday', 'Thursday', 'Sunday'), ('Saturday', 'Thursday', 'Monday'), ('Saturday', 'Thursday', 'Tuesday'), ('Saturday', 'Thursday', 'Wednesday'), ('Saturday', 'Thursday', 'Friday'), ('Saturday', 'Friday', 'Sunday'), ('Saturday', 'Friday', 'Monday'), ('Saturday', 'Friday', 'Tuesday'), ('Saturday', 'Friday', 'Wednesday'), ('Saturday', 'Friday', 'Thursday')])



## Final example for homework problem
#
#outcome = set(["a", "b", "c", "d", "e", "f"])
#
#permutations = gen_permutations(outcome, 4)
#permutation_list = list(permutations)
#permutation_list.sort()
#print
#print "Answer is", permutation_list[100]


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
#x = Zombie(5,4,[],[(2,3),(3,3)])
#x = Zombie(20, 30, [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10)], [], [(18, 14), (18, 20), (14, 24), (7, 24), (2, 22)])
#x = Zombie(3, 3, [], [], [(2, 2)])
#x = Zombie(3, 3, [], [(1, 1)], [(2, 2)])
#print x.__str__()
#x.set_full(2,3)
#print x.__str__()
#print x._zombie_list
#x._zombie_list.pop()
#print x._zombie_list
#print x.num_zombies()
#x.add_zombie(1,1)
#print x.num_zombies()
#print x._zombie_list
#for zombie in x.zombies():
#    print zombie
#x.clear()
#print x.__str__()
#print x._cells

#dist2 = x.compute_distance_field(HUMAN)
#x.move_zombies(dist2)
#print x._zombie_list
#print x.__str__()
