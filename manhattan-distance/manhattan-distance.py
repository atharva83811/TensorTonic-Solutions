import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    sum = 0
    for i in range (len(x)):
        sum = sum + abs(x[i]-y[i])

    return sum