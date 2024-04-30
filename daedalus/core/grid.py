from random import randrange
from typing import List, Optional, cast
from daedalus.core.cell import Cell
from daedalus.utils.types import CellPoint


class Grid:
    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def size(self) -> int:
        return self.rows * self.columns

    def __init__(self, rows: int, columns: int) -> None:
        if rows is None or rows < 0:
            raise ValueError("rows must be a positive integer")
        if columns is None or columns < 0:
            raise ValueError("columns must be a positive integer")
        self._rows: int = rows
        self._columns: int = columns
        self._grid: List[List[Cell]] = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self) -> List[List[Cell]]:
        return [[Cell(i, j) for j in range(self.columns)] for i in range(self.rows)]

    # Set neighbours to cells
    def configure_cells(self) -> None:
        for cell in self.each_cell():
            row, column = cell.row, cell.column
            cell.north = self[row - 1, column]
            cell.south = self[row + 1, column]
            cell.west = self[row, column - 1]
            cell.east = self[row, column + 1]

    def each_row(self):
        for row in range(self.rows):
            yield self._grid[row]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def cell_at(self, cell: CellPoint) -> Optional[Cell]:
        row, column = cell
        if not 0 <= row < self.rows:
            return None
        if not 0 <= column < self.columns:
            return None
        return cast(Cell, self._grid[row][column])

    def set_cell_at(self, cell: CellPoint, value: Cell) -> None:
        row, column = cell
        self._grid[row][column] = value

    def __getitem__(self, cell: CellPoint) -> Optional[Cell]:
        return self.cell_at(cell)

    def __setitem__(self, cell: CellPoint, value) -> None:
        self.set_cell_at(cell, value)

    def random_cell(self) -> Cell:
        row = randrange(0, self.rows)
        column = randrange(0, self.columns)
        cell: Cell = self[row, column]
        return cell

    def __repr__(self) -> str:
        return str(self._grid)

    def __json__(self) -> dict:
        return {
            "rows": self.rows,
            "columns": self.columns,
            "cells": [cell.__json__() for cell in self.each_cell()],
        }

    def __eq__(self, grid: "Grid") -> bool:
        for self_cell in self.each_cell():
            grid_cell = grid[self_cell.row, self_cell.column]
            if self_cell.links != grid_cell.links:
                return False
        return True
