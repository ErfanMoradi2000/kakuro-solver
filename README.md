# kakuro-solver

  This project provides a Python-based solver for Kakuro puzzles using Constraint Satisfaction Problems (CSP) techniques.

  The Kakuro Solver employs backtracking in conjunction with forward checking for efficient pruning of the search space. It works as follows:
  
  Backtracking: A recursive algorithm for finding all solutions to the puzzle by exploring the space of potential solutions incrementally, one component at a time, and abandoning components that could not possibly lead to a viable solution (backtrack).
  
  Forward Checking: As the algorithm assigns values to the puzzle, forward checking looks ahead to constrain the legal values of neighboring cells to avoid future conflicts. This reduces the need for backtracking and speeds up the search for a solution.
  
  Consistency Checking: Each assignment is checked for consistency against the constraints of the Kakuro puzzle. It ensures that no two cells in a sum-group have the same number and that sum constraints of each sum-group are not exceeded.
