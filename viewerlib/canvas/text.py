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


def draw_coordinate_label(distance_from_origin: int,
                          font_size: int,
                          camera: pr.Camera3D
                          ):
    x_coord_pos = pr.get_world_to_screen(pr.Vector3(distance_from_origin, 0, 0), camera)
    y_coord_pos = pr.get_world_to_screen(pr.Vector3(0, distance_from_origin, 0), camera)
    z_coord_pos = pr.get_world_to_screen(pr.Vector3(0, 0, distance_from_origin), camera)
    pr.draw_text("x", int(x_coord_pos.x), int(x_coord_pos.y), font_size, pr.BLACK)
    pr.draw_text("y", int(y_coord_pos.x), int(y_coord_pos.y), font_size, pr.BLACK)
    pr.draw_text("z", int(z_coord_pos.x), int(z_coord_pos.y), font_size, pr.BLACK)
