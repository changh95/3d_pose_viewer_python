import pyray as pr
import dataclasses


@dataclasses.dataclass
class CameraConfig:
    position: pr.Vector3
    target: pr.Vector3
    up: pr.Vector3
    fovy: float
    projection: pr.CameraProjection
    camera_view_person: int
