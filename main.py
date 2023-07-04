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

    # Generate spiral motion
    poses = []
    position = np.array([0.5, 0.5, 0.0])
    rotation = np.eye(3)
    pose = np.eye(4)
    pose[:3, :3] = rotation
    pose[:3, 3] = position

    for iter in range(100):
        poses.append(pose.copy())
        pose[0, 3] += 1.0

    # # first frame
    # rotation_first_frame = Rotation.from_euler('y', np.deg2rad(30)).as_matrix()
    # pose[:3, :3] = rotation_first_frame
    # pose[:3, 3] = position
    # poses.append(pose)
    #
    # for iter in range(100):
    #     spin_radians = np.deg2rad(10.0)
    #     rotation_matrix = Rotation.from_euler('z', spin_radians).as_matrix()
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
            draw_coordinate_frame(pose, PoseConvention.OPENGL)

        # position = np.array([0.5, 0.5, 0.0])
        # rotation = np.eye(3)
        #
        # extrinsic_matrix = np.eye(4)
        # extrinsic_matrix[:3, :3] = rotation
        # extrinsic_matrix[:3, 3] = position
        #
        # yaw_angle_degrees = 10.0
        # yaw_angle_radians = np.deg2rad(yaw_angle_degrees)
        # rotation_matrix = Rotation.from_euler('y', yaw_angle_radians).as_matrix()
        # transformation = np.eye(4)
        # transformation[:3, :3] = rotation_matrix
        #
        # for iter in range(10):
        #     draw_coordinate_frame_np(extrinsic_matrix, PoseConvention.OPENCV)
        #     extrinsic_matrix = extrinsic_matrix @ transformation
        #     extrinsic_matrix[0, 3] += 1.0

        cam.end_mode_3d()

        x_coord_pos = pr.get_world_to_screen(pr.Vector3(5, 0, 0), cam.camera)
        y_coord_pos = pr.get_world_to_screen(pr.Vector3(0, 5, 0), cam.camera)
        z_coord_pos = pr.get_world_to_screen(pr.Vector3(0, 0, 5), cam.camera)
        pr.draw_text("x", int(x_coord_pos.x), int(x_coord_pos.y), 30, pr.BLACK)
        pr.draw_text("y", int(y_coord_pos.x), int(y_coord_pos.y), 30, pr.BLACK)
        pr.draw_text("z", int(z_coord_pos.x), int(z_coord_pos.y), 30, pr.BLACK)
        pr.draw_text("WASD and mouse to move", 10, 30, 20, pr.VIOLET)
        pr.draw_fps(10, 10)
        pr.end_drawing()
    pr.close_window()
