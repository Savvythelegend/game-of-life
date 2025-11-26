# # creating the desired pattern from cli


# class LifeGrid:
#     def __init__ (self, pattern):
#         self.pattern = pattern
        
#     def evolve (self):
#         """
#         we'll only focus on alive_cells
#         for each cells which in the alive_cells 

#         we'll calculate the neighbours
#         apply the rules to get teh next_gen cell
#         (stay_alive , come_alive)
#         for row, col in self.pattern.alive_cells:
            
#             stay_alive : rule 1 . sum of neighbours in (2,3)

#             come_alive : rule 2. sum of neigbours  == 3 and (is three if alive_cells[row][col] == 0)
        
#         """

#         for row, col in self.pattern.alive_cells:
            

import collections

ALIVE = "♥"
DEAD = "‧"


class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors = (
            (-1, -1),  # Above left
            (-1, 0),  # Above
            (-1, 1),  # Above right
            (0, -1),  # Left
            (0, 1),  # Right
            (1, -1),  # Below left
            (1, 0),  # Below
            (1, 1),  # Below right
        )
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row + drow, col + dcol)] += 1

        stay_alive = {
            cell for cell, num in num_neighbors.items() if num in {2, 3}
        } & self.pattern.alive_cells
        come_alive = {
            cell for cell, num in num_neighbors.items() if num == 3
        } - self.pattern.alive_cells

        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox):
        start_col, start_row, end_col, end_row = bbox
        display = [self.pattern.name.center(2 * (end_col - start_col))]
        for row in range(start_row, end_row):
            display_row = [
                ALIVE if (row, col) in self.pattern.alive_cells else DEAD
                for col in range(start_col, end_col)
            ]
            display.append(" ".join(display_row))
        return "\n ".join(display)

    def __str__(self):
        return f"{self.pattern.name}:\nAlive cells -> {sorted(self.pattern.alive_cells)}"