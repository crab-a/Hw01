import sys
import Data
import Statistics
import pandas


def main(argv):
    print("Question 1:")
    features = ['hum', 't1', 'cnt', 'season', 'is_holiday']
    short_features = features[:3]
    statistic_funcs = [Statistics.sum, Statistics.mean, Statistics.median]
    data = Data.load_data("london_sample.csv", features)
    prints('season', 'Summer', short_features, data, statistic_funcs, [1])
    prints('is_holiday', 'Holiday', short_features, data, statistic_funcs, [1])
    print_all(short_features, data, statistic_funcs)





# def...
def prints(feature, title, short_features, data, statistic_funcs, values):
    data1, data2 = Data.filter_by_feature(data, feature, values)
    print(title+":")
    Data.print_details(data1, short_features, statistic_funcs)


def print_all(short_features, data, statistic_funcs):
    print("All:")
    Data.print_details(data, short_features, statistic_funcs)


if __name__ == '__main__':
    main(sys.argv)
