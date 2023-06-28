import pyray as pr


def draw_line_3d(
        start_position: pr.Vector3,
        end_position: pr.Vector3,
        color: pr.Color
):
    pr.draw_line_3d(start_position, end_position, color)


def draw_point_3d(
        position: pr.Vector3,
        color: pr.Color
):
    pr.draw_point_3d(position, color)


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
