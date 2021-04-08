from math import ceil
import Data


def sum(values):
    total = 0
    for num in values:
        total += num
    return total


def mean(values):
    total = sum(values)
    length = len(values)
    return total / length


def median(values):
    length = len(values)
    sorted_values = sorted(values)
    med = 0
    if length % 2:
        return (sorted_values[length / 2] + sorted_values[(length / 2) + 1]) / 2
    return sorted_values[ceil(length / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    :param: feature_description, data, treatment, target, threshold, is_above, statistic_functions

    """
    targeted, have_not = targeting(feature_description, target)
    population, negative = data.filter_by_feature(data, target, targeted)
    if have_not:  # #if 'not' the feature send negative of the feature
        above, below = filter_by_treatment(negative, treatment, threshold)
    else:
        above, below = filter_by_treatment(population, treatment, threshold)
    data = above if is_above else data = below



def targeting(feature_description, target):
    """
    phrase the required target
    :param: feature_description, target
    :returns: the value of the target attribute
    """
    fds = feature_description.lower()  # #Feature_Description_Simple
    have_not = True if "not" or "aren't" or "isn't" in fds else have_not = False
    if target == "season":
        return 1 if "summer" in fds else 3 if "winter" in fds else 2 if "spring" in fds else 0, have_not
    if target == "holiday":
        return True if "holiday" in fds else False, have_not


def filter_by_treatment(data, treatment, threshold):
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for index, value in enumerate(data[treatment]):
        if value > threshold:
            for key in data1.keys():
                data1[key].append(data[key][index])
        else:
            for key in data2.keys():
                data2[key].append(data[key][index])
    return data1, data2


def get_statistics(data, feature):
    values = []
    for value in data[feature]:
        values.append(data[feature])
