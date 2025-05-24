
import streamlit as st
import math
from Theorems.master_theorem import master_theorem
from Theorems.extended_master_theorem import extended_master_theorem
from Theorems.subtractive_master_theorem import subtractive_master_theorem

# Set page configuration
st.set_page_config(
    page_title="Recurrence Relation Solver",
    page_icon="➗",
    layout="wide",
)

# Application header
def display_header():
    st.title("Recurrence Relation Solver")
    st.markdown("---")
    st.markdown(
        """
        This tool helps you solve recurrence relations using different theorems.
        Choose a theorem from the sidebar and enter the required parameters.
        """
    )

# Sidebar for navigation
def create_sidebar():
    with st.sidebar:
        st.title("Navigation")
        theorem_option = st.radio(
            "Choose a theorem:",
            [
                "Master Theorem",
                "Extended Master Theorem",
                "Subtractive Master Theorem", 
                "About"
            ]
        )
    return theorem_option

# Master Theorem UI
def render_master_theorem():
    st.header("Master Theorem")
    st.markdown("""
    The Master Theorem solves recurrence relations of the form:

    \[
    T(n) = a \cdot T\left(\frac{n}{b}\right) + \Theta(n^k)
    \]

    Where:
    - \(a \geq 1\): number of subproblems
    - \(b > 1\): factor by which input size is reduced
    - \(k \geq 0\): exponent in the combine step
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        a = st.number_input("a (number of subproblems)", min_value=1.0, value=2.0, step=1.0, format="%.0f", key="master_a")
    with col2:
        b = st.number_input("b (size reduction factor)", min_value=1.1, value=2.0, step=0.1, format="%.2f", key="master_b")
    with col3:
        k = st.number_input("k (exponent in combine step)", min_value=0.0, value=1.0, step=0.1, format="%.2f", key="master_k")

    if st.button("Solve using Master Theorem"):
        try:
            complexity, case, comparison = master_theorem(a, b, k)

            st.success(f"**Time Complexity:** {complexity}")

            st.subheader("Explanation")
            st.markdown(f"**Case {case}** applies: {comparison}")

            log_b_a = math.log(a, b)

            if case == 1:
                st.markdown("**The recursive work dominates:** Recursive calls contribute more than the combine step.")
                st.latex(fr"\log_{{{b:.2f}}}({int(a)}) = {log_b_a:.3f} > {k:.2f} \implies O(n^{{\log_{{{b:.2f}}}({int(a)})}})")
            elif case == 2:
                st.markdown("**The recursive work and combine step are comparable:** Both contribute equally.")
                st.latex(fr"\log_{{{b:.2f}}}({int(a)}) = {log_b_a:.3f} = {k:.2f} \implies O(n^{k:.2f} \log n)")
            else:
                st.markdown("**The combine step dominates:** The combine step contributes more than recursive calls.")
                st.latex(fr"\log_{{{b:.2f}}}({int(a)}) = {log_b_a:.3f} < {k:.2f} \implies O(n^{k:.2f})")

            st.subheader("Recurrence Relation")
            st.latex(f"T(n) = {int(a)} \\cdot T\\left(\\frac{{n}}{{{b:.2f}}}\\right) + \\Theta\\left(n^{{{k:.2f}}}\\right)")

        except Exception as e:
            st.error(f"Error solving the recurrence: {str(e)}")

# Extended Master Theorem UI
def render_extended_master_theorem():
    st.header("Extended Master Theorem")
    st.markdown("""
    The Extended Master Theorem solves recurrence relations of the form:

    \[
    T(n) = a \cdot T\left(\frac{n}{b}\right) + \Theta\left(n^k (\log n)^i\right)
    \]

    Where:
    - \(a \geq 1\): number of subproblems
    - \(b > 1\): input size reduction factor
    - \(k \geq 0\): exponent of \(n\) in combine step
    - \(i\): exponent of \(\log n\) in combine step
    """)

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("a (number of subproblems)", min_value=1.0, value=2.0, step=1.0, format="%.0f", key="ext_a")
        b = st.number_input("b (size reduction factor)", min_value=1.1, value=2.0, step=0.1, format="%.2f", key="ext_b")
    with col2:
        k = st.number_input("k (exponent of n in combine step)", min_value=0.0, value=1.0, step=0.1, format="%.2f", key="ext_k")
        i = st.number_input("i (exponent of log n in combine step)", value=0.0, step=1.0, format="%.0f", key="ext_i")

    if st.button("Solve using Extended Master Theorem"):
        try:
            complexity, case, comparison = extended_master_theorem(a, b, k, i)

            st.success(f"**Time Complexity:** {complexity}")

            st.subheader("Explanation")
            st.markdown(f"**Case {case}** applies: {comparison}")

            log_b_a = math.log(a, b)

            if case == 3:
                st.markdown("**The recursive work dominates:** Recursive calls contribute more than the combine step.")
                st.latex(f"\\text{{Since }} \\log_{{{b:.2f}}}({a:.0f}) = {log_b_a:.3f} > {k:.2f}, \\text{{ the time complexity is }} {complexity}")
            elif case == 2:
                st.markdown("**The recursive work and combine step are comparable:** Both contribute equally.")
                st.latex(f"\\text{{Since }} \\log_{{{b:.2f}}}({a:.0f}) = {log_b_a:.3f} \\approx {k:.2f}, \\text{{ the time complexity is }} {complexity}")
            else:
                st.markdown("**The combine step dominates:** The combine step work contributes more than recursive calls.")
                st.latex(f"\\text{{Since }} \\log_{{{b:.2f}}}({a:.0f}) = {log_b_a:.3f} < {k:.2f}, \\text{{ the time complexity is }} {complexity}")

            st.subheader("Recurrence Relation")
            st.latex(f"T(n) = {int(a)} \\cdot T\\left(\\frac{{n}}{{{b:.2f}}}\\right) + \\Theta\\left(n^{{{k:.2f}}} (\\log n)^{{{int(i)}}}\\right)")

        except Exception as e:
            st.error(f"Error solving the recurrence: {str(e)}")

# Subtractive Master Theorem UI
def render_subtractive_master_theorem():
    st.header("Subtractive Master Theorem")
    st.markdown("""
    The Subtractive Master Theorem solves recurrence relations of the form:

    \[
    T(n) = a \cdot T(n - b) + \Theta(n^k)
    \]

    Where:
    - \(a\): multiplier for the subproblem
    - \(b > 0\): amount subtracted from input size
    - \(k \geq 0\): exponent in the combine step
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        a = st.number_input("a (subproblem multiplier)", value=2.0, step=0.1, format="%.2f", key="sub_a")
    with col2:
        b = st.number_input("b (size reduction)", min_value=0.1, value=1.0, step=0.1, format="%.2f", key="sub_b")
    with col3:
        k = st.number_input("k (exponent in combine step)", min_value=0.0, value=1.0, step=0.1, format="%.2f", key="sub_k")

    if st.button("Solve using Subtractive Master Theorem"):
        try:
            complexity, case, explanation = subtractive_master_theorem(a, b, k)

            st.success(f"**Time Complexity:** {complexity}")

            st.subheader("Explanation")
            st.markdown(f"**Case {case}** applies: {explanation}")

            if case == 1:
                st.markdown("**Combine step dominates:** Recursive calls shrink quickly since \(a < 1\), so the work is dominated by the combine step.")
            elif case == 2:
                st.markdown("**Linear recurrence:** \(a = 1\) means each recursive level contributes equally, increasing polynomial degree by 1.")
            else:  # case == 3
                st.markdown("**Exponential growth:** When \(a > 1\), the number of subproblems grows exponentially with recursion depth.")

            st.subheader("Recurrence Relation")
            st.latex(f"T(n) = {a:.2f} \\cdot T(n - {b:.2f}) + \\Theta(n^{{{k:.2f}}})")

        except Exception as e:
            st.error(f"Error solving the recurrence: {str(e)}")


# About section
def render_about():
    st.header("About Recurrence Relation Solver")
    st.markdown("""
    ### What are Recurrence Relations?
    
    Recurrence relations are equations that define a sequence recursively, where each term is defined as a function of previous terms.
    In algorithm analysis, they're used to describe the running time of divide-and-conquer algorithms.
    
    ### Theorems Included:
    
    1. **Master Theorem**: For recurrences of form T(n) = a * T(n/b) + f(n) where a ≥ 1, b > 1
    
    2. **Extended Master Theorem**: Handles recurrences with logarithmic factors in the work function
    
    3. **Subtractive Master Theorem**: For recurrences of form T(n) = a * T(n-b) + f(n)
    
    ### Applications:
    
    - Analyzing divide and conquer algorithms like Merge Sort, Quick Sort
    - Understanding the complexity of recursive algorithms
    - Solving dynamic programming problems
    
    ### Resources:
    
    - [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) by Cormen, Leiserson, Rivest, and Stein
    - [Algorithm Design Manual](http://www.algorist.com/) by Steven Skiena
    """)

# Main application
def main():
    display_header()
    theorem_option = create_sidebar()
    
    if theorem_option == "Master Theorem":
        render_master_theorem()
    elif theorem_option == "Extended Master Theorem":
        render_extended_master_theorem()
    elif theorem_option == "Subtractive Master Theorem":
        render_subtractive_master_theorem()
    else:  # About
        render_about()
    
    # Footer
    st.markdown("---")
    st.markdown("© 2025 Recurrence Relation Solver | Created with Streamlit")

if __name__ == "__main__":
    main()