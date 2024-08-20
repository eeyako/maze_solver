from graphics import Window, Line, Point


class Cell:

    def __init__(self, win: Window) -> None:
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
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1
        if self.has_left_wall:
            self._win.draw_line(
                Line(
                    point0=Point(x=x0, y=y0),
                    point1=Point(x=x0, y=y1)
                )
            )
        if self.has_right_wall:
            self._win.draw_line(
                Line(
                    point0=Point(x=x1, y=y0),
                    point1=Point(x=x1, y=y1)
                )
            )
        if self.has_top_wall:
            self._win.draw_line(
                Line(
                    point0=Point(x=x0, y=y0),
                    point1=Point(x=x1, y=y0)
                )
            )
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(
                    point0=Point(x=x0, y=y1),
                    point1=Point(x=x1, y=y1)
                )
            )
