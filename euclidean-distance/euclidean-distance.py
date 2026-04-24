import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    sum = 0
    if len(x) != len(y):
        raise ValueError("Vectors must be of same length")
    for i in range (len(x)):
        sum = sum + pow((x[i]-y[i]),2)

    return pow(sum,0.5)