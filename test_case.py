from Theorems.master_theorem import print_master_theorem_result
from Theorems.extended_master_theorem_akra_bazzi import print_akra_bazzi_result
from Theorems.muster_theorem import print_muster_theorem_result
from Theorems.approximation_method import print_approximation_method_result

print("=" * 80)
print("RECURRENCE EQUATION SOLVER - TEST CASES".center(80))
print("=" * 80)

# # Test cases for the Master Theorem
# print("\nMASTER THEOREM TEST CASES")
# print("-" * 80)

# # Example 1: Merge Sort T(n) = 2T(n/2) + O(n)
# print("Example 1: Merge Sort")
# print_master_theorem_result(2, 2, 1)
# print()

# # Example 2: Binary Search T(n) = 1T(n/2) + O(1)
# print("Example 2: Binary Search")
# print_master_theorem_result(1, 2, 0)
# print()

# # Example 3: Strassen's Matrix Multiplication T(n) = 7T(n/2) + O(n^2)
# print("Example 3: Strassen's Matrix Multiplication")
# print_master_theorem_result(7, 2, 2)
# print()

# # Test cases for the Akra-Bazzi Method
# print("\nAKRA-BAZZI METHOD TEST CASES")
# print("-" * 80)

# # Example 4: Multiple recursion T(n) = 3T(n/2) + 2T(n/3) + O(n)
# print("Example 4: Multiple recursion")
# print_akra_bazzi_result([3, 2], [2, 3], 1)
# print()

# # Example 5: Unbalanced recursion T(n) = T(n/3) + T(2n/3) + O(n)
# print("Example 5: Unbalanced recursion")
# print_akra_bazzi_result([1, 1], [3, 1.5], 1)
# print()

# # Test cases for the Muster Theorem
# print("\nMUSTER THEOREM TEST CASES")
# print("-" * 80)

# # Example 6: Linear recurrence T(n) = T(n-1) + O(1)
# print("Example 6: Linear recurrence")
# print_muster_theorem_result(1, 1, 0)
# print()

# # Example 7: Exponential recurrence T(n) = 2T(n-1) + O(n)
# print("Example 7: Exponential recurrence")
# print_muster_theorem_result(2, 1, 1)
# print()

# Test cases for the Approximation Method
print("\nAPPROXIMATION METHOD TEST CASES")
print("-" * 80)

# Example 8: Different size subproblems T(n) = T(n/2) + T(n/3) + O(n)
print("Example 8: Different size subproblems")
print_approximation_method_result([1/2, 1/3], [1, 1], 1)
print()

# Example 9: Complex case T(n) = 2T(n/2) + 3T(n/4) + O(n^2)
print("Example 9: Complex case with different weights")
print_approximation_method_result([1/2, 1/4], [2, 3], 2)
print()

print("=" * 80)
print("END OF TEST CASES".center(80))
print("=" * 80)
