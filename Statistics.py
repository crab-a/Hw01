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
    sorted_vals = sorted(values)
    med = 0
    if length % 2:
        return (sorted_vals[length / 2] + sorted_vals[(length / 2) + 1]) / 2
    return sorted_vals[ceil(length / 2)]


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
    :param: feature_description, data, treatment, target, threshold, is_above, statistic_functions

    """
    targeted, have_not = targeting(feature_description, target)  # #neccesarly categorical??
    population, negative = Data.filter_by_feature(data, target, targeted)
    treated, _ = targeting(feature_description, treatment)  # #need to see how to deal if more then one number
# #here i add the modifid version of filter_by_feature with thershold as value and treated param
    if is_above:
        pass  # #use it to choose if above or under


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
