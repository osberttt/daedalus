from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from daedalus.core.maze import Maze
else:
    Maze = "Maze"


class Exporter(metaclass=ABCMeta):
    @abstractmethod
    def on(self, maze: Maze) -> None:
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self.__class__.__name__
