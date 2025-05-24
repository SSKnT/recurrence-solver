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

master_test_cases = [
    {
        "a": 2,
        "b": 2,
        "k": 1,
        "expected_case": 2,
        "expected_complexity": "O(n^1.0 log n)"
    },
    {
        "a": 3,
        "b": 2,
        "k": 1,
        "expected_case": 3,
        "expected_complexity": "O(n^1.5849)"
    },
    {
        "a": 2,
        "b": 2,
        "k": 2,
        "expected_case": 1,
        "expected_complexity": "O(n^2.0)"
    }
]

def run_master_test_cases():
    for i, test in enumerate(master_test_cases):
        print(f"Test Case {i + 1}:")
        a = test["a"]
        b = test["b"]
        k = test["k"]
        expected_case = test["expected_case"]
        expected_complexity = test["expected_complexity"]

        print_master_theorem_result(a, b, k)

        print("-" * 50)

run_master_test_cases()
