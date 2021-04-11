import pandas

def load_data(path, features):
    """
    gets the whole dictionary from csv file and removes the columns that we dont need
    :param path: the location of the csv file
    :param features: a list of features which we need their data
    :return: the new dictionary, which we will work with
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    del_list = []
    for key in data.keys():
        if key not in features:
            del_list.append(key)
    for i in del_list:
        data.pop(i)
    return data


def filter_by_feature(data, feature, values):
    """
    divides a dictionary to 2 different dictionaries according certain list of values of specific feature
    :param data: the dictionary to divide
    :param feature: the feature to which we need to divide the dictionary according its value
    :param values: a list of values (if 'feature' get value in this list- the row copied to 'data1'. else- the row copied to 'data2')
    :return: 2 different dictionaries (data1, data2)
    """
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for index, value in enumerate(data[feature]):
        if value in values:
            for key in data1.keys():
                data1[key].append(data[key][index])
        else:
            for key in data2.keys():
                data2[key].append(data[key][index])
    return data1, data2


def print_details(data, features, statistic_functions):
    """
    Prints statistics (in this case- sum, mean, median) for each feature in list
    :param data: the dictionary to print the statistics about
    :param features: the features to print the statistics for each of them
    :param statistic_functions: list of statistic types to print
    :return: void
    """
    for feature in features:
        print(feature + ": ", end="")
        for func in statistic_functions:
            formatted_data = "{:.14f}".format(func(data[feature])) if 'mean' in str(func) else "{:.1f}".format(
                func(data[feature])) if 'median' in str(func) else "{:.0f}".format(func(data[feature]))
            if func == statistic_functions[-1]:
                print(func(data[feature]))
            else:
                print(formatted_data + ", ", end="")
