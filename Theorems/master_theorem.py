import math

def master_theorem(a, b, k):
    """
    Applies the Master Theorem to determine the time complexity of a divide-and-conquer algorithm.
    
    The Master Theorem applies to recurrence relations of the form:
    T(n) = a * T(n/b) + O(n^k)
    
    Where:
    - a: number of subproblems in the recursion
    - b: factor by which input size is reduced in each subproblem
    - k: exponent in the running time of the divide and combine steps
    
    Returns a tuple containing:
    - The asymptotic complexity as a string (e.g., "O(n log n)")
    - The case of the Master Theorem that was applied
    - The comparison result between log_b(a) and k
    """
    
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
    """
    Prints a detailed explanation of the Master Theorem application.
    
    Parameters:
    - a: number of subproblems
    - b: factor by which input size is reduced
    - k: exponent in the combine step
    """
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