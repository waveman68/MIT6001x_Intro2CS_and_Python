__author__ = 'Sam Broderick'


# define the SimpleDivide function here


def FancyDivide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [SimpleDivide(item, denom)
            for item in list_of_numbers]


def SimpleDivide(item, denom):
    try:
        return_value = item / denom
    except ZeroDivisionError, e:
        return_value = 0
    return return_value


print(FancyDivide([0, 2, 4], 0))
