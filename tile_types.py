import numpy as np  # type: ignore
from typing import Tuple

import colour


# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32), # Unicode codepoint.
        ("fg", "3B"),     # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)


#Tile attributes
TA_DARK        = "dark"
TA_LIGHT       = "light"
TA_TRANSPARENT = "transparent"
TA_WALKABLE    = "walkable"


# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        (TA_WALKABLE, np.bool),    # True if this tile can be walked over.
        (TA_TRANSPARENT, np.bool), # True if this tile doesn't block FOV.
        (TA_DARK, graphic_dt),     # Graphics for when this tile is not in FOV.
        (TA_LIGHT, graphic_dt),    # Graphics for when this tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]]
    ) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), colour.white, colour.black), dtype=graphic_dt)


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), colour.white, colour.tile_dark_floor_bg),
    light=(ord(" "), colour.white, colour.tile_light_floor_bg),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), colour.tile_dark_down_stairs_fg,
          colour.tile_dark_floor_bg
    ),
    light=(ord(">"), colour.white, colour.tile_light_floor_bg),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), colour.white, colour.tile_dark_wall_bg),
    light=(ord(" "), colour.white, colour.tile_light_wall_bg),
)
