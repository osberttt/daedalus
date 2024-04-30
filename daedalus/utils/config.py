from daedalus.algorithms.base import Algorithm
from daedalus.algorithms.binary_tree import BinaryTree
from daedalus.exporters.ascii.maze import AsciiExporter
from daedalus.exporters.base import Exporter


DEFAULT_ALGORITHM: Algorithm = BinaryTree
DEFAULT_EXPORTER: Exporter = AsciiExporter

PNG_OFFSET: int = 8
PNG_FOLDER: str = "images"
