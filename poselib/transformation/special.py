from .transform import *
from .interpolation import *
from .convert import *
import copy
import numpy as np
from scipy.spatial.transform import Rotation, Slerp


def generate_spiral_motion(poses: list[np.matrix],
                           pitch_angle: float,
                           num_interpolation_between_spiral_endpoints: int):
    """
    Generate a spiral motion from a list of poses
    :param poses: 4x4 pose matrices
    :param pitch_angle: Pitch angle in radians
    :return: List of 4x4 pose matrices
    """
    new_poses = copy.deepcopy(poses)

    spiral_transformations = []
    spiral_LUT = generate_spiral_endpoints_LUT(pitch_angle)

    if num_interpolation_between_spiral_endpoints > 0:
        while len(spiral_transformations) < len(new_poses):
            for i in range(len(spiral_LUT)-1):
                rot12 = Rotation.from_matrix([spiral_LUT[i][:3, :3], spiral_LUT[i + 1][:3, :3]])

                slerp = Slerp([0, num_interpolation_between_spiral_endpoints + 1], rot12)
                times = np.linspace(0, num_interpolation_between_spiral_endpoints + 1, num_interpolation_between_spiral_endpoints + 2)
                interp_rots = slerp(times)

                for j in range(len(interp_rots)):
                    if len(spiral_transformations) >= len(new_poses):
                        break

                    pose = np.identity(4)
                    pose[:3, :3] = interp_rots[j].as_matrix()
                    spiral_transformations.append(pose)
    else:
        for i in range(len(new_poses)):
            spiral_transformations.append(spiral_LUT[i % len(spiral_LUT)])

    # Apply the spiral transformations to the poses
    for i in range(len(new_poses)):
        new_poses[i] = new_poses[i] @ spiral_transformations[i]

    return new_poses


def generate_spiral_endpoints_LUT(angle: float):
    """
    Generate a lookup table for 8 spiral endpoints, each representing N, NE, E, SE, S, SW, W, NW
    :param angle: Pitch angle in radians
    :return: List of 4x4 pose matrices
    """

    endpoints = []

    # N
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_y(pose[:3, :3], angle)
    endpoints.append(pose)

    # NE
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_local_y(rotate_around_x(pose.copy()[:3, :3], -angle), angle)
    endpoints.append(pose)

    # E
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_x(pose.copy()[:3, :3], -angle)
    endpoints.append(pose)

    # SE
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_local_y(rotate_around_x(pose.copy()[:3, :3], -angle), -angle)
    endpoints.append(pose)

    # S
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_y(pose[:3, :3], -angle)
    endpoints.append(pose)

    # SW
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_local_y(rotate_around_x(pose.copy()[:3, :3], angle), -angle)
    endpoints.append(pose)

    # W
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_x(pose.copy()[:3, :3], angle)
    endpoints.append(pose)

    # NW
    pose = np.identity(4)
    pose[:3, :3] = rotate_around_local_y(rotate_around_x(pose.copy()[:3, :3], angle), angle)
    endpoints.append(pose)

    return endpoints
