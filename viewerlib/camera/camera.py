from .config import CameraConfig
import pyray as pr


class Camera3D:
    def __init__(self,
                 camera_config: CameraConfig
                 ):
        self.position = camera_config.position
        self.target = camera_config.target
        self.up = camera_config.up
        self.fovy = camera_config.fovy
        self.projection = camera_config.projection
        self.camera_view_person = camera_config.camera_view_person

        self.camera = pr.Camera3D()
        self.camera.position = self.position
        self.camera.target = self.target
        self.camera.up = self.up
        self.camera.fovy = self.fovy
        self.camera.projection = self.projection

    def update_state(self):
        pr.update_camera(self.camera, self.camera_view_person)

    def begin_mode_3d(self):
        pr.begin_mode_3d(self.camera)

    def end_mode_3d(self):
        pr.end_mode_3d(self.camera)
