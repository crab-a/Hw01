from math import ceil
from Data import print_details as print_data


def sum(values):
    """
    :return
    the sum of iterable
    """
    total = 0
    for num in values:
        total += num
    return total


def mean(values):
    """
    :return
    the mean of iterable
    """
    total = sum(values)
    length = len(values)
    return total / length


def median(values):
    """
    :return
    the median of iterable
    """
    length = len(values)
    sorted_values = sorted(values)
    med = 0
    if length % 2:
        return sorted_values[int(length / 2)]
    return (sorted_values[int(length / 2)] + sorted_values[int((length / 2)) + 1]) / 2


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    prints the statistics for given feature(target) with care for given threshold about given feature(treatment)
    :param:
    feature_description = description to be displayed,
    data,
    treatment = what parameter the threshold refers to
    target = which feature we look for in the data
    threshold,
    is_above = if True the func calculate  above the threshold,
    statistic_functions = list of functions to be used,
    """
    above, below = filter_by_treatment(data, treatment, threshold)
    data_clean = above if is_above else below
    print_details(feature_description, data_clean, target, statistic_functions)


def filter_by_treatment(data, treatment, threshold):
    """
    split the data based on given threshold about a feature(treatment)
    :param:
    data,
    treatment,
    threshold,
    :return:
    two dict: one with all values above the threshold the other with the rest (below and equal)
    """
    above = {}
    below = {}
    for key in data.keys():
        above[key] = []
        below[key] = []
    for index, value in enumerate(data[treatment]):
        if value > threshold:
            for key in above.keys():
                above[key].append(data[key][index])
        else:
            for key in below.keys():
                below[key].append(data[key][index])
    return above, below


def print_details(feature_description, data, target, statistic_functions):
    """handle printing according to format"""
    print(feature_description)
    temp_features = [target]
    print_data(data, temp_features, statistic_functions)
