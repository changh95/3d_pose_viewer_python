import pyray as pr


def draw_text(
        text: str,
        position_x: int,
        position_y: int,
        font_size: int,
        color: pr.Color
):
    pr.draw_text(text, position_x, position_y, font_size, color)


def draw_fps(position_x: int,
             position_y: int
):
    pr.draw_fps(position_x, position_y)
