import sys
import Data
from Statistics import population_statistics as pop_stats
import Statistics


def main(argv):
    """
    answers questions 1 and 2 using modules Data.py and Statistics.py
    :param argv: argv[0]=path to main.py  argv[1]=path to csv file  argv[2]=string containing list of features in csv
    :return: void
    """
    print("Question 1:")
    features = argv[2].split(', ')
    short_features = features[:3]
    statistic_funcs = [Statistics.sum, Statistics.mean, Statistics.median]
    data = Data.load_data(str(argv[1]), features)
    prints_q1('season', 'Summer', short_features, data, statistic_funcs, [1])  # #print data for summer
    prints_q1('is_holiday', 'Holiday', short_features, data, statistic_funcs, [1])  # #print data for holidays
    print_all(short_features, data, statistic_funcs)  # #print data of the whole year
    print("\nQuestion 2:")
    prints_q2(data, 't1', 13.0, 'cnt', 'Winter', statistic_funcs[1:])  # #answer question 2


def prints_q1(feature, title, short_features, data, statistic_funcs, values):
    """
    Prints statistics (in this case- sum, mean, median) for each feature in list for specific value of another feature
    :param feature: the feature which its value makes the results being printed or not
    :param title: declare what feature value we depend on
    :param short_features: list of features to calculate their statistics
    :param data: the dictionary we work with
    :param statistic_funcs: list of statistic types to print
    :param values: the value of 'feature' to make the data being counted or not
    :return: void
    """
    data1, data2 = Data.filter_by_feature(data, feature, values)
    print(title + ":")
    Data.print_details(data1, short_features, statistic_funcs)


def prints_q2(data, treatment, threshold, target, description, statistic_funcs):
    """
    prints statistics for a given season.
    first print the statistics for all entries above the given threshold split by holidays and weekdays
    then does the same for all entries below the threshold
    :param data: dictionary we work with
    :param treatment: the feature which its value will be evaluated to the threshold
    :param threshold: the threshold
    :param target: the feature for which entries will be calculated and printed
    :param description: declare which season we look for records
    :param statistic_funcs: list of statistic types to print
    :return: void
    """
    season_only, _ = Data.filter_by_feature(data, 'season', [determine_season(description)])
    weekdays, holidays = Data.filter_by_feature(season_only, 'is_holiday', [0])
    print(f'If {treatment}<={threshold}, then:')
    pop_stats(description + ' holiday records:', holidays, treatment, target, threshold, False, statistic_funcs)
    pop_stats(description + ' weekday records:', weekdays, treatment, target, threshold, False, statistic_funcs)
    print(f'If {treatment}>{threshold}, then:')
    pop_stats(description + ' holiday records:', holidays, treatment, target, threshold, True, statistic_funcs)
    pop_stats(description + ' weekday records:', weekdays, treatment, target, threshold, True, statistic_funcs)


def print_all(short_features, data, statistic_funcs):
    """
    Prints statistics (in this case- sum, mean, median) for each feature in list for the whole year
    (doesnt depend on another condition as season or holiday)
    :param short_features: list of features to calculate their statistics
    :param data: the dictionary we work with
    :param statistic_funcs: list of statistic types to print
    :return: void
    """
    print("All:")
    Data.print_details(data, short_features, statistic_funcs)


def determine_season(season):
    """
    translate the name of the season to the numeric value it has in the csv
    :param season: name of the season
    :return: the number of the season based on the csv we were given
    """
    season = season.lower()
    return 1 if "summer" in season else 3 if "winter" in season else 2 if "spring" in season else 0


if __name__ == '__main__':
    main(sys.argv)
