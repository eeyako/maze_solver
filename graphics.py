from __future__ import annotations

from tkinter import BOTH, Canvas, Tk

from colors import BLACK


class Window:
    def __init__(self, width, height):
        # type: (int, int) -> Window
        self.__root = Tk()
        self.__root.title(string="Maze Solver")
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol(name="WM_DELETE_WINDOW", func=self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color=BLACK):
        # type: (Line, str) -> None
        line.draw(self.__canvas, fill_color=fill_color)


class Point:
    def __init__(self, x, y):
        # type: (float, float) -> None
        self.x = x
        self.y = y


class Line:
    def __init__(self, point0, point1):
        # type: (Point, Point) -> None
        self.point0 = point0
        self.point1 = point1

    def draw(self, canvas, fill_color):
        # type: (Canvas, str) -> None
        canvas.create_line(self.point0.x, self.point0.y, self.point1.x, self.point1.y, fill=fill_color, width=2)
