# Recurrence Relation Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

A comprehensive tool for solving recurrence relations using various theorems commonly used in algorithm analysis. This project provides both a command-line interface and a web-based interface built with Streamlit for analyzing and solving recurrence relations.

This project was developed as part of the Complex Computing Problem assignment for CSC-208 Design and Analysis of Algorithms.

## ✨ Live Demo

You can try out the Recurrence Solver online:

[Access the Recurrence Solver Web App](https://recurrence-solver.streamlit.app/)


## 📚 Features

- **Multiple Theorem Support**: 
  - Master Theorem
  - Extended Master Theorem 
  - Subtractive Master Theorem

- **Dual Interfaces**:
  - Command-line interface for quick access
  - Web-based Streamlit interface with visualizations and explanations

- **Educational Resources**:
  - Detailed explanations of each recurrence relation case
  - Step-by-step solution breakdowns

## 🎯 Use Cases

This tool is particularly useful for:

- **Students** studying Algorithm Design & Analysis courses
- **Educators** teaching algorithm complexity concepts
- **Developers** analyzing the time complexity of recursive algorithms
- **Computer Science researchers** working with recurrence relations

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/recurrence-solver.git
   cd recurrence-solver
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Command-line Interface

Run the application from your terminal:

```bash
python main.py
```

Then follow the interactive prompts to select a theorem and input the necessary parameters.

### Streamlit Web Interface

Launch the web interface with:

```bash
streamlit run app.py
```

Then open your browser and navigate to the provided URL (typically http://localhost:8501).

## 🧮 Supported Theorems

### Master Theorem
Solves recurrence relations of the form:
```
T(n) = a * T(n/b) + Θ(n^k)
```
Where:
- a ≥ 1 (number of subproblems)
- b > 1 (factor by which input size is reduced)
- k ≥ 0 (exponent in the combine step)

### Extended Master Theorem
Solves recurrence relations with logarithmic factors:
```
T(n) = a * T(n/b) + Θ(n^k * (log n)^i)
```
Where:
- a ≥ 1 (number of subproblems)
- b > 1 (factor by which input size is reduced)
- k ≥ 0 (exponent of n in the combine step)
- i (exponent of log n in the combine step)

### Subtractive Master Theorem
Solves recurrence relations of the form:
```
T(n) = a * T(n-b) + Θ(n^k)
```
Where:
- a (multiplier for the subproblem)
- b > 0 (amount subtracted from input size)
- k ≥ 0 (exponent in the combine step)

Additionally, the project's documentation mentions support for other methods including:
- **Akra-Bazzi Method** - For recurrences with multiple subproblems of different sizes
- **Approximation Method** - For recurrences with subproblems of different sizes where other methods don't apply

## 📊 Examples

### Master Theorem Example
For the recurrence relation `T(n) = 2 * T(n/2) + Θ(n)`:
- a = 2, b = 2, k = 1
- log₂(2) = 1, which equals k = 1
- Therefore, Case 2 of the Master Theorem applies
- Time complexity: O(n log n)

### Subtractive Master Theorem Example
For the recurrence relation `T(n) = 3 * T(n-1) + Θ(n)`:
- a = 3, b = 1, k = 1
- Since a > 1, the recurrence grows exponentially
- Time complexity: O(3^(n/1) * n^1) = O(3^n * n)

## 📝 Project Structure

```
recurrence-solver/
│
├── main.py                  # Command-line interface
├── app.py                   # Streamlit web interface
├── requirements.txt         # Project dependencies
├── README.md                # This file
├── Documentation.md         # Detailed system documentation
├── test_case.py             # Testing utilities
│
└── Theorems/                # Implementation of theorem algorithms
    ├── master_theorem.py              # Standard Master Theorem
    ├── extended_master_theorem.py     # Extended Master Theorem with logarithmic factors
    ├── subtractive_master_theorem.py  # For decreasing recurrences T(n) = aT(n-b) + f(n)
    └── other theorem implementations as referenced in documentation
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 🔗 Additional Resources

- [Introduction to Algorithms](https://mitpress.mit.edu/books/introduction-algorithms-third-edition) by Cormen, Leiserson, Rivest, and Stein
- [Algorithm Design Manual](http://www.algorist.com/) by Steven Skiena