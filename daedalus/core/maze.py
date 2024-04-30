from daedalus.algorithms.base import Algorithm
from daedalus.core.grid import Grid
from daedalus.exporters.base import Exporter
from daedalus.utils.config import DEFAULT_ALGORITHM, DEFAULT_EXPORTER


class Maze:
    def __init__(
        self,
        grid: Grid,
        algorithm: Algorithm = DEFAULT_ALGORITHM(),
    ) -> None:
        if not isinstance(algorithm, Algorithm) and algorithm is not None:
            raise ValueError("algorithm must be of type Algorithm ")
        if not isinstance(grid, Grid):
            raise ValueError("grid must be of type Grid")
        self.grid = grid
        self.algorithm = algorithm
        self.algorithm.on(self.grid)

    def export(self, exporter: Exporter = DEFAULT_EXPORTER()) -> "Maze":
        exporter.on(self)
        return self

    def __json__(self) -> dict:
        return {"grid": self.grid.__json__()}

    def __eq__(self, maze: "Maze") -> bool:
        return self.grid == maze.grid
