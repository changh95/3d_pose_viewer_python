import numpy as np
from scipy.linalg import logm, expm


def average_pose(pose1: np.matrix,
                 pose2: np.matrix):
    """
    Average two poses
    :param pose1: 4x4 pose matrix
    :param pose2: 4x4 pose matrix
    :return: Averaged pose
    """
    rotation_matrix1 = pose1[:3, :3]
    rotation_matrix2 = pose2[:3, :3]
    averaged_rotation_matrix = average_rotation(rotation_matrix1, rotation_matrix2)

    position1 = pose1[:3, 3]
    position2 = pose2[:3, 3]
    averaged_position = average_position(position1, position2)

    averaged_pose = np.eye(4)
    averaged_pose[:3, :3] = averaged_rotation_matrix
    averaged_pose[:3, 3] = averaged_position

    return averaged_pose


def average_rotation(rotation_matrix1: np.matrix,
                     rotation_matrix2: np.matrix):
    """
    Average two rotation matrices, by making them rotation vectors and averaging them.
    :param rotation_matrix1: 3x3 rotation matrix
    :param rotation_matrix2: 3x3 rotation matrix
    :return: Averaged rotation matrix
    """

    log_matrix1 = logm(rotation_matrix1)
    log_matrix2 = logm(rotation_matrix2)

    average_log_matrix = 0.5 * (log_matrix1 + log_matrix2)

    return expm(average_log_matrix)


def average_position(position1: np.array,
                    position2: np.array):
    """
    Average two positions.
    :param position1: 3x1 position vector
    :param position2: 3x1 position vector
    :return: Averaged position vector
    """
    return 0.5 * (position1 + position2)


def quaternion_slerp(quaternion1, quaternion2, t):
    dot_product = np.dot(quaternion1, quaternion2)

    # If the dot product is negative, invert one of the quaternions
    if dot_product < 0.0:
        quaternion1 *= -1

    result_quaternion = np.empty(4)
    np.multiply(quaternion1, 1 - t, out=result_quaternion)
    np.multiply(quaternion2, t, out=result_quaternion, where=quaternion2 != quaternion1)

    return result_quaternion / np.linalg.norm(result_quaternion)
