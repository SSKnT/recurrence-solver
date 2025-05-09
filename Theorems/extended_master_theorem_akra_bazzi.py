import math
from scipy.optimize import fsolve


def akra_bazzi_method(a_values, b_values, k, p=1):
    
    # Check if input lengths match
    if len(a_values) != len(b_values):
        return "Error: The number of a and b values must be the same"
    
    # Define the function for finding p (characteristic constant)
    def equation(p):
        return sum(a * (b ** (-p)) for a, b in zip(a_values, b_values)) - 1
    
    # If p is not provided (default=1), solve for p
    if p == 1:
        try:
            # Solve the characteristic equation to find p
            p = fsolve(equation, 0.5)[0]
        except:
            return "Error: Could not solve for the characteristic constant p"
    
    # Determine the complexity based on the Akra-Bazzi theorem
    if k < p:
        complexity = f"O(n^{p:.3f})"
        comparison = f"k = {k} < p = {p:.3f}"
    elif k == p:
        complexity = f"O(n^{p:.3f} log n)"
        comparison = f"k = {p:.3f} = p"
    else:  # k > p
        complexity = f"O(n^{k})"
        comparison = f"k = {k} > p = {p:.3f}"
    
    return complexity, p, comparison


def print_akra_bazzi_result(a_values, b_values, k, p=1):

    try:
        complexity, p_value, comparison = akra_bazzi_method(a_values, b_values, k, p)
        
        # Print the recurrence relation
        relation = "T(n) = "
        for i in range(len(a_values)):
            relation += f"{a_values[i]}T(n/{b_values[i]}) + "
        relation += f"Θ(n^{k})"
        
        print(f"Recurrence relation: {relation}")
        print(f"Characteristic constant p = {p_value:.3f}")
        print(f"Comparison: {comparison}")
        print(f"Time complexity: {complexity}")
        
        # Additional explanation
        if k < p_value:
            print("The subproblems dominate.")
        elif k == p_value:
            print("The subproblems and the combine step contribute equally.")
        else:
            print("The combine step dominates.")
            
    except Exception as e:
        print(f"Could not apply the Akra-Bazzi method: {e}")
        print("Note: The Akra-Bazzi method requires the scipy library for solving equations.")
        print("Install it with: pip install scipy")