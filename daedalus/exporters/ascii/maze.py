from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from daedalus.core.maze import Maze
else:
    Maze = "Maze"
from daedalus.exporters.base import Exporter


class AsciiExporter(Exporter):
    def __init__(self, cell_width: int = 3) -> None:
        self.cell_width = cell_width

    def on(self, maze: Maze) -> None:
        super().on(maze)

        cell_width = (
            max(len(str(maze.grid.size)), 3)
            if self.show_distances or self.show_path
            else self.cell_width
        )

        # topmost line
        output = "+" + ("-" * cell_width + "+") * maze.grid.columns + "\n"
        for row in maze.grid.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                # for distances and paths
                if self.show_distances:
                    body = " " * (cell_width - len(str(maze.distances[cell]))) + str(
                        maze.distances[cell]
                    )
                elif self.show_path and cell in maze.path:
                    body = " " * (cell_width - len(str(maze.path[cell]))) + str(
                        maze.path[cell]
                    )
                else:
                    body = " " * cell_width

                east_boundary = " " if cell.is_linked(cell.east) else "|"
                top += body + east_boundary
                south_boundary = (
                    " " * cell_width if cell.is_linked(cell.south) else "-" * cell_width
                )
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        print(output)
