from math import ceil


class Statistics:

    def sum(values):

        total = 0
        for num in values:
            total += num
        return total

    def mean(values):

        total = sum(values)
        length = len(values)
        return (total/length)