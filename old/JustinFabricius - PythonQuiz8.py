import math
import statistics
import calendar

num_list = [66, 88, 99, 44, 55, 22]


def gcdOfList(list_numbers: list):
    gcd = math.gcd(max(list_numbers), min(list_numbers))
    print("The greatest common divisor of the smallest and largest number from the given list is:", gcd)


def powAllListElements(list_numbers: list, power: int = 1):
    print("For every single element in the list, i apply the math.pow operation, i put that in a list then print it.")
    print(list(map(lambda x: math.pow(x, power), list_numbers)))


def stats(numlist: list):
    print("This function prints out the mean, median, standard deviation and variance of a dataset")
    print("Mean is:", statistics.mean(numlist))
    print("Median is:", statistics.median(numlist))
    print("Standard Deviation is:", statistics.stdev(numlist))
    print("Variance is:", statistics.variance(numlist))


def birthday(year: int, month: int, day: int):
    print(calendar.weekday(year, month, day))


def combined(numlist: list):
    # Prints out various statistics from a list
    stats(numlist)
    print()
    # Finds the GCD between the lowest and highets value in a given list
    gcdOfList(numlist)
    print()
    # I choose to square all elements
    powAllListElements(numlist)

combined(num_list)

# print(mathStuff())
# gcdOfList(numlist)
# stats(numlist)
