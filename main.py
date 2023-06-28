from viewerlib import *


if __name__ == "__main__":
    # Setup window
    win_cfg = WindowConfig(1280, 720, "3D pose_viewer", 60)
    window = Window(win_cfg)

    # Setup camera
    cam_cfg = CameraConfig(pr.Vector3(18.0, 16.0, 18.0), pr.Vector3(0.0, 0.0, 0.0), pr.Vector3(0.0, 1.0, 0.0), 45.0, pr.CameraProjection.CAMERA_PERSPECTIVE, pr.CAMERA_THIRD_PERSON)
    cam = Camera3D(cam_cfg)

    start_position = pr.Vector3(0.0, 0.0, 0.0)
    end_position = pr.Vector3(5.0, 5.0, 5.0)

    while not pr.window_should_close():
        cam.update_state()

        begin_drawing()
        clear_background(pr.RAYWHITE)

        cam.begin_mode_3d()
        draw_line_3d(start_position, end_position, pr.RED)
        draw_point_3d(pr.Vector3(10.0, 10.0, 10.0), pr.RED)
        draw_sphere(pr.Vector3(10.0, 10.0, 10.0), 0.1, pr.RED)
        draw_grid(200, 1.0)

        for x in range(10):
            if x % 2 != 0:
                continue
            for y in range (10):
                if y % 2 != 0:
                    continue
                for z in range (10):
                    if z % 2 != 0:
                        continue
                    draw_coordinate_frame(pr.Vector3(x,y,z), pr.Vector3(0.0, 0.0, 0.0), PoseConvention.OPENCV)

        cam.end_mode_3d()

        pr.draw_text("WASD and mouse to move",10, 30, 20, pr.VIOLET)
        pr.draw_fps(10, 10)
        pr.end_drawing()
    pr.close_window()
