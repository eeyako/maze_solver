from __future__ import annotations
import time
from graphics import Window
from cell import Cell


class Maze:

    def __init__(self, x1: float, y1: float, num_rows: int, num_cols: int, cell_size_x: float, cell_size_y: float, win: Window) -> None:
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

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

    def _draw_cell(self, i: int, j: int):
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
            self._cell_size_y * 2 + self._cell_size_y * j,
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
        time.sleep(0.05)
