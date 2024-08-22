import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10
        )
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_2(self):
        num_rows = 50
        num_cols = 100
        m1 = Maze(
            x1=0,
            y1=0,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=150,
            cell_size_y=10
        )
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_3(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(
            x1=20,
            y1=20,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10
        )
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_break_walls(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(
            x1=20,
            y1=20,
            num_rows=num_rows,
            num_cols=num_cols,
            cell_size_x=10,
            cell_size_y=10
        )
        top_lf = m1._cells[0][0]
        bot_rt = m1._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(
            {False, True},
            {top_lf.has_left_wall, top_lf.has_top_wall}
        )
        self.assertEqual(
            {False, True},
            {bot_rt.has_right_wall, bot_rt.has_bottom_wall}
        )


if __name__ == '__main__':
    unittest.main()
