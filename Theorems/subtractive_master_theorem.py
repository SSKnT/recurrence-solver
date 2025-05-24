def subtractive_master_theorem(a, b, k):
    """
    For recurrences of the form:
    T(n) = a T(n - b) + Θ(n^k)
    Returns:
        complexity (str), case (int), explanation (str)
    """
    if a < 1:
        return f"O(n^{k})", 1, f"a = {a} < 1, dominated by the combine step (unusual case)"
    elif a == 1:
        return f"O(n^{k+1})", 2, f"a = 1, sum of polynomial terms increases degree by 1"
    else:  # a > 1
        if k == 0:
            return f"O({a}^(n/{b}))", 3, f"a = {a} > 1, exponential growth dominates"
        else:
            return f"O({a}^(n/{b}) * n^{k})", 3, f"a = {a} > 1, exponential times polynomial growth"


def print_subtractive_master_result(a, b, k):
    complexity, case, explanation = subtractive_master_theorem(a, b, k)
    print(f"Recurrence relation: T(n) = {a} T(n - {b}) + Θ(n^{k})")
    print(f"Master Theorem Case {case} applies: {explanation}")
    print(f"Time complexity: {complexity}\n")


# example
if __name__ == "__main__":
    sample_tests = [
        (0.5, 1, 2),
        (1, 1, 0),
        (1, 2, 1),
        (2, 1, 0),
        (3, 2, 1),
    ]

    for a, b, k in sample_tests:
        print_subtractive_master_result(a, b, k)
