
from graphics import Window, Line, Point


def main():
    win = Window(width=800, height=600)
    line0 = Line(point0=Point(x=10, y=10), point1=Point(x=50, y=10))
    line1 = Line(point0=Point(x=50, y=10), point1=Point(x=50, y=50))
    line2 = Line(point0=Point(x=10, y=10), point1=Point(x=10, y=50))
    line3 = Line(point0=Point(x=10, y=50), point1=Point(x=50, y=50))
    win.draw_line(line=line0, fill_color="black")
    win.draw_line(line=line1, fill_color="black")
    win.draw_line(line=line2, fill_color="black")
    win.draw_line(line=line3, fill_color="black")
    win.wait_for_close()


if __name__ == '__main__':
    main()
