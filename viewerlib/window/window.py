from .config import WindowConfig
import pyray as pr


def close_window():
    pr.close_window()


class Window:
    def __init__(self,
                 window_config: WindowConfig
                 ):
        self.width = window_config.width
        self.height = window_config.height
        self.window_name = window_config.window_name
        self.target_fps = window_config.target_fps

        pr.init_window(self.width, self.height, self.window_name)
        pr.set_target_fps(self.target_fps)
