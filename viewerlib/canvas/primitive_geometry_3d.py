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
