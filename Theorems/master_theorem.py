import math

def master_theorem(a, b, k):
    
    # Calculate log_b(a)
    log_b_a = math.log(a, b)
    
    # Case 1: log_b(a) > k
    if log_b_a > k:
        return f"O(n^{log_b_a:.3f})", 1, f"log_{b}({a}) = {log_b_a:.3f} > {k}"
    
    # Case 2: log_b(a) = k
    elif log_b_a == k:
        return f"O(n^{k} log n)", 2, f"log_{b}({a}) = {log_b_a:.3f} = {k}"
    
    # Case 3: log_b(a) < k
    else:
        return f"O(n^{k})", 3, f"log_{b}({a}) = {log_b_a:.3f} < {k}"


def print_master_theorem_result(a, b, k):

    complexity, case, comparison = master_theorem(a, b, k)
    
    print(f"Recurrence relation: T(n) = {a} T(n/{b}) + Θ(n^{k})")
    print(f"Master Theorem Case {case} applies: {comparison}")
    print(f"Time complexity: {complexity}")
    
    # Additional explanation based on the case
    if case == 1:
        print("The subproblems dominate.")
    elif case == 2:
        print("The subproblems and the combine step contribute equally.")
    else:
        print("The combine step dominates.")