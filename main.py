from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)

    cell1 = Cell(True, False, True, True, 400, 500, 400, 500, win)

    cell2 = Cell(True, True, False, False, 600, 700, 200, 300, win)

    cell1.draw()
    cell2.draw()

    win.wait_for_close()

main()
