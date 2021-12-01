def fibonacci(n):
    '''this function recreates the fibonacci math equation
    it is a series of numbers which each number is the sum of the
    two preceding numbers'''
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n -2)

def lucas(n):
    '''this function recreates lucas numbers, closely related to fibonacci'''
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, first = 0, second = 1):
    '''returns the nth number in the series created by summing previous two numbers.
    also accepts two parameters representing first two numbers in the series.'''
    if n == 0:
        return first
    if n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n -2, first, second)