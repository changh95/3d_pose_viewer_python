from .primitive_geometry_3d import *
import pyray as pr

from enum import Enum

class PoseConvention(Enum):
    OPENCV = 0
    LLFF = 1
    OPENGL = 2


def draw_coordinate_frame(position_3d: pr.Vector3,
                          rotation_3d: pr.Vector3,
                          pose_convention: PoseConvention
                          ):
    if pose_convention == PoseConvention.OPENCV:
        draw_coordinate_frame_opencv(position_3d, rotation_3d)
    elif pose_convention == PoseConvention.LLFF:
        draw_coordinate_frame_llff(position_3d, rotation_3d)
    elif pose_convention == PoseConvention.OPENGL:
        draw_coordinate_frame_opengl(position_3d, rotation_3d)


def draw_coordinate_frame_opencv(position_3d: pr.Vector3,
                                 rotation_3d: pr.Vector3
                                 ):
    # Draw x-axis
    draw_line_3d(position_3d, pr.Vector3(position_3d.x + 1.0, position_3d.y + 0.0, position_3d.z + 0.0), pr.RED)
    # Draw y-axis
    draw_line_3d(position_3d, pr.Vector3(position_3d.x + 0.0, position_3d.y + 1.0, position_3d.z + 0.0), pr.GREEN)
    # Draw z-axis
    draw_line_3d(position_3d, pr.Vector3(position_3d.x + 0.0, position_3d.y + 0.0, position_3d.z + 1.0), pr.BLUE)


def draw_coordinate_frame_llff(position_3d: pr.Vector3,
                               rotation_3d: pr.Vector3
                               ):
    # Draw x-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(1.0, 0.0, 0.0), pr.RED)
    # Draw y-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(0.0, 0.0, 1.0), pr.GREEN)
    # Draw z-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(0.0, 1.0, 0.0), pr.BLUE)


def draw_coordinate_frame_opengl(position_3d: pr.Vector3,
                                 rotation_3d: pr.Vector3
                                 ):
    # Draw x-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(1.0, 0.0, 0.0), pr.RED)
    # Draw y-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(0.0, 1.0, 0.0), pr.GREEN)
    # Draw z-axis
    draw_line_3d(position_3d, position_3d + pr.Vector3(0.0, 0.0, 1.0), pr.BLUE)
