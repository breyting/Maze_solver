from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze solver")
        self.__canvas = Canvas(self.__root, bg="White", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        
    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill = fill_color,
            width = 2
        )


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self,x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(wall)

        if self.has_right_wall:
            wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(wall)

        if self.has_top_wall:
            wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(wall)

        if self.has_left_wall:
            wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(wall)
        