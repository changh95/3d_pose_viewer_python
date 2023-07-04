import pyray as pr
import numpy as np


def draw_line_3d_np(
        start_position: np.array,
        end_position: np.array,
        color: pr.Color
):
    draw_line_3d(
        pr.Vector3(start_position[0], start_position[1], start_position[2]),
        pr.Vector3(end_position[0], end_position[1], end_position[2]),
        color
    )


def draw_line_3d(
        start_position: pr.Vector3,
        end_position: pr.Vector3,
        color: pr.Color
):
    pr.draw_line_3d(start_position, end_position, color)


def draw_point_3d_np(
        position: np.array,
        color: pr.Color
):
    pr.draw_point_3d(
        pr.Vector3(position[0], position[1], position[2]),
        color)


def draw_point_3d(
        position: pr.Vector3,
        color: pr.Color
):
    pr.draw_point_3d(position, color)


def draw_sphere_np(
        position: np.array,
        radius: float,
        color: pr.Color
):
    pr.draw_sphere(
        pr.Vector3(position[0], position[1], position[2]),
        radius,
        color
    )

def draw_sphere(
        position: pr.Vector3,
        radius: float,
        color: pr.Color
):
    pr.draw_sphere(position, radius, color)

def draw_grid(
        slices: int,
        spacing: float
):
    pr.draw_grid(slices, spacing)

# TODO: Replace draw_grid by the new function
# def draw_grid(
#         screen_width: int,
#         screen_height: int,
#         spacing: float
# ):
#     # pr.draw_grid(slices, spacing)
#
#     # Draw the grid lines
#     half_screen_width = int(screen_width * 0.5)
#     for x in range(-half_screen_width, half_screen_width, int(spacing)):
#         pr.draw_line(x, 0, x, 720, pr.BLACK)
#     for y in range(-half_screen_width, half_screen_width, int(spacing)):
#         pr.draw_line(0, y, 720, y, pr.BLACK)
