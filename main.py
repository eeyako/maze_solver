
from graphics import Window, Cell
import random


def main():
    win = Window(width=800, height=600)
    for y in range(10):
        for x in range(14):
            cell = Cell(win=win)
            cell.has_left_wall = bool(random.randint(0, 1))
            cell.has_right_wall = bool(random.randint(0, 1))
            cell.has_top_wall = bool(random.randint(0, 1))
            cell.has_bottom_wall = bool(random.randint(0, 1))
            cell.draw(
                50 + 50 * x,
                50 + 50 * y,
                100 + 50 * x,
                100 + 50 * y
            )
    win.wait_for_close()


if __name__ == '__main__':
    main()
