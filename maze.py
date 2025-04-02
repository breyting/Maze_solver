from graphics import Cell
import time
import random
from enum import Enum

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        i_last_col = len(self._cells) - 1
        i_last_row = len(self._cells[i_last_col]) - 1
        self._cells[i_last_col][i_last_row].has_bottom_wall = False
        self._draw_cell(i_last_col, i_last_row)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = self._x1 + ((i + 1) * self._cell_size_x)
        y2 = self._y1 + ((j + 1) * self._cell_size_y)

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.001)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            visited = []
            possible_direction = []

            if i+1 < len(self._cells) and not self._cells[i+1][j].visited:
                possible_direction.append(self._cells[i+1][j])
            if i-1 >= 0 and not self._cells[i-1][j].visited:
                possible_direction.append(self._cells[i-1][j])
            if j+1 < len(self._cells[i]) and not self._cells[i][j+1].visited:
                possible_direction.append(self._cells[i][j+1])
            if j-1 >= 0 and not self._cells[i][j-1].visited:
                possible_direction.append(self._cells[i][j-1])

            if len(possible_direction) == 0:
                self._draw_cell(i, j)
                return
            
            rdm_cell = possible_direction[random.randrange(0, len(possible_direction))]

            if i+1 < len(self._cells) and self._cells[i+1][j] == rdm_cell:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            if i-1 >= 0 and self._cells[i-1][j] == rdm_cell:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            if j+1 < len(self._cells[i]) and self._cells[i][j+1] == rdm_cell:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)
            if j-1 >= 0 and self._cells[i][j-1] == rdm_cell:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)


    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    
    def solve(self):
        return self._solve_r()

    
    def _solve_r(self, i=0, j=0):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[len(self._cells)-1][len(self._cells[len(self._cells)-1])-1]:
            return True
        

        if i-1 >= 0 and (not self._cells[i][j].has_left_wall) and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            res = self._solve_r(i-1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if i+1 < len(self._cells) and (not self._cells[i][j].has_right_wall) and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            res = self._solve_r(i+1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        
        if j-1 >= 0 and (not self._cells[i][j].has_top_wall) and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            res = self._solve_r(i, j-1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        
        if j+1 < len(self._cells[i]) and (not self._cells[i][j].has_bottom_wall) and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            res = self._solve_r(i, j+1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False
