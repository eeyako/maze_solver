from __future__ import annotations
from graphics import Window, Line, Point
from colors import *

class Cell:

    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x0 = None
        self._y0 = None
        self._x1 = None
        self._y1 = None
        self._win = win

    def draw(self, x0: float, y0: float, x1: float, y1: float):
        if self._win is None:
            return

        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

        # Draw left wall
        self._win.draw_line(
            Line(
                point0=Point(x=x0, y=y0),
                point1=Point(x=x0, y=y1)
            ),
            fill_color=BLACK if self.has_left_wall else WHITE
        )

        # Draw right wall
        self._win.draw_line(
            Line(
                point0=Point(x=x1, y=y0),
                point1=Point(x=x1, y=y1)
            ),
            fill_color=BLACK if self.has_right_wall else WHITE
        )

        # Draw top wall
        self._win.draw_line(
            Line(
                point0=Point(x=x0, y=y0),
                point1=Point(x=x1, y=y0)
            ),
            fill_color=BLACK if self.has_top_wall else WHITE
        )

        # Draw bottom wall
        self._win.draw_line(
            Line(
                point0=Point(x=x0, y=y1),
                point1=Point(x=x1, y=y1)
            ),
            fill_color=BLACK if self.has_bottom_wall else WHITE
        )

    def draw_move(self, to_cell: Cell, undo=False):
        mid_point0 = Point(
            x=(self._x1 + self._x0) / 2,
            y=(self._y1 + self._y0) / 2
        )
        mid_point1 = Point(
            x=(to_cell._x1 + to_cell._x0) / 2,
            y=(to_cell._y1 + to_cell._y0) / 2
        )
        self._win.draw_line(
            Line(point0=mid_point0, point1=mid_point1),
            fill_color="gray" if undo else "red"
        )
