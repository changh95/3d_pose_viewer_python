import dataclasses
from typing import NewType

import pyray as pr


Position3D = NewType("Position3D", list[float])
Vector3D = NewType("Vector3D", list[float])


@dataclasses.dataclass
class CameraConfig:
    position: Position3D
    target: Position3D
    up: Vector3D
    fovy: float
    projection: pr.CameraProjection


@dataclasses.dataclass
class WindowConfig:
    width: int
    height: int
    window_name: str
    target_fps: int


class Window:
    def __init__(self,
                 window_config: WindowConfig
                 ):
        self.width = window_config.width
        self.height = window_config.height
        self.window_name = window_config.window_name
        self.target_fps = window_config.target_fps

        pr.init_window(self.width, self.height, self.window_name)
        pr.set_target_fps(self.target_fps)


if __name__ == "__main__":
    # Setup window
    win_cfg = WindowConfig(1280, 720, "3D pose_viewer", 60)
    window = Window(win_cfg)

    # Setup camera
    cam_cfg = CameraConfig(Position3D([18.0, 16.0, 18.0]), Position3D([0.0, 0.0, 0.0]), Vector3D([0.0, 1.0, 0.0]), 45.0, pr.CameraProjection.CAMERA_PERSPECTIVE)

    cam = pr.Camera3D()
    cam.position = [18.0, 16.0, 18.0]
    cam.target = [0.0, 0.0, 0.0]
    cam.up = [0.0, 1.0, 0.0]
    cam.fovy = 45.0
    cam.projection = pr.CameraProjection.CAMERA_PERSPECTIVE

    start_position = pr.Vector3(0.0, 0.0, 0.0)
    end_position = pr.Vector3(5.0, 5.0, 5.0)

    while not pr.window_should_close():
        pr.update_camera(cam, pr.CAMERA_THIRD_PERSON)

        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)

        pr.begin_mode_3d(cam)
        pr.draw_line_3d(start_position, end_position, pr.RED)
        pr.draw_grid(20, 1.0)
        pr.end_mode_3d()

        pr.draw_text("Hello world", 190, 200, 20, pr.VIOLET)
        pr.end_drawing()
    pr.close_window()
