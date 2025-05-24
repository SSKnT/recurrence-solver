import math

def extended_master_theorem(a, b, k, i):
    """
    Solve recurrence of the form:
    T(n) = a T(n/b) + Θ(n^k (log n)^i)
    """
    log_b_a = math.log(a, b)

    if log_b_a < k:
        complexity = f"O(n^{k} (log n)^{i})"
        case = 1
        comparison = f"log_{b}({a}) = {log_b_a:.3f} < k = {k}"
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
        complexity = f"O(n^{log_b_a:.3f})"
        case = 3
        comparison = f"log_{b}({a}) = {log_b_a:.3f} > k = {k}"

    return complexity, case, comparison


def print_extended_master_result(a, b, k, i):
    complexity, case, comparison = extended_master_theorem(a, b, k, i)
    
    print(f"Recurrence relation: T(n) = {a} T(n/{b}) + Θ(n^{k} (log n)^{i})")
    print(f"Extended Master Theorem Case {case} applies: {comparison}")
    print(f"Time complexity: {complexity}")

    if case == 1:
        print("Case 1: The combine step dominates.")
    elif case == 2:
        print("Case 2: The subproblems and the combine step contribute equally.")
    else:
        print("Case 3: The recursive subproblems dominate.")
