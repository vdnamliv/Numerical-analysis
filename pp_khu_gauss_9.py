import numpy as np

def solve_system(a):
  """
  Analyzes and solves the linear system for a given value of 'a'.

  Args:
      a: The value of 'a' for which to analyze and solve the system.

  Returns:
      A tuple containing (has_solution, solution) where:
          - has_solution: True if a solution exists, False otherwise.
          - solution: A numpy array containing the solution (x1, x2) if a solution exists, None otherwise.
  """
  coefficient_matrix = np.array([[2, -6*a], [3*a, -1]])
  constant_vector = np.array([3, 3/2])

  # Check if determinant is zero (infinite solutions or no solution)
  determinant = np.linalg.det(coefficient_matrix)
  if abs(determinant) < 1e-6:
    if np.allclose(coefficient_matrix.dot(constant_vector), np.zeros(2)):
      return (True, np.inf)  # Infinite solutions
    else:
      return (False, None)  # No solution
  
  # Solve the system using inverse
  solution = np.linalg.inv(coefficient_matrix).dot(constant_vector)
  return (True, solution)

# Analyze and solve for different values of 'a'
def analyze_and_solve(a_values):
  for a in a_values:
    has_solution, solution = solve_system(a)
    if has_solution:
      if solution is np.inf:
        print(f"For a = {a}: Infinite number of solutions")
      else:
        print(f"For a = {a}: Solution (x1, x2) = {solution}")
    else:
      print(f"For a = {a}: No solution")

a_values = [1, 2, 1/3]  # Test cases for different values of 'a'
analyze_and_solve(a_values)
