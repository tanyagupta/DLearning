from __future__ import annotations
from data_structures.referential_array import ArrayR
from data_structures.array_sorted_list import ArraySortedList
class Grid:
    DRAW_STYLE_SET = "SET"
    DRAW_STYLE_ADD = "ADD"
    DRAW_STYLE_SEQUENCE = "SEQUENCE"
    DRAW_STYLE_OPTIONS = (
        DRAW_STYLE_SET,
        DRAW_STYLE_ADD,
        DRAW_STYLE_SEQUENCE
    )

    DEFAULT_BRUSH_SIZE = 2
    MAX_BRUSH = 5
    MIN_BRUSH = 0

    def __init__(self, draw_style, x, y) -> None:
        """
        Initialise the grid object.
        - draw_style:
            The style with which colours will be drawn.
            Should be one of DRAW_STYLE_OPTIONS
            This draw style determines the LayerStore used on each grid square.
        - x, y: The dimensions of the grid.

        Should also intialise the brush size to the DEFAULT provided as a class variable.
        """

        self.rows = x
        self.cols = y
        self.grid = []

        """"
        -making the grid using nested lists inside the main list
        -Here, self.rows is the number of nested lists i.e the rows
         and self.cols is the number of items inside the nested lists i.e the columns
        """
        for i in range(self.rows):
            self.grid.append([None]*self.cols)


    def __getitem__ (self, key):
            return self.grid[key]

    def __setitem__(self, item, row, col):
        self.grid[row][col] = item
         #raise NotImplementedError()

    def increase_brush_size(self):
        """
        Increases the size of the brush by 1,
        if the brush size is already MAX_BRUSH,
        then do nothing.
        """
        raise NotImplementedError()

    def decrease_brush_size(self):
        """
        Decreases the size of the brush by 1,
        if the brush size is already MIN_BRUSH,
        then do nothing.
        """
        raise NotImplementedError()

    def special(self):
        """
        Activate the special affect on all grid squares.
        """
        raise NotImplementedError()
