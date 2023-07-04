from viewerlib import *
from poselib import *
import numpy as np
from scipy.spatial.transform import Rotation

# TODO: Make z-direction point up

if __name__ == "__main__":
    # Setup window
    screen_width = 1920
    screen_height = 1080
    win_cfg = WindowConfig(screen_width, screen_height, "3D pose_viewer", 60)
    window = Window(win_cfg)

    # Setup camera
    cam_starting_target = np.array([-1359, -1847, 118])
    cam_starting_position = cam_starting_target + 10
    cam_up_vector = np.array([0.0, 1.0, 0.0])
    cam_cfg = CameraConfig(cam_starting_position, cam_starting_target, cam_up_vector, 45.0,
                           pr.CameraProjection.CAMERA_PERSPECTIVE, pr.CAMERA_THIRD_PERSON)
    cam = Camera3D(cam_cfg)

    # Generate motion
    left_poses = []
    right_poses = []
    raw_data = np.load('poses_bounds.npy', allow_pickle=True)
    raw_data = raw_data[:, :-2]
    for index, data in enumerate(raw_data):
        data = data.reshape(3,5)
        data = data[:, :-1]

        if index % 2 == 0:
            left_poses.append(data)
        else:
            right_poses.append(data)

    center_poses = []
    for left_pose, right_pose in zip(left_poses, right_poses):
        center_poses.append(average_pose(left_pose, right_pose))

    center_poses = generate_spiral_motion(center_poses, np.deg2rad(20), 1)

    while not pr.window_should_close():
        cam.update_state()

        begin_drawing()
        clear_background(pr.RAYWHITE)

        cam.begin_mode_3d()
        # draw_line_3d_np(np.array([0.0, 0.0, 0.0]), np.array([5.0, 5.0, 5.0]), pr.RED)
        draw_point_3d_np(np.array([10.0, 10.0, 10.0]), pr.RED)
        draw_sphere_np(np.array([10.0, 10.0, 10.0]), 0.1, pr.RED)
        draw_grid(200, 1.0)

        for left_pose in left_poses:
            draw_coordinate_frame(left_pose, PoseConvention.OPENCV)

        for right_pose in right_poses:
            draw_coordinate_frame(right_pose, PoseConvention.OPENCV)

        for center_pose in center_poses:
            draw_coordinate_frame(center_pose, PoseConvention.OPENCV)

        cam.end_mode_3d()

        draw_coordinate_label(5, 30, cam.camera)
        draw_text("WASD and mouse to move", 10, 30, 20, pr.VIOLET)
        draw_fps(10, 10)
        end_drawing()
    close_window()
