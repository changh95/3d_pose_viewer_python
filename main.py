from viewerlib import *
import numpy as np
from scipy.spatial.transform import Rotation

# TODO: Make z-direction point up

if __name__ == "__main__":
    # Setup window
    screen_width = 1280
    screen_height = 720
    win_cfg = WindowConfig(screen_width, screen_height, "3D pose_viewer", 60)
    window = Window(win_cfg)

    # Setup camera
    cam_cfg = CameraConfig(np.array([18.0, 16.0, 18.0]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), 45.0,
                           pr.CameraProjection.CAMERA_PERSPECTIVE, pr.CAMERA_THIRD_PERSON)
    cam = Camera3D(cam_cfg)

    start_position = np.array([0.0, 0.0, 0.0])
    end_position = np.array([5.0, 5.0, 5.0])

    # Generate motion
    poses = []
    position = np.array([0.5, 0.5, 0.0])
    rotation = np.eye(3)
    pose = np.eye(4)
    pose[:3, :3] = rotation
    pose[:3, 3] = position

    # Straight motion
    for iter in range(100):
        poses.append(pose.copy())
        pose[0, 3] += 1.0

    # Spiral motion
    transformation = np.eye(4)
    rotation_first_frame = Rotation.from_euler('x', np.deg2rad(30)).as_matrix()
    transformation[:3, :3] = rotation_first_frame
    poses[0] = poses[0] @ transformation

    # for iter in range(100):
    #     spin_radians = np.deg2rad(10.0)
    #     rotation_matrix = Rotation.from_euler('x', spin_radians).as_matrix()
    #     transformation = np.eye(4)
    #     transformation[:3, :3] = rotation_matrix
    #
    #     pose = pose @ transformation
    #     pose[0, 3] += 1.0
    #     poses.append(pose)

    while not pr.window_should_close():
        cam.update_state()

        begin_drawing()
        clear_background(pr.RAYWHITE)

        cam.begin_mode_3d()
        draw_line_3d_np(start_position, end_position, pr.RED)
        draw_point_3d_np(np.array([10.0, 10.0, 10.0]), pr.RED)
        draw_sphere_np(np.array([10.0, 10.0, 10.0]), 0.1, pr.RED)
        draw_grid(200, 1.0)

        for pose in poses:
            draw_coordinate_frame(pose, PoseConvention.OPENCV)

        cam.end_mode_3d()

        draw_coordinate_label(5, 30, cam.camera)
        draw_text("WASD and mouse to move", 10, 30, 20, pr.VIOLET)
        draw_fps(10, 10)
        end_drawing()
    close_window()
