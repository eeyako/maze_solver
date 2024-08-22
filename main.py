from graphics import Window
from maze import Maze


def main():
    win = Window(width=800, height=600)

    maze = Maze(
        x1=50,
        y1=50,
        num_rows=10,
        num_cols=14,
        cell_size_x=50,
        cell_size_y=50,
        win=win
    )
    maze._create_cells()

    win.wait_for_close()


if __name__ == '__main__':
    main()
