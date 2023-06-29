import numpy as np
import pyray as pr
import dataclasses


@dataclasses.dataclass
class CameraConfig:
    position: np.array
    target: np.array
    up: np.array
    fovy: float
    projection: pr.CameraProjection
    camera_view_person: int
