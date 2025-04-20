import math

def muster_theorem(a, b, k):
    """
    Applies the Muster Theorem to determine the time complexity of recursive algorithms
    with decreasing functions.
    
    The Muster Theorem applies to recurrence relations of the form:
    T(n) = a * T(n-b) + O(n^k)
    
    Where:
    - a: number of subproblems in the recursion
    - b: amount by which input size is reduced in each subproblem
    - k: exponent in the running time of the combine step
    
    Returns a tuple containing:
    - The asymptotic complexity as a string
    - The case of the Muster Theorem that was applied
    - An explanation of the result
    """
    
    # Case 1: a < 1
    if a < 1:
        return f"O(n^{k})", 1, f"a = {a} < 1, dominated by the combine step"
    
    # Case 2: a = 1
    elif a == 1:
        return f"O(n^{k+1})", 2, f"a = 1, increases the degree of the polynomial by 1"
    
    # Case 3: a > 1
    else:
        if k == 0:
            return f"O({a}^(n/{b}))", 3, f"a = {a} > 1, exponential growth dominates"
        else:
            return f"O({a}^(n/{b}) * n^{k})", 3, f"a = {a} > 1, exponential x polynomial"


def print_muster_theorem_result(a, b, k):
    """
    Prints a detailed explanation of the Muster Theorem application.
    
    Parameters:
    - a: number of subproblems
    - b: amount by which input size is reduced
    - k: exponent in the combine step
    """
    complexity, case, explanation = muster_theorem(a, b, k)
    
    print(f"Recurrence relation: T(n) = {a} T(n-{b}) + Θ(n^{k})")
    print(f"Muster Theorem Case {case} applies: {explanation}")
    print(f"Time complexity: {complexity}")
    
    # Additional explanation based on the case
    if case == 1:
        print("The combine step dominates, resulting in a polynomial time complexity.")
    elif case == 2:
        print("Each level adds a polynomial factor, increasing the degree by 1.")
    else:
        print("The recursive calls dominate, resulting in exponential time complexity.")