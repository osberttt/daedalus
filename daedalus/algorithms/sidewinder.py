from random import choice, randint
from typing import cast
from daedalus.algorithms.base import Algorithm
from daedalus.core.cell import Cell
from daedalus.core.grid import Grid


class SideWinder(Algorithm):
    def on(self, grid: Grid) -> None:
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)

                cell_has_no_east = cell.east is None
                cell_has_north = isinstance(cell.north, Cell)
                head_in_coin_toss = randint(0, 1) == 0

                go_north = cell_has_no_east or (cell_has_north and head_in_coin_toss)

                if go_north:
                    chosen_cell = cast(Cell, choice(run))
                    if chosen_cell.north:
                        chosen_cell.link(chosen_cell.north)
                    run.clear()
                else:
                    cell.link(cell.east)
