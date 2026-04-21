import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    a = len(A)
    b = len(A[0])
    B = np.zeros((b,a))
    for i in range(a):
        for j in range(b):
            B[j][i]=A[i][j]

    return B