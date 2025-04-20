import sys
import math

# Import all recurrence solver methods
from Theorems.master_theorem import master_theorem, print_master_theorem_result
from Theorems.extended_master_theorem_akra_bazzi import akra_bazzi_method, print_akra_bazzi_result
from Theorems.muster_theorem import muster_theorem, print_muster_theorem_result
from Theorems.approximation_method import approximation_method, print_approximation_method_result


def clear_screen():
    """Clears the console screen"""
    print("\033[H\033[J", end="")


def print_header():
    """Prints the header for the application"""
    print("=" * 80)
    print("RECURRENCE EQUATION SOLVER".center(80))
    print("=" * 80)
    print("This program solves recurrence relations arising from recursive algorithms.")
    print("It automatically selects the appropriate method based on the type of recurrence.")
    print("=" * 80)


def get_function_info():
    """Gets the information about the function f(n) in the recurrence relation"""
    print("\nEnter information about the function f(n) in the recurrence:")
    while True:
        try:
            k = float(input("Enter the exponent k for f(n) = n^k: "))
            return k
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_dividing_function_info():
    """Gets information for recurrences with dividing functions T(n) = aT(n/b) + f(n)"""
    print("\nEnter information about the recurrence with dividing function:")
    
    # Get the number of subproblems
    while True:
        try:
            num_subproblems = int(input("Enter the number of subproblems: "))
            if num_subproblems < 1:
                print("Number of subproblems must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Get the a values and b values
    a_values = []
    b_values = []
    
    for i in range(num_subproblems):
        while True:
            try:
                a = float(input(f"Enter the coefficient for subproblem {i+1} (a{i+1}): "))
                b = float(input(f"Enter the divisor for subproblem {i+1} (b{i+1}): "))
                if b <= 1:
                    print("Divisor must be greater than 1.")
                    continue
                a_values.append(a)
                b_values.append(b)
                break
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
    
    return a_values, b_values


def get_decreasing_function_info():
    """Gets information for recurrences with decreasing functions T(n) = aT(n-b) + f(n)"""
    print("\nEnter information about the recurrence with decreasing function:")
    
    while True:
        try:
            a = float(input("Enter the coefficient a for T(n-b) term: "))
            b = float(input("Enter the decrement value b (how much n decreases): "))
            if b <= 0:
                print("Decrement value must be positive.")
                continue
            return a, b
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def solve_recurrence():
    """Main function to solve recurrence relations"""
    clear_screen()
    print_header()
    
    print("\nSelect the type of recurrence relation:")
    print("1. Dividing function: T(n) = aT(n/b) + f(n)")
    print("2. Decreasing function: T(n) = aT(n-b) + f(n)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1 or 2): "))
            if choice not in [1, 2]:
                print("Invalid choice. Please enter 1 or 2.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Get the function info
    k = get_function_info()
    
    # Process based on the type of recurrence
    if choice == 1:  # Dividing function
        a_values, b_values = get_dividing_function_info()
        
        # Decide which method to use based on the inputs
        if len(a_values) == 1:
            # Standard Master Theorem applies
            print("\n\nUsing Master Theorem:")
            print_master_theorem_result(a_values[0], b_values[0], k)
        else:
            # Check if all subproblems have same size
            if all(b == b_values[0] for b in b_values):
                # Extended Master Theorem (Akra-Bazzi) applies
                print("\n\nUsing Extended Master Theorem (Akra-Bazzi method):")
                print_akra_bazzi_result(a_values, b_values, k)
            else:
                # Approximation method for different subproblem sizes
                print("\n\nUsing Approximation Method for different subproblem sizes:")
                # Convert b_values to size fractions (1/b)
                sizes = [1/b for b in b_values]
                print_approximation_method_result(sizes, a_values, k)
    
    else:  # Decreasing function
        a, b = get_decreasing_function_info()
        
        # Use Muster theorem for decreasing functions
        print("\n\nUsing Muster Theorem for decreasing functions:")
        print_muster_theorem_result(a, b, k)
    
    # Ask if the user wants to solve another recurrence
    print("\n")
    again = input("Do you want to solve another recurrence relation? (y/n): ")
    if again.lower() == 'y':
        solve_recurrence()
    else:
        print("\nThank you for using the Recurrence Equation Solver!")


if __name__ == "__main__":
    try:
        solve_recurrence()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        print("Please try again.")