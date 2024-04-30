from daedalus.algorithms.base import Algorithm
from daedalus.core.grid import Grid


class AldousBroder(Algorithm):
    def on(self, grid: Grid) -> None:
        current_cell = grid.random_cell()
        unvisited_count = grid.size - 1

        while unvisited_count > 0:
            neighbour = current_cell.random_neighbour()
            if neighbour is None:
                raise ValueError(f"{current_cell} has no neighbour")
            if len(neighbour.links) == 0:
                current_cell.link(neighbour)
                unvisited_count -= 1
            current_cell = neighbour
