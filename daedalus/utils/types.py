from typing import TYPE_CHECKING, Dict, Tuple

if TYPE_CHECKING:
    from daedalus.core.cell import Cell
else:
    Cell = "Cell"


CellPoint = Tuple[int, int]
Distances = Dict[Cell, int]
