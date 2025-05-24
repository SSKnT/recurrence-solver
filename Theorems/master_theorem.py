import math

def master_theorem(a, b, k):
    log_b_a = math.log(a, b)

    # Case 1: log_b(a) > k
    if log_b_a > k:
        return f"O(n^{log_b_a:.3f})", 1, f"log_{b}({a}) = {log_b_a:.3f} > {k}"

    # Case 2: log_b(a) ≈ k
    elif math.isclose(log_b_a, k, rel_tol=1e-9):
        return f"O(n^{k} log n)", 2, f"log_{b}({a}) = {log_b_a:.3f} ≈ {k}"

    # Case 3: log_b(a) < k
    else:
        return f"O(n^{k})", 3, f"log_{b}({a}) = {log_b_a:.3f} < {k}"


def print_master_theorem_result(a, b, k):
    complexity, case, comparison = master_theorem(a, b, k)

    print(f"Recurrence relation: T(n) = {a} T(n/{b}) + Θ(n^{k})")
    print(f"Master Theorem Case {case} applies: {comparison}")
    print(f"Time complexity: {complexity}")

    if case == 1:
        print("Case 1: The work done by recursive calls dominates the combine step.")
    elif case == 2:
        print("Case 2: The recursive work and the combine step contribute equally.")
    else:
        print("Case 3: The combine step dominates the recursive work.")
