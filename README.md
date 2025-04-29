# Recurrence Solver

A powerful tool for analyzing and solving recurrence relations in algorithmic complexity analysis.

![Recurrence Solver](https://img.shields.io/badge/Recurrence-Solver-3498db)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.12+-red)

## 📖 Overview

Recurrence Solver is a comprehensive tool designed to solve and analyze recurrence relations commonly encountered in algorithm analysis. It provides multiple solving methods, including:

- Master Theorem
- Extended Master Theorem (Akra-Bazzi)
- Muster Theorem (for decreasing functions)
- Approximation Method (for different size subproblems)

The application offers both a command-line interface and an interactive web interface using Streamlit.

## ✨ Live Demo

You can try out the Recurrence Solver online:

[Access the Recurrence Solver Web App](https://recurrence-solver.streamlit.app)

## 🚀 Features

- **Multiple Solving Methods**: Apply various theoretical approaches to solve different types of recurrence relations
- **Interactive Visualization**: View graphical comparisons between growth rates
- **LaTeX Rendering**: Beautiful mathematical notation for equations
- **User-friendly Interface**: Intuitive UI with clear instructions
- **Dark Mode Support**: Comfortable viewing in different lighting conditions

## 💻 Installation and Setup

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/recurrence-solver.git
   cd recurrence-solver
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Usage

### Web Interface (Recommended)

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open your browser and navigate to `http://localhost:8501`

### Command Line Interface

Use the terminal-based version:

```bash
python main.py
```

Follow the interactive prompts to input your recurrence relation parameters.

## 📊 Examples

### Master Theorem

Solve recurrences of the form: T(n) = a * T(n/b) + Θ(n^k)

Example: T(n) = 2 * T(n/2) + Θ(n)

### Akra-Bazzi Method

Solve recurrences with multiple terms: T(n) = g(n) + ∑ aᵢ * T(n/bᵢ)

Example: T(n) = T(n/3) + T(2n/3) + Θ(n)

### Muster Theorem

Solve recurrences with subtraction: T(n) = a * T(n-b) + Θ(n^k)

Example: T(n) = T(n-1) + Θ(1)

## 🧮 Mathematical Background

The application implements various mathematical theorems for solving recurrence relations:

- **Master Theorem**: A method for solving divide-and-conquer recurrences where subproblems have equal size
- **Akra-Bazzi Method**: A generalization of the Master Theorem for more complex recurrences
- **Muster Theorem**: For recurrences involving subtraction rather than division
- **Approximation Method**: For approximating bounds when exact solutions are difficult

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/SSKnT/recurrence-solver/issues).

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

For any questions or feedback, please reach out via [GitHub issues](https://github.com/SSKnT/recurrence-solver/issues).
