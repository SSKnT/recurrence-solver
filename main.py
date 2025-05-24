
import sys
import os
from Theorems.master_theorem import print_master_theorem_result
from Theorems.extended_master_theorem import print_extended_master_result
from Theorems.subtractive_master_theorem import print_subtractive_master_result

def clear_screen():
    """Clear the console screen."""
    # Check if the OS is Windows or Unix-based
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_header():
    """Print the application header."""
    print("=" * 60)
    print("         RECURRENCE RELATION SOLVER")
    print("=" * 60)
    print("Solve recurrence relations using different theorems")
    print("=" * 60)

def print_menu():
    """Print the main menu options."""
    print("\nChoose a theorem to solve your recurrence relation:")
    print("1. Master Theorem (T(n) = a * T(n/b) + Θ(n^k))")
    print("2. Extended Master Theorem (T(n) = a * T(n/b) + Θ(n^k * (log n)^i))")
    print("3. Subtractive Master Theorem (T(n) = a * T(n-b) + Θ(n^k))")
    print("4. Exit")
    print("=" * 60)

def get_float_input(prompt):
    """Get a float input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def get_int_input(prompt):
    """Get an integer input from the user with validation."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")

def master_theorem_solver():
    """Handle the Master Theorem input and solution."""
    print("\n== Master Theorem Solver ==")
    print("For recurrences of form: T(n) = a * T(n/b) + Θ(n^k)")
    
    a = get_float_input("Enter value of a (number of subproblems): ")
    
    # Ensure b is not zero to prevent division by zero in log calculation
    while True:
        b = get_float_input("Enter value of b (factor by which input size is reduced, must be > 1): ")
        if b > 1:
            break
        print("Error: 'b' must be greater than 1 for the Master Theorem.")
    
    k = get_float_input("Enter value of k (exponent in the combine step): ")
    
    print("\nSolving...")
    print("-" * 50)
    print_master_theorem_result(a, b, k)

def extended_master_theorem_solver():
    """Handle the Extended Master Theorem input and solution."""
    print("\n== Extended Master Theorem Solver ==")
    print("For recurrences of form: T(n) = a * T(n/b) + Θ(n^k * (log n)^i)")
    
    a = get_float_input("Enter value of a (number of subproblems): ")
    
    # Ensure b is not zero to prevent division by zero in log calculation
    while True:
        b = get_float_input("Enter value of b (factor by which input size is reduced, must be > 1): ")
        if b > 1:
            break
        print("Error: 'b' must be greater than 1 for the Extended Master Theorem.")
    
    k = get_float_input("Enter value of k (exponent of n in the combine step): ")
    i = get_float_input("Enter value of i (exponent of log n in the combine step): ")
    
    print("\nSolving...")
    print("-" * 50)
    print_extended_master_result(a, b, k, i)

def subtractive_master_theorem_solver():
    """Handle the Subtractive Master Theorem input and solution."""
    print("\n== Subtractive Master Theorem Solver ==")
    print("For recurrences of form: T(n) = a * T(n-b) + Θ(n^k)")
    
    a = get_float_input("Enter value of a (multiplier for subproblem): ")
    
    # Ensure b is a positive value
    while True:
        b = get_float_input("Enter value of b (amount subtracted from input size, must be > 0): ")
        if b > 0:
            break
        print("Error: 'b' must be greater than 0 for the Subtractive Master Theorem.")
    
    k = get_float_input("Enter value of k (exponent in the combine step): ")
    
    print("\nSolving...")
    print("-" * 50)
    print_subtractive_master_result(a, b, k)

def main():
    """Main application loop."""
    while True:
        try:
            clear_screen()
            print_header()
            print_menu()
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                master_theorem_solver()
            elif choice == '2':
                extended_master_theorem_solver()
            elif choice == '3':
                subtractive_master_theorem_solver()
            elif choice == '4':
                print("\nThank you for using the Recurrence Relation Solver!")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again with different inputs.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()