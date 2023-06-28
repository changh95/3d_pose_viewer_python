import dataclasses


@dataclasses.dataclass
class WindowConfig:
    width: int
    height: int
    window_name: str
    target_fps: int
