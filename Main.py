import sys
import Data
import Statistics


def main(argv):
    print("Question 1:")
    features = argv[2].split(', ')
    short_features = features[:3]
    statistic_funcs = [Statistics.sum, Statistics.mean, Statistics.median]
    data = Data.load_data(str(argv[1]), features)
    prints_q1('season', 'Summer', short_features, data, statistic_funcs, [1])
    prints_q1('is_holiday', 'Holiday', short_features, data, statistic_funcs, [1])
    print_all(short_features, data, statistic_funcs)
    print("\nQuestion 2:")
    season = 'Winter'
    prints_q2(data, 't1', 13.0, 'cnt', season, statistic_funcs[1:], [determine_season(season)])





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


def prints_q2(data, treatment, threshold, target, description, statistic_funcs, season):
    """
    prints statistics about a given season and threshold
    first print the statistics if above the threshold split by holidays and weekdays
    then does the same for below the threshold
    """
    season_only, _ = Data.filter_by_feature(data, 'season', season)
    weekdays, holidays = Data.filter_by_feature(season_only, 'is_holiday', [0])
    print(f'If {treatment}<={threshold}, then:')
    Statistics.population_statistics(description + ' holiday records:', holidays, treatment, target, threshold, False,
                                     statistic_funcs)
    Statistics.population_statistics(description + ' weekday records:', weekdays, treatment, target, threshold, False,
                                     statistic_funcs)
    print(f'If {treatment}>{threshold}, then:')
    Statistics.population_statistics(description + ' holiday records:', holidays, treatment, target, threshold, True,
                                     statistic_funcs)
    Statistics.population_statistics(description + ' weekday records:', weekdays, treatment, target, threshold, True,
                                     statistic_funcs)


def print_all(short_features, data, statistic_funcs):
    """
    Prints statistics (in this case- sum, mean, median) for each feature in list for the whole year (doesnt depend on another condition as season or holiday)
    :param short_features: list of features to calculate their statistics
    :param data: the dictionary we work with
    :param statistic_funcs: list of statistic types to print
    :return: void
    """
    print("All:")
    Data.print_details(data, short_features, statistic_funcs)


def determine_season(season):
    """
    :return the number of the season based on the csv we were given
    """
    season = season.lower()
    return 1 if "summer" in season else 3 if "winter" in season else 2 if "spring" in season else 0


if __name__ == '__main__':
    main(sys.argv)
