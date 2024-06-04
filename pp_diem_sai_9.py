def false_position(f, a, b, tolerance=1e-4):
  """
  Finds a solution to f(x) = 0 using the False Position method within a tolerance.

  Args:
      f: The function for which to find the root.
      a: Lower bound of the interval.
      b: Upper bound of the interval.
      tolerance: The desired accuracy of the solution.

  Returns:
      An approximation to the root of f(x) = 0, accurate to within the tolerance.
  """
  while abs(b - a) > tolerance:
    fa = f(a)
    fb = f(b)
    if fa * fb < 0:
      new_root = a - fa * (b - a) / (fb - fa)
    else:
      raise ValueError("Function signs must have opposite signs at initial bounds.")
    if abs(f(new_root)) < tolerance:
      return new_root
    elif f(new_root) * fa < 0:
      b = new_root
    else:
      a = new_root
  return (a + b) / 2  # Handle cases where interval becomes very small

# Define functions for each problem
def f1(x):
  return x**3 - 2*x**2 - 5

def f2(x):
  return x**3 + 3*x**2 - 1

def f3(x):
  return x - math.cos(x)

def f4(x):
  return x - 0.8 - 0.2 * math.sin(x)

import math

# Solve each problem

# a) x^3 - 2x^2 - 5 = 0, [1,4]
root_a = false_position(f1, 1, 4)
print(f"Root of x^3 - 2x^2 - 5 (a): {root_a:.4f}")

# b) x^3 + 3x^2 - 1 = 0, [-3,-2]
root_b = false_position(f2, -3, -2)
print(f"Root of x^3 + 3x^2 - 1 (b): {root_b:.4f}")

# c) x - cos x = 0, [0,pi/2] (use math.cos for cosine)
root_c = false_position(f3, 0, math.pi/2)
print(f"Root of x - cos(x) = 0 (c): {root_c:.4f}")

# d) x - 0.8 - 0.2 * sin x = 0, [0, pi/2] (use math.sin for sine)
root_d = false_position(f4, 0, math.pi/2)
print(f"Root of x - 0.8 - 0.2sin(x) = 0 (d): {root_d:.4f}")
