import pandas
class Data:
    def load_data(path, features):
        df = pandas.read_csv(path)
        data = df.to_dict(orient="list")
        return data

    def filter_by_feature(data, feature, values):
