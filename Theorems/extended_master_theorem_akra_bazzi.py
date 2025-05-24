import math

def extended_master_theorem(a, b, k, i):
    """
    Solve recurrence of the form:
    T(n) = a T(n/b) + Θ(n^k (log n)^i)
    """
    log_b_a = math.log(a, b)

    if log_b_a > k:
        complexity = f"O(n^{log_b_a:.3f})"
        case = 1
        comparison = f"log_{b}({a}) = {log_b_a:.3f} > k = {k}"
    elif math.isclose(log_b_a, k):
        if i > -1:
            complexity = f"O(n^{k} (log n)^{i+1})"
            case = 2
            comparison = f"log_{b}({a}) = {log_b_a:.3f} ≈ k = {k}, i = {i} > -1"
        elif i == -1:
            complexity = f"O(n^{k} log log n)"
            case = 2
            comparison = f"log_{b}({a}) = {log_b_a:.3f} ≈ k = {k}, i = {i}"
        else:
            complexity = f"O(n^{k})"
            case = 2
            comparison = f"log_{b}({a}) = {log_b_a:.3f} ≈ k = {k}, i = {i} < -1"
    else:
        complexity = f"O(n^{k} (log n)^{i})"
        case = 3
        comparison = f"log_{b}({a}) = {log_b_a:.3f} < k = {k}"

    return complexity, case, comparison


def print_extended_master_result(a, b, k, i):
    complexity, case, comparison = extended_master_theorem(a, b, k, i)
    
    print(f"Recurrence relation: T(n) = {a} T(n/{b}) + Θ(n^{k} (log n)^{i})")
    print(f"Extended Master Theorem Case {case} applies: {comparison}")
    print(f"Time complexity: {complexity}")

    if case == 1:
        print("Case 1: The subproblems dominate.")
    elif case == 2:
        print("Case 2: The subproblems and the combine step contribute equally.")
    else:
        print("Case 3: The combine step dominates.")

# Sample test cases for extended master theorem

print_extended_master_result(2, 2, 1, 0)
# T(n) = 2 T(n/2) + Θ(n^1 (log n)^0) → Case 2

print_extended_master_result(2, 2, 1, 2)
# T(n) = 2 T(n/2) + Θ(n^1 (log n)^2) → Case 2

print_extended_master_result(4, 2, 1, 1)
# T(n) = 4 T(n/2) + Θ(n^1 (log n)^1) → Case 1

print_extended_master_result(2, 2, 2, 1)
# T(n) = 2 T(n/2) + Θ(n^2 (log n)^1) → Case 3

print_extended_master_result(3, 3, 2, 1)
# T(n) = 3 T(n/3) + Θ(n^2 (log n)^1) → Case 3

print_extended_master_result(3, 3, 1.0, -1)
# T(n) = 3 T(n/3) + Θ(n^1 (log n)^-1) → Case 2 (log log n)

print_extended_master_result(3, 3, 1.0, -2)
# T(n) = 3 T(n/3) + Θ(n^1 (log n)^-2) → Case 2 (log^(-2) n)

print_extended_master_result(16, 2, 4, 0)
# T(n) = 16 T(n/2) + Θ(n^4 (log n)^0) → Case 2

print_extended_master_result(16, 2, 5, 3)
# T(n) = 16 T(n/2) + Θ(n^5 (log n)^3) → Case 3

print_extended_master_result(8, 2, 2, 5)
# T(n) = 8 T(n/2) + Θ(n^2 (log n)^5) → Case 2
