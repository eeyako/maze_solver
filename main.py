from graphics import Window
from maze import Maze


def main():
    win = Window(width=800, height=600)

    num_rows = 10
    num_cols = 14
    m1 = Maze(
        x1=50,
        y1=50,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=50,
        cell_size_y=50,
        win=win,
    )

    m1.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
