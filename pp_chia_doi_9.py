import numpy as np

def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

def bisection_method(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("The function must have different signs at the endpoints a and b.")
    
    iteration = 0
    while (b - a) / 2 > tol and iteration < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
    
    return (a + b) / 2

# Find the root in the interval [0.5, 1.5]
root = bisection_method(f, 0.5, 1.5)
print(f"The root is approximately at x = {root:.5f}")
