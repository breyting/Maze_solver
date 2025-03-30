from graphics import Window, Line, Point


def main():
    win = Window(800, 600)

    point1 = Point(1, 1)
    point2 = Point(100, 100)
    point3 = Point(50, 200)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)

    win.draw_line(line1, "red")
    win.draw_line(line2, "black")

    win.wait_for_close()

main()
