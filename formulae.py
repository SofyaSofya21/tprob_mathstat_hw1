import numpy as np
from math import factorial

def combinations(n,k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n-k))

def arrangements(n,k):
    return np.math.factorial(n) // np.math.factorial(n-k)

def permutation(n):
    return np.math.factorial(n)

def bayesformula(p_a_b, p_b, p_a):
    return p_a_b*p_b/p_a

def probability(m,n):
    return m/n