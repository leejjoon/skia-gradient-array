from typing import NamedTuple, List, Tuple
import numpy as np

class Point(NamedTuple):
    x: float
    y: float

class RGB(NamedTuple):
    r: float
    g: float
    b: float

class GradientParam(NamedTuple):
    el_id: str
    tag: str
    pt1: Point
    pt2: Point
    oca_list: List[Tuple[float, RGB, float]]
    gradientTransform: np.ndarray
