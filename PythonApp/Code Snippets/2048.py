"""
Clone of 2048 game.
"""

###import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = []
    new_line_item = 0
    for line_item in range(len(line)):
        new_line.append(0)
        if line[line_item] != 0:
            if new_line[new_line_item] == 0:
                new_line[new_line_item] = line[line_item]
            elif new_line[new_line_item] != line[line_item]:
                new_line_item += 1
                new_line[new_line_item] = line[line_item]
            elif new_line[new_line_item] == line[line_item]:
                new_line[new_line_item] *= 2
                new_line_item += 1
    return new_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    Methods: reset(), __str__(), get_grid_height()
            , get_grid_width(), move(direction)
            , new_title(), set_tile(row, col, value)
            , get_tile(row, col)
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = []

        self.reset()

        rows = grid_height
        columns = grid_width

        up_list = []
        down_list = []
        for column in range(columns):
            up_list.append([0, column])
            down_list.append([rows - 1, column])

        left_list = []
        right_list = []
        for row in range(rows):
            left_list.append([row, 0])
            right_list.append([row, columns - 1])

        self.dir_dict = {UP: up_list, DOWN: down_list, LEFT: left_list, RIGHT: right_list}

        self.dir_moves = {UP: grid_height, DOWN: grid_height, LEFT: grid_width, RIGHT: grid_width}

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        rows = self.grid_height
        columns = self.grid_width
        row_list = []

        for dummy_row in range(rows):
            column_list = []
            for dummy_column in range(columns):
                column_list.append(0)
            row_list.append(column_list)

        self.grid = row_list

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return self.grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tiles_moved = 0
        for each_index in self.dir_dict[direction]:
            init_index1 = list(each_index)
            init_index2 = list(each_index)
            temp_list = []
            for next_item in range(self.dir_moves[direction]):
                temp_list.append(self.grid[each_index[0]][each_index[1]])
                init_index1[0] += OFFSETS[direction][0]
                init_index1[1] += OFFSETS[direction][1]

            temp_list = merge(temp_list)

            for next_item in range(self.dir_moves[direction]):
                if temp_list[next_item] != self.grid[init_index2[0]][init_index2[1]]:
                    tiles_moved = 1
                self.grid[init_index2[0]][init_index2[1]] = temp_list[next_item]
                init_index2[0] += OFFSETS[direction][0]
                init_index2[1] += OFFSETS[direction][1]

        if tiles_moved == 1:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        rows = self.grid_height
        columns = self.grid_width
        zero_list = []

        for row in range(rows):
            for column in range(columns):
                if self.grid[row][column] == 0:
                    zero_list.append([row, column])

        rand = random.choice(zero_list)
        rand_int = random.randint(0, 9)
        if rand_int == 0:
            self.grid[rand[0]][rand[1]] = 4
        else:
            self.grid[rand[0]][rand[1]] = 2

        return zero_list

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

###poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

game = TwentyFortyEight(4,4)
print game.__str__()
game.new_tile()
game.move(DOWN)
print game.__str__()
game.move(RIGHT)
print game.__str__()
game.move(DOWN)
print game.__str__()
game.move(RIGHT)
print game.__str__()
game.move(LEFT)
print game.__str__()
game.move(UP)
print game.__str__()
game.move(UP)
print game.__str__()
game.move(UP)
print game.__str__()
game.move(LEFT)
print game.__str__()