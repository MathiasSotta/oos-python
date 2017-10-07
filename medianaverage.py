#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Define a function sum() that returns the median and the
# average of all parameters

def sum(numbers):
    fx = 0
    a = 0
    # sort numbers in ascending order
    nsorted = sorted(numbers)
    # get count
    n = nsorted.__len__()

    # get the average without using sum-function
    for i in nsorted:
        a += i
    a = a / n

    # if count of numbers is equal

    if (n % 2) == 0:
        f1 = int(n / 2)
        f2 = int(f1 + 1)
        fx = float(0.5 * (nsorted[f1-1] + nsorted[f2]))
        #print(fx)
        return print("median:",fx,"average:",a)
    else:
        ue = int((n + 1) / 2)
        return print("median =",nsorted[ue-1],"average:",a)

numbers = [ 8, 5, 4, 7, 4, 3, 6, 6, 7, 4, 7, 3 ]
numbers2 = [ 8, 5, 4, 7, 4, 3, 6, 6, 7, 4, 7, 3, 16 ]
print(sum(numbers))