#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Define a function sum() that returns the median and the
# average of all parameters


def sum(numbers):
    a = 0
    # sort numbers in ascending order
    nsorted = sorted(numbers)
    # get count
    n = nsorted.__len__()

    # get the average without using sum-function
    for i in nsorted:
        a += i
    a = a / n

    # case 1: count of numbers is equal
    if (n % 2) == 0:
        f1 = int(n / 2)
        f2 = int(f1 + 1)
        fx = float(0.5 * (nsorted[f1-1] + nsorted[f2]))
        # print(fx)
        return print("median:", fx, "average:", a)
    # case 2: count unequal
    else:
        ue = int((n + 1) / 2)
        return print("median:", nsorted[ue-1], "average:", a)


# testing
numbers = [8, 5, 4, 7, 4, 3, 6, 6, 7, 4, 7, 3]
numbers2 = [8, 5, 4, 7, 4, 11, 6, 6, 18, 4, 7, 3, 16]
sum(numbers)
sum(numbers2)
