# Simplex Algorithms

A Python implementation of linear programming optimization algorithms, including the standard Simplex method and the Big-M method for solving linear programming problems.

## Overview

This repository contains implementations of two fundamental algorithms used in operations research and optimization:

- **Standard Simplex Algorithm** (`Simplex.py`) - For solving linear programming problems in standard form
- **Big-M Method** (`Big M Simplex.py`) - For solving LP problems with constraints requiring artificial variables

## What is the Simplex Algorithm?

The **Simplex algorithm** is an iterative method for solving linear programming (LP) problems. It was developed by George Dantzig in 1947 and remains one of the most efficient algorithms for solving LP problems in practice.

The algorithm works by:
1. Converting the LP problem to **slack form**
2. Moving from one **basic feasible solution** to an adjacent one
3. Improving the objective function at each step
4. Terminating when no further improvement is possible (optimal solution found)

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Tableau** | A matrix representation of the LP problem |
| **Pivot** | The process of exchanging a basic and non-basic variable |
| **Slack Variables** | Convert ≤ constraints to equalities |
| **Artificial Variables** | Added for ≥ or = constraints (Big-M method) |
| **Optimality Condition** | All coefficients in the objective row are non-negative |

## Files

### `Simplex.py`

Standard Simplex algorithm implementation. Currently includes a hardcoded example demonstrating the algorithm.

```python
# Example tableau (from Simplex.py):
tableau = [[-2, 0, 1, 1, 0, 0, 0, 3],
           [3, 0, -2, 0, 1, 2, 0, 6],
           [1, 1, -3, 0, 0, 1, 0, 2],
           [-3, 0, 2, 0, 0, -1, 1, 4],
           [2, 0, -11, 0, 0, -4, 0, 8]]
```

### `Big M Simplex.py`

Big-M method implementation for handling constraints that cannot be converted directly to slack form (i.e., constraints of type ≥ or =). Uses a large penalty value M to force artificial variables out of the basis.

```python
# Large penalty value used in Big-M method
M = 10000000000
```

## Usage

### Running the Standard Simplex

```bash
python Simplex.py
```

The program will display each iteration of the tableau and output "Solved!" when complete.

### Running the Big-M Method

```bash
python "Big M Simplex.py
```

The program will prompt you for:
- Number of artificial variables
- Number of equations
- Number of variables
- Matrix values for each row

## Example

### Input Format

For a problem with:
- 3 variables
- 2 equations

You would enter:
```
How many artificial variables?: 0
How many equations?: 2
How many variables?: 3
row 0
: [coefficients for equation 1]
: [coefficients for equation 2]
: [right-hand side values]
```

### Expected Output

The algorithm prints each tableau iteration showing:
- Current basic feasible solution
- Objective function value
- Convergence progress

## Requirements

- Python 3.x
- No external dependencies (standard library only)

## License

MIT License

## References

- Dantzig, G. B. (1951). "Maximization of a Linear Function of Variables Subject to Linear Inequalities". Activity Analysis of Production and Allocation.
- Bertsimas, D., & Tsitsiklis, J. N. (1997). Introduction to Linear Optimization. Athena Scientific.
