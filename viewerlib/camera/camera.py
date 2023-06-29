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
        self.camera.position = pr.Vector3(self.position[0], self.position[1], self.position[2])
        self.camera.target = pr.Vector3(self.target[0], self.target[1], self.target[2])
        self.camera.up = pr.Vector3(self.up[0], self.up[1], self.up[2])
        self.camera.fovy = self.fovy
        self.camera.projection = self.projection

    def update_state(self):
        pr.update_camera(self.camera, self.camera_view_person)

    def begin_mode_3d(self):
        pr.begin_mode_3d(self.camera)

    def end_mode_3d(self):
        pr.end_mode_3d(self.camera)
