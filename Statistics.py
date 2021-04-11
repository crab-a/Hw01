from math import ceil
from Data import print_details as print_data


def sum(values):
    """
    calculate the sum of all values in the iterable 'values'
    :param values: iterable containing numbers(int/float/double)
    :return: the sum
    """
    total = 0
    for num in values:
        total += num
    return total


def mean(values):
    """
    calculate the mean of all values in the iterable 'values'
    :param values: iterable containing numbers(int/float/double)
    :return: the mean
    """
    total = sum(values)
    length = len(values)
    return total / length


def median(values):
    """
    calculate the median of all values in the iterable 'values'
    :param values: iterable containing numbers(int/float/double)
    :return: the median
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
    :param feature_description: description to be displayed
    :param data: dictionary we work with
    :param treatment: what parameter the threshold refers to
    :param target: which feature we look for in the data
    :param threshold: the threshold
    :param is_above: if True the func calculate  above the threshold
    :param statistic_functions: list of functions to be used
    :return: void
    """
    above, below = filter_by_treatment(data, treatment, threshold)
    data_clean = above if is_above else below
    print_details(feature_description, data_clean, target, statistic_functions)


def filter_by_treatment(data, treatment, threshold):
    """
    split the data based on given threshold about a feature(treatment)
    :param data: dictionary we work with
    :param treatment: what parameter the threshold refers to
    :param threshold: the threshold
    :return: two dictionary: the first with all entries surpassing the threshold, the second we all entries equals or below the threshold
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
    """
    handle printing according to format
    :param feature_description: description to be printed
    :param data: dictionary we work with
    :param target: the feature we looked the statistics for
    :param statistic_functions: list of functions to be used
    :return: void
    """
    print(feature_description)
    temp_features = [target]
    print_data(data, temp_features, statistic_functions)
