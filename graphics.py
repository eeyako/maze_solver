from __future__ import annotations
from tkinter import Tk, BOTH, Canvas
from colors import *


class Window:

    def __init__(self, width: int, height: int):
        self.__root = Tk()
        print(self.__root['background'])
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

    def draw_line(self, line: Line, fill_color: str = BLACK):
        line.draw(self.__canvas, fill_color=fill_color)


class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:

    def __init__(self, point0: Point, point1: Point) -> None:
        self.point0 = point0
        self.point1 = point1

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.point0.x,
            self.point0.y,
            self.point1.x,
            self.point1.y,
            fill=fill_color,
            width=2
        )
