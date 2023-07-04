import numpy as np


def rotate_around_x(rotation_matrix: np.matrix,
                    angle: float):
    """
    Rotate a rotation matrix around the x-axis
    :param rotation_matrix: 3x3 rotation matrix
    :param angle: Angle in radians
    :return: Rotated rotation matrix
    """

    return np.matmul(rotation_matrix, np.array([[1, 0, 0],
                                                [0, np.cos(angle), -np.sin(angle)],
                                                [0, np.sin(angle), np.cos(angle)]]))


def rotate_around_local_x(rotation_matrix: np.matrix,
                          angle: float):
    """
    Rotate a rotation matrix around the x-axis
    :param rotation_matrix: 3x3 rotation matrix
    :param angle: Angle in radians
    :return: Rotated rotation matrix
    """

    return np.matmul(np.array([[1, 0, 0],
                               [0, np.cos(angle), -np.sin(angle)],
                               [0, np.sin(angle), np.cos(angle)]]), rotation_matrix)


def rotate_around_y(rotation_matrix: np.matrix,
                    angle: float):
    """
    Rotate a rotation matrix around the y-axis
    :param rotation_matrix: 3x3 rotation matrix
    :param angle: Angle in radians
    :return: Rotated rotation matrix
    """

    return np.matmul(rotation_matrix, np.array([[np.cos(angle), 0, np.sin(angle)],
                                                [0, 1, 0],
                                                [-np.sin(angle), 0, np.cos(angle)]]))


def rotate_around_local_y(rotation_matrix: np.matrix,
                          angle: float):
    """
    Rotate a rotation matrix around the y-axis
    :param rotation_matrix: 3x3 rotation matrix
    :param angle: Angle in radians
    :return: Rotated rotation matrix
    """

    return np.matmul(np.array([[np.cos(angle), 0, np.sin(angle)],
                               [0, 1, 0],
                               [-np.sin(angle), 0, np.cos(angle)]]), rotation_matrix)


def rotate_around_z(rotation_matrix: np.matrix,
                    angle: float):
    """
    Rotate a rotation matrix around the z-axis
    :param rotation_matrix: 3x3 rotation matrix
    :param angle: Angle in radians
    :return: Rotated rotation matrix
    """

    return np.matmul(rotation_matrix, np.array([[np.cos(angle), -np.sin(angle), 0],
                                                [np.sin(angle), np.cos(angle), 0],
                                                [0, 0, 1]]))


def rotate_around_local_z(rotation_matrix: np.matrix,
                            angle: float):
        """
        Rotate a rotation matrix around the z-axis
        :param rotation_matrix: 3x3 rotation matrix
        :param angle: Angle in radians
        :return: Rotated rotation matrix
        """

        return np.matmul(np.array([[np.cos(angle), -np.sin(angle), 0],
                                 [np.sin(angle), np.cos(angle), 0],
                                 [0, 0, 1]]), rotation_matrix)
