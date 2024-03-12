"""
Design a function that takes a list of numerical data and performs calculations
for mean, median and standard deviation.
Write unit tests to verify the correctness of the statistical calculations
for various inputs, including edge cases like an empty list or a list with one element  (Use unittest module).
"""

import math


def calculate_stats(data):
    """
    Calculate mean, median, and standard deviation of a list of numerical data.

    Args:
    data (list): A list of numerical data.

    Returns:
    tuple: A tuple containing the mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("Empty List")

    if len(data) == 1:
        raise ValueError("Only one elemt in the List")

    data = sorted(data)
    n = len(data)
    mean = sum(data) / n

    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)

    return (mean, median,std_dev)

# print(calculate_stats([40, 72, 93, 0, 16, 23, 21, 16]))