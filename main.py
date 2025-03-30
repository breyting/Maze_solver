from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c1 = Cell(win)
    c1.has_right_wall = False
    c1.draw(125, 125, 200, 200)

    c2 = Cell(win)
    c2.has_bottom_wall = False
    c2.draw(225, 225, 250, 250)

    c3 = Cell(win)
    c3.has_top_wall = False
    c3.draw(300, 300, 500, 500)

    c.draw_move(c2)
    c3.draw_move(c1, True)

    win.wait_for_close()

main()
