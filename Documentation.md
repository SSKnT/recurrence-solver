# Recurrence Solver: System Documentation

## Project Overview

This document outlines the design and implementation of our Recurrence Solver system, which addresses the Complex Computing Problem assignment for CSC-208 Design and Analysis of Algorithms.

## Team Members

1. [Student Name 1] - [Registration Number]
2. [Student Name 2] - [Registration Number] 
3. [Student Name 3] - [Registration Number]

## Problem Description

Recursive algorithms have their running time computed using various methods like mathematical induction, substitution method, recurrence tree method, or Master theorem. Each method has limitations, and our system implements multiple approaches to accurately solve different types of recurrence relations.

Our Recurrence Solver handles:
- Dividing function recurrences with same-size subproblems: `T(n) = aT(n/b) + f(n)`
- Dividing function recurrences with different-size subproblems: `T(n) = T(n/b) + T(n/b') + f(n)`
- Decreasing function recurrences: `T(n) = a T(n-b) + f(n)`

The system determines the appropriate solving method based on the input and produces the time complexity with the correct asymptotic notation.

## System Architecture

Our system implements four solver methods:

1. **Master Theorem** - For standard divide-and-conquer recurrences of the form `T(n) = aT(n/b) + Θ(n^k)`
2. **Extended Master Theorem (Akra-Bazzi)** - For recurrences with multiple subproblems of different sizes
3. **Muster Theorem** - For recurrences with decreasing functions like `T(n) = aT(n-b) + Θ(n^k)`
4. **Approximation Method** - For recurrences with subproblems of different sizes where other methods don't apply

### File Structure

```
recurrence-solver/
├── app.py                  # Web interface using Streamlit
├── main.py                 # CLI version of the application
├── test_case.py            # Testing utilities
├── Theorems/
│   ├── master_theorem.py   # Implementation of Master Theorem
│   ├── extended_master_theorem_akra_bazzi.py  # Akra-Bazzi method
│   ├── muster_theorem.py   # Solving decreasing recurrences
│   └── approximation_method.py  # Custom method for different size subproblems
└── Documentation.md        # This documentation file
```

## Implementation Details

### 1. Master Theorem

The Master Theorem applies to recurrence relations of the form:
```
T(n) = a T(n/b) + Θ(n^k)
```

Where:
- `a` ≥ 1: number of subproblems
- `b` > 1: size reduction factor
- `k` ≥ 0: exponent of the work done outside the recursive calls

Our implementation compares `log_b(a)` and `k` to determine the appropriate case:

- **Case 1**: If `log_b(a) > k`, then `T(n) = Θ(n^(log_b(a)))`
- **Case 2**: If `log_b(a) = k`, then `T(n) = Θ(n^k log n)`
- **Case 3**: If `log_b(a) < k`, then `T(n) = Θ(n^k)`

### 2. Extended Master Theorem (Akra-Bazzi Method)

The Akra-Bazzi method handles more general recurrences of the form:
```
T(n) = g(n) + Σ (a_i * T(n/b_i)) for i = 1 to k
```

Our implementation:
1. Finds the unique real value `p` that satisfies the equation: Σ a_i * (b_i)^(-p) = 1
2. Compares `p` with the exponent of `g(n)` to determine the time complexity

### 3. Muster Theorem

For decreasing recurrences of the form:
```
T(n) = a T(n-b) + Θ(n^k)
```

Our implementation has three cases:
- **Case 1**: If `a < 1`, then `T(n) = O(n^k)`
- **Case 2**: If `a = 1`, then `T(n) = O(n^(k+1))`
- **Case 3**: If `a > 1`, then `T(n) = O(a^(n/b) * n^k)` (exponential complexity)

### 4. Approximation Method

For recurrences with subproblems of different sizes, we use a custom approach:
1. Analyze the shallowest branch of the recursion tree to determine a lower bound
2. Analyze the deepest branch to determine an upper bound
3. Return both bounds to provide a range for the algorithm's time complexity

## System Flow

1. User inputs recurrence type (dividing or decreasing function)
2. User inputs values for parameters (a, b, and f(n))
3. System identifies the appropriate solver method based on the input
4. The selected method analyzes the recurrence relation
5. System outputs the time complexity with appropriate asymptotic notation

## User Interface

We've implemented two interfaces:
1. **Command-Line Interface (CLI)** - For quick access and scriptability
2. **Web Interface** - Built with Streamlit for an interactive, user-friendly experience

## Examples and Analysis

### Example 1: Binary Search
- Recurrence: `T(n) = T(n/2) + O(1)`
- Parameters: `a = 1, b = 2, k = 0`
- Using Master Theorem: `log_2(1) = 0 = k` → Case 2
- Result: `T(n) = Θ(log n)`

### Example 2: Merge Sort
- Recurrence: `T(n) = 2T(n/2) + O(n)`
- Parameters: `a = 2, b = 2, k = 1`
- Using Master Theorem: `log_2(2) = 1 = k` → Case 2
- Result: `T(n) = Θ(n log n)`

### Example 3: Linear Search Recursive Variant
- Recurrence: `T(n) = T(n-1) + O(1)`
- Parameters: `a = 1, b = 1, k = 0`
- Using Muster Theorem: `a = 1` → Case 2
- Result: `T(n) = O(n)`

## Conclusion

Our Recurrence Solver effectively analyzes a wide range of recursive algorithms by:
1. Correctly identifying the recurrence type
2. Selecting the appropriate solving method
3. Accurately calculating the time complexity
4. Presenting results with proper asymptotic notation

This comprehensive approach ensures that users can quickly understand the efficiency class of their recursive algorithms, aiding in algorithm analysis and optimization.

## References

1. Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.
2. Akra, M., & Bazzi, L. (1998). On the solution of linear recurrence equations. Computational Optimization and Applications, 10(2), 195-210.
3. Bentley, J.L., Haken, D., & Saxe, J.B. (1980). A general method for solving divide-and-conquer recurrences. ACM SIGACT News, 12(3), 36-44.