import sys
import Data
import Statistics


def main(argv):
    print("Question 1:")
    features = ['hum', 't1', 'cnt', 'season', 'is_holiday']
    short_features = features[:3]
    statistic_funcs = [Statistics.sum, Statistics.mean, Statistics.median]
    data = Data.load_data("london_sample.csv", features)
    prints_q1('season', 'Summer', short_features, data, statistic_funcs, [1])
    prints_q1('is_holiday', 'Holiday', short_features, data, statistic_funcs, [1])
    print_all(short_features, data, statistic_funcs)
    print("Question 2:")
    treatment, threshold, target, season = 't', 13.0, 'cnt', 'Winter'
    prints_q2(data, treatment, threshold, target, season, statistic_funcs[1:])


# def...


def prints_q1(feature, title, short_features, data, statistic_funcs, values):
    data1, data2 = Data.filter_by_feature(data, feature, values)
    print(title + ":")
    Data.print_details(data1, short_features, statistic_funcs)


def prints_q2(data, treatment, threshold, target, season, statistic_funcs):
    seasoned = season.lower()
    seasoned = 1 if "summer" in seasoned else 3 if "winter" in seasoned else 2 if "spring" in seasoned else 0
    season_only, _ = Data.filter_by_feature(data, season, seasoned)
    weekdays, holidays = Data.filter_by_feature(season_only, 'is_holiday', 0)
    print(f'If {treatment}<={threshold}, then:')
    Statistics.population_statistics(season + 'holiday records', holidays, treatment, target, threshold, False,
                                     statistic_funcs)
    Statistics.population_statistics(season + 'weekday records', weekdays, treatment, target, threshold, False,
                                     statistic_funcs)
    print(f'If {treatment}>{threshold}, then:')
    Statistics.population_statistics(season + 'holiday records', holidays, treatment, target, threshold, True,
                                     statistic_funcs)
    Statistics.population_statistics(season + 'weekday records', weekdays, treatment, target, threshold, True,
                                     statistic_funcs)


def print_all(short_features, data, statistic_funcs):
    print("All:")
    Data.print_details(data, short_features, statistic_funcs)


if __name__ == '__main__':
    main(sys.argv)
