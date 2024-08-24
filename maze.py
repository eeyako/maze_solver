from __future__ import annotations
import itertools
import random
import time
from graphics import Window
from cell import Cell


class Maze:

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        # type: (float, float, int, int, float, float, Window, int | float | str | bytes | bytearray) -> Maze
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._current_cell = (0, 0)
        self._cells = []  # type: list[list[Cell]]
        if seed:
            random.seed(seed)

        # Build maze
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(i=0, j=0)
        self._reset_cells_visited()

    def _create_cells(self):
        """
        Fills a self._cells list with lists of cells.
        Each top-level list is a column of Cell objects.
        Once the matrix is populated, it calls _draw_cell() method on each Cell.
        """
        # Populate
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(win=self._win))

        # Draw
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i=i, j=j)

    def _draw_cell(self, i, j):
        # type: (int, int) -> None
        """
        Calculates the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself.
        The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.
        Once calculated, it draws the cell and calls the _animate() method.
        """
        if self._win is None:
            return

        # Calculate and draw
        self._cells[i][j].draw(
            self._cell_size_x + self._cell_size_x * i,
            self._cell_size_y + self._cell_size_y * j,
            self._cell_size_x * 2 + self._cell_size_x * i,
            self._cell_size_y * 2 + self._cell_size_y * j
        )
        self._animate()

    def _animate(self):
        """
        Allows us to visualize what the algorithms are doing in real time.
        Calls the window's redraw() method, then sleeps for 0.05 s so our eyes keep up with each render frame.
        """
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        """
        Removes an outer wall from top-left cell and bottom-right cell.
        Calls _draw_cell() after each removal.
        """
        # Randomly pick which wall will be removed for each
        top_lf = self._cells[0][0]
        top_lf.has_left_wall = bool(random.randint(0, 1))
        top_lf.has_top_wall = not top_lf.has_left_wall
        self._draw_cell(i=0, j=0)

        bot_rt = self._cells[self._num_cols - 1][self._num_rows - 1]
        bot_rt.has_right_wall = bool(random.randint(0, 1))
        bot_rt.has_bottom_wall = not bot_rt.has_right_wall
        self._draw_cell(i=self._num_cols - 1, j=self._num_rows - 1)

    def _break_walls_r(self, i, j):
        # type: (int, int) -> None
        """
        Depth-first traversal through the cells, breaking down walls as it goes.
        """
        self._cells[i][j].visited = True
        while True:
            # Check the cells that are directly adjacent to the current cell.
            available_cells = {
                'left': (-1, 0),
                'right': (+1, 0),
                'top': (0, -1),
                'bottom': (0, +1),
            }
            for direction, coords in available_cells.copy().items():
                _i, _j = coords
                # Exclude columns of bounds
                if not (0 <= i + _i <= self._num_cols - 1):
                    available_cells.pop(direction)

                # Exclude rows of bounds
                if not (0 <= j + _j <= self._num_rows - 1):
                    available_cells.pop(direction)

            # Exclude visited
            for direction, coords in available_cells.copy().items():
                _i, _j = coords
                if self._cells[i+_i][j+_j].visited:
                    available_cells.pop(direction)

            # Break out if there are no more available cells
            if not available_cells:
                break

            # Pick a random direciton
            direction = random.choice(list(available_cells))
            _i, _j = available_cells[direction]
            _i += i
            _j += j
            adjacent_cell = self._cells[_i][_j]
            current_cell = self._cells[i][j]

            # Break the appropriate walls depending on direciton
            if direction == 'left':
                current_cell.has_left_wall = False
                adjacent_cell.has_right_wall = False
            elif direction == 'right':
                current_cell.has_right_wall = False
                adjacent_cell.has_left_wall = False
            elif direction == 'top':
                current_cell.has_top_wall = False
                adjacent_cell.has_bottom_wall = False
            elif direction == 'bottom':
                current_cell.has_bottom_wall = False
                adjacent_cell.has_top_wall = False

            # Draw cells
            self._draw_cell(i=i, j=j)
            self._draw_cell(i=_i, j=_j)

            # Recurse
            self._break_walls_r(i=_i, j=_j)

    def _reset_cells_visited(self):
        """
        Resets the visited property of all the cells in the Maze to False.
        """
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        # type: () -> bool
        """
        Calls the _solve_r method starting at i=0 and j=0.
        Returns True if the maze was solved, False otherwise.
        """
        self._current_cell = (0, 0)
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        # type: (int, int) -> bool
        """
        Depth-first search maze solving algorithm.
        Returns True if the current cell is an end cell, OR if it leads to the end cell.
        Returns False if the current cell is a loser cell.
        """
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if (i, j) == (self._num_cols - 1, self._num_rows - 1):
            return True

        # Check the cells that are directly adjacent to the current cell.
        available_cells = {
            'left': (-1, 0),
            'right': (+1, 0),
            'top': (0, -1),
            'bottom': (0, +1),
        }
        for direction, coords in available_cells.copy().items():
            _i, _j = coords
            # Exclude columns of bounds
            if not (0 <= i + _i <= self._num_cols - 1):
                available_cells.pop(direction)

            # Exclude rows of bounds
            if not (0 <= j + _j <= self._num_rows - 1):
                available_cells.pop(direction)

        # Exclude visited
        for direction, coords in available_cells.copy().items():
            _i, _j = coords
            _i += i
            _j += j
            other_cell = self._cells[_i][_j]
            if other_cell.visited:
                available_cells.pop(direction)
            elif direction == 'left' and other_cell.has_right_wall:
                available_cells.pop(direction)
            elif direction == 'right' and other_cell.has_left_wall:
                available_cells.pop(direction)
            elif direction == 'top' and other_cell.has_bottom_wall:
                available_cells.pop(direction)
            elif direction == 'bottom' and other_cell.has_top_wall:
                available_cells.pop(direction)

        # Return False if there are no more available cells
        if not available_cells:
            return False

        # Try on remaining cells
        for direction, coords in available_cells.items():
            _i, _j = coords
            _i += i
            _j += j
            other_cell = self._cells[_i][_j]
            current_cell.draw_move(other_cell)
            success = self._solve_r(i=_i, j=_j)
            if success:
                return True
            current_cell.draw_move(other_cell, undo=True)

        # If we reach this point, none of the options worked out
        return False
