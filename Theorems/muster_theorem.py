import math

def muster_theorem(a, b, k):
    
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