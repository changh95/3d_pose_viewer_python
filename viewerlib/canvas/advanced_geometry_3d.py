from .primitive_geometry_3d import *
import pyray as pr

from enum import Enum


class PoseConvention(Enum):
    OPENCV = 0
    LLFF = 1
    OPENGL = 2
    NERF = 3


def draw_coordinate_frame(
        extrinsic_matrix_4x4: np.matrix,
        pose_convention: PoseConvention
):
    if pose_convention == PoseConvention.OPENCV:
        draw_coordinate_frame_opencv(extrinsic_matrix_4x4)
    elif pose_convention == PoseConvention.LLFF:
        draw_coordinate_frame_llff(extrinsic_matrix_4x4)
    elif pose_convention == PoseConvention.OPENGL:
        draw_coordinate_frame_opengl_nerf(extrinsic_matrix_4x4)
    elif pose_convention == PoseConvention.NERF:
        draw_coordinate_frame_opengl_nerf(extrinsic_matrix_4x4)


def draw_coordinate_frame_opencv(extrinsic_matrix_4x4: np.matrix):
    pos = pr.Vector3(extrinsic_matrix_4x4[0, 3], extrinsic_matrix_4x4[1, 3], extrinsic_matrix_4x4[2, 3])

    rotation_matrix = np.array([0.0, 0.0, 1.0, 0.0,
                                0.0, -1.0, 0.0, 0.0,
                                1.0, 0.0, 0.0, 0.0,
                                0.0, 0.0, 0.0, 1.0]).reshape(4, 4)

    x_dir = np.array([1.0, 0.0, 0.0])
    y_dir = np.array([0.0, 1.0, 0.0])
    z_dir = np.array([0.0, 0.0, 1.0])

    # x_dir = np.array([0.0, 0.0, 1.0])
    # y_dir = np.array([0.0, -1.0, 0.0])
    # z_dir = np.array([1.0, 0.0, 0.0])

    scale = 1.0

    x_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(x_dir, 1.0))
    y_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(y_dir, 1.0))
    z_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(z_dir, 1.0))

    # Draw x-axis
    draw_line_3d(pos, pr.Vector3(x_dir[0], x_dir[1], x_dir[2]), pr.RED)
    # Draw y-axis
    draw_line_3d(pos, pr.Vector3(y_dir[0], y_dir[1], y_dir[2]), pr.GREEN)
    # Draw z-axis
    draw_line_3d(pos, pr.Vector3(z_dir[0], z_dir[1], z_dir[2]), pr.BLUE)


def draw_coordinate_frame_llff(extrinsic_matrix_4x4: np.matrix):
    pos = pr.Vector3(extrinsic_matrix_4x4[0, 3], extrinsic_matrix_4x4[1, 3], extrinsic_matrix_4x4[2, 3])

    x_dir = np.array([0.0, -1.0, 0.0])
    y_dir = np.array([0.0, 0.0, 1.0])
    z_dir = np.array([-1.0, 0.0, 0.0])

    scale = 1.0

    x_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(x_dir, 1.0))
    y_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(y_dir, 1.0))
    z_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(z_dir, 1.0))

    # Draw x-axis
    draw_line_3d(pos, pr.Vector3(x_dir[0], x_dir[1], x_dir[2]), pr.RED)
    # Draw y-axis
    draw_line_3d(pos, pr.Vector3(y_dir[0], y_dir[1], y_dir[2]), pr.GREEN)
    # Draw z-axis
    draw_line_3d(pos, pr.Vector3(z_dir[0], z_dir[1], z_dir[2]), pr.BLUE)


def draw_coordinate_frame_opengl_nerf(extrinsic_matrix_4x4: np.matrix):
    pos = pr.Vector3(extrinsic_matrix_4x4[0, 3], extrinsic_matrix_4x4[1, 3], extrinsic_matrix_4x4[2, 3])

    x_dir = np.array([0.0, 0.0, 1.0])
    y_dir = np.array([0.0, 1.0, 0.0])
    z_dir = np.array([-1.0, 0.0, 0.0])

    scale = 1.0

    x_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(x_dir, 1.0))
    y_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(y_dir, 1.0))
    z_dir = scale * np.matmul(extrinsic_matrix_4x4, np.append(z_dir, 1.0))

    # Draw x-axis
    draw_line_3d(pos, pr.Vector3(x_dir[0], x_dir[1], x_dir[2]), pr.RED)
    # Draw y-axis
    draw_line_3d(pos, pr.Vector3(y_dir[0], y_dir[1], y_dir[2]), pr.GREEN)
    # Draw z-axis
    draw_line_3d(pos, pr.Vector3(z_dir[0], z_dir[1], z_dir[2]), pr.BLUE)
