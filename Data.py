import pandas

def load_data(path, features):
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
    for feature in features:
        print(feature + ": ", end="")
        for func in statistic_functions:
            formatted_data = "{:.14f}".format(func(data[feature])) if 'mean' in str(func) else "{:.1f}".format(
                func(data[feature])) if 'median' in str(func) else "{:.0f}".format(func(data[feature]))
            if func == statistic_functions[-1]:
                print(func(data[feature]))
            else:
                print(formatted_data + ", ", end="")
