import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, latex
from scipy.optimize import fsolve

# Import recurrence solver functions
from Theorems.master_theorem import master_theorem
from Theorems.extended_master_theorem_akra_bazzi import akra_bazzi_method
from Theorems.muster_theorem import muster_theorem
from Theorems.approximation_method import approximation_method

# Set page configuration
st.set_page_config(
    page_title="Recurrence Solver",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS for improved design
st.markdown("""
<style>
    /* Global styles */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header styling */
    h1, h2, h3, h4 {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    h1 {
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    
    /* Input field and widget styling */
    .stNumberInput, .stSlider, .stRadio, .stCheckbox, .stButton>button {
        border-radius: 6px;
    }
    
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Equation display box */
    .equation-box {
        background-color: #f1f8ff;
        border-left: 5px solid #3498db;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 6px 6px 0;
    }
    
    /* Result display box */
    .result-box {
        background: linear-gradient(to right, #f1f8ff, #f8f9fa);
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* Solution highlight */
    .solution-highlight {
        color: #2c3e50;
        font-weight: 600;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1rem;
        border-top: 1px solid #e0e0e0;
        color: #7f8c8d;
    }
    
    /* Section card styling */
    .section-card {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-top: 3px solid #3498db;
    }
    
    /* Hide Streamlit's default elements better */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Dark mode compatible elements */
    @media (prefers-color-scheme: dark) {
        .section-card {
            background-color: #2d3748;
            border-top: 3px solid #4299e1;
        }
        
        .result-box {
            background: linear-gradient(to right, #2d3748, #1a202c);
        }
        
        .equation-box {
            background-color: #2d3748;
            border-left: 5px solid #4299e1;
        }
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Recurrence Equation Solver")
    
    with st.container():
        st.markdown("""
        <div class="section-card">
        <h3>Analyze the Time Complexity of Recursive Algorithms</h3>
        <p>This tool helps you determine the asymptotic complexity of recursive algorithms 
        by analyzing their recurrence relations using various theoretical methods.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Sidebar for navigation
    with st.sidebar:
        st.title("Navigation")
        solver_type = st.radio(
            "Select Solver Type",
            ["Master Theorem", 
             "Extended Master Theorem (Akra-Bazzi)", 
             "Muster Theorem (Decreasing Functions)", 
             "Approximation Method"]
        )
    
    # Display the selected solver
    if solver_type == "Master Theorem":
        master_theorem_ui()
    elif solver_type == "Extended Master Theorem (Akra-Bazzi)":
        akra_bazzi_ui()
    elif solver_type == "Muster Theorem (Decreasing Functions)":
        muster_theorem_ui()
    else:
        approximation_method_ui()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Recurrence Equation Solver - Design and Analysis of Algorithms</p>
    </div>
    """, unsafe_allow_html=True)

def render_equation(equation_str):
    """Render a LaTeX equation"""
    return f"$${equation_str}$$"

def generate_recurrence_latex(a, b, k, recurrence_type="dividing"):
    """Generate LaTeX representation of the recurrence relation"""
    n, c = symbols('n c')
    
    if recurrence_type == "dividing":
        # For T(n) = a * T(n/b) + O(n^k)
        left_side = r"T(n)"
        right_side = r"{} \cdot T\left(\frac{{n}}{{{}}} \right) + \Theta(n^{{{}}})".format(a, b, k)
    elif recurrence_type == "decreasing":
        # For T(n) = a * T(n-b) + O(n^k)
        left_side = r"T(n)"
        right_side = r"{} \cdot T(n - {}) + \Theta(n^{{{}}})".format(a, b, k)
    
    return r"{} = {}".format(left_side, right_side)

def master_theorem_ui():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Master Theorem Solver")
    st.write("""
        The Master Theorem applies to recurrence relations of the form:
        T(n) = a * T(n/b) + Θ(n^k)
    """)
    
    # Parameters input
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Number of subproblems (a)", min_value=1, value=2, step=1)
    with col2:
        b = st.number_input("Size reduction factor (b)", min_value=2, value=2, step=1)
    with col3:
        k = st.number_input("Exponent in combine step (k)", min_value=0.0, value=1.0, step=0.1)
    
    # Generate the LaTeX equation
    equation_latex = generate_recurrence_latex(a, b, k, "dividing")
    
    # Display the recurrence relation
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(render_equation(equation_latex), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate the result
    if st.button("Solve Recurrence"):
        complexity, case, comparison = master_theorem(a, b, k)
        
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Solution:")
        st.markdown(f"<span class='solution-highlight'>Case {case}</span> of the Master Theorem applies.", unsafe_allow_html=True)
        st.write(f"**Comparison:** {comparison}")
        st.markdown(f"**Time Complexity:** <span class='solution-highlight'>{complexity}</span>", unsafe_allow_html=True)
        
        # Additional explanation
        if case == 1:
            st.write("The subproblems dominate the overall complexity.")
        elif case == 2:
            st.write("The subproblems and the combine step contribute equally.")
        else:
            st.write("The combine step dominates the overall complexity.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visual representation
        log_b_a = math.log(a, b)
        st.subheader("Visual Comparison:")
        
        fig, ax = plt.subplots(figsize=(10, 5))
        x = np.linspace(1, 10, 100)
        
        # Plot n^log_b(a)
        y1 = np.power(x, log_b_a)
        ax.plot(x, y1, label=f"n^log_{b}({a}) = n^{log_b_a:.3f}", color='#3498db')
        
        # Plot n^k
        y2 = np.power(x, k)
        ax.plot(x, y2, label=f"n^{k}", color='#e74c3c')
        
        ax.set_xlabel('n')
        ax.set_ylabel('Growth rate')
        ax.set_title('Comparison of Growth Rates')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Add a background color to the figure
        fig.patch.set_facecolor('#f8f9fa')
        ax.set_facecolor('#f8f9fa')
        
        st.pyplot(fig)
    
    st.markdown('</div>', unsafe_allow_html=True)

def akra_bazzi_ui():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Extended Master Theorem (Akra-Bazzi) Solver")
    st.write("""
        The Akra-Bazzi method applies to recurrence relations of the form:
        T(n) = g(n) + ∑ aᵢ * T(n/bᵢ) for i = 1 to k
    """)
    
    # Number of subproblems input
    num_subproblems = st.slider("Number of subproblems", min_value=1, max_value=5, value=2)
    
    # Parameters input for each subproblem
    a_values = []
    b_values = []
    
    for i in range(num_subproblems):
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input(f"Coefficient for subproblem {i+1} (a{i+1})", value=1.0, step=0.1, key=f"a{i}")
            a_values.append(a)
        with col2:
            b = st.number_input(f"Divisor for subproblem {i+1} (b{i+1})", min_value=1.1, value=2.0, step=0.1, key=f"b{i}")
            b_values.append(b)
    
    # Input for g(n)
    k = st.number_input("Exponent in combine step (k for g(n) = n^k)", min_value=0.0, value=1.0, step=0.1)
    
    # Generate the LaTeX equation for display
    equation_parts = []
    for i in range(num_subproblems):
        equation_parts.append(f"{a_values[i]} \\cdot T\\left(\\frac{{n}}{{{b_values[i]}}}\\right)")
    
    recurrence_latex = "T(n) = " + " + ".join(equation_parts) + f" + \\Theta(n^{{{k}}})"
    
    # Display the recurrence relation
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(render_equation(recurrence_latex), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate the result
    if st.button("Solve Recurrence"):
        try:
            complexity, p, comparison = akra_bazzi_method(a_values, b_values, k)
            
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("Solution:")
            st.markdown(f"<span class='solution-highlight'>Characteristic constant p = {p:.5f}</span>", unsafe_allow_html=True)
            st.write(f"**Comparison:** {comparison}")
            st.markdown(f"**Time Complexity:** <span class='solution-highlight'>{complexity}</span>", unsafe_allow_html=True)
            
            # Additional explanation
            if k < p:
                st.write("The subproblems dominate the overall complexity.")
            elif k == p:
                st.write("The subproblems and the combine step contribute equally.")
            else:
                st.write("The combine step dominates the overall complexity.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"Error solving the recurrence: {e}")
            st.info("Note: The Akra-Bazzi method requires the scipy library for solving equations.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def muster_theorem_ui():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Muster Theorem Solver (for Decreasing Functions)")
    st.write("""
        The Muster Theorem applies to recurrence relations of the form:
        T(n) = a * T(n-b) + Θ(n^k)
    """)
    
    # Parameters input
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Number of subproblems (a)", min_value=0.0, value=1.0, step=0.1)
    with col2:
        b = st.number_input("Size reduction amount (b)", min_value=1, value=1, step=1)
    with col3:
        k = st.number_input("Exponent in combine step (k)", min_value=0.0, value=0.0, step=0.1)
    
    # Generate the LaTeX equation
    equation_latex = generate_recurrence_latex(a, b, k, "decreasing")
    
    # Display the recurrence relation
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(render_equation(equation_latex), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate the result
    if st.button("Solve Recurrence"):
        complexity, case, explanation = muster_theorem(a, b, k)
        
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Solution:")
        st.markdown(f"<span class='solution-highlight'>Case {case}</span> of the Muster Theorem applies.", unsafe_allow_html=True)
        st.write(f"**Reasoning:** {explanation}")
        st.markdown(f"**Time Complexity:** <span class='solution-highlight'>{complexity}</span>", unsafe_allow_html=True)
        
        # Additional explanation
        if case == 1:
            st.write("The combine step dominates, resulting in a polynomial time complexity.")
        elif case == 2:
            st.write("Each level adds a polynomial factor, increasing the degree by 1.")
        else:
            st.write("The recursive calls dominate, resulting in exponential time complexity.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def approximation_method_ui():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.header("Approximation Method (Different Size Subproblems)")
    st.write("""
        This method approximates the bounds for recurrences with subproblems of different sizes.
    """)
    
    # Number of subproblems input
    num_subproblems = st.slider("Number of subproblems", min_value=2, max_value=5, value=2)
    
    # Parameters input for each subproblem
    sizes = []
    weights = []
    
    st.write("Enter the size fraction for each subproblem (e.g., 0.5 for n/2, 0.33 for n/3):")
    
    for i in range(num_subproblems):
        col1, col2 = st.columns(2)
        with col1:
            size = st.number_input(f"Size fraction for subproblem {i+1}", 
                                  min_value=0.01, max_value=0.99, 
                                  value=0.5 if i == 0 else 0.33, 
                                  step=0.01, key=f"size{i}")
            sizes.append(size)
        with col2:
            weight = st.number_input(f"Weight for subproblem {i+1}", 
                                    value=1.0, step=0.1, key=f"weight{i}")
            weights.append(weight)
    
    # Input for g(n)
    k = st.number_input("Exponent in combine step (k for g(n) = n^k)", min_value=0.0, value=1.0, step=0.1)
    
    # Generate the LaTeX equation for display
    equation_parts = []
    for i in range(num_subproblems):
        # Convert decimal to fraction representation for display
        if sizes[i] == 0.5:
            size_display = "2"
        elif sizes[i] == 0.33 or sizes[i] == 0.34:
            size_display = "3"
        elif sizes[i] == 0.25:
            size_display = "4"
        else:
            # Approximate fraction
            size_display = f"{int(1/sizes[i])}"
            
        if weights[i] == 1:
            equation_parts.append(f"T\\left(\\frac{{n}}{{{size_display}}}\\right)")
        else:
            equation_parts.append(f"{weights[i]} \\cdot T\\left(\\frac{{n}}{{{size_display}}}\\right)")
    
    recurrence_latex = "T(n) = " + " + ".join(equation_parts) + f" + \\Theta(n^{{{k}}})"
    
    # Display the recurrence relation
    st.markdown('<div class="equation-box">', unsafe_allow_html=True)
    st.markdown(render_equation(recurrence_latex), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate the result
    if st.button("Solve Recurrence"):
        lower_bound, upper_bound, explanation = approximation_method(sizes, weights, k)
        
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("Solution:")
        st.markdown("<span class='solution-highlight'>Approximate Bounds:</span>", unsafe_allow_html=True)
        st.write(f"Lower bound (shallowest branch): {lower_bound}")
        st.write(f"Upper bound (deepest branch): {upper_bound}")
        st.markdown(f"<span class='solution-highlight'>Time Complexity Range:</span> {lower_bound} to {upper_bound}", unsafe_allow_html=True)
        st.write("**Note:** This is an approximation based on recursion tree analysis.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()