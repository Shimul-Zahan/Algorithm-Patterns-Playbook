# Algorithm Patterns Playbook 📘

Welcome to the **Algorithm Patterns Playbook**! This repository is designed to help you master various problem-solving techniques commonly used in coding interviews and competitive programming. Each folder in this repository focuses on a specific pattern or technique, providing explanations, example problems, and solutions.

---

## Table of Contents

- [Two Pointer Technique](#two-pointer-technique)
- [Sliding Window](#sliding-window)
- [Binary Search](#binary-search)
- [Dynamic Programming](#dynamic-programming)
- [Divide and Conquer](#divide-and-conquer)
- [Greedy Algorithms](#greedy-algorithms)
- [Backtracking](#backtracking)
- [Breadth-First Search (BFS)](#breadth-first-search-bfs)
- [Depth-First Search (DFS)](#depth-first-search-dfs)
- [Linked List Manipulation](#linked-list-manipulation)

---

## Techniques Overview

Each section contains an overview of the pattern, a description of common use cases, and links to example problems with explanations.

### Two Pointer Technique
Two pointers allow for efficient solutions by using two indices to traverse the data, often from different directions.

- **When to Use**: Arrays, linked lists, and problems involving pairs or partitions.
- **Common Problems**:
  - Remove duplicates from a sorted array
  - Container with most water
  - Three-sum problem
- [Examples & Solutions](./TwoPointer/)

### Sliding Window
The sliding window technique helps handle problems requiring tracking a subset of elements in an array or string.

- **When to Use**: Subarrays, substrings, or any fixed/variable-sized window problems.
- **Common Problems**:
  - Maximum sum subarray of size K
  - Longest substring without repeating characters
  - Minimum window substring
- [Examples & Solutions](./SlidingWindow/)

### Binary Search
Binary search is used on sorted data to find an element's position or make efficient decisions in logarithmic time.

- **When to Use**: Sorted arrays, binary trees, or any range-based search.
- **Common Problems**:
  - Find an element in a sorted array
  - First and last position of an element in sorted array
  - Find the square root of a number
- [Examples & Solutions](./BinarySearch/)

### Dynamic Programming
Dynamic programming (DP) is an optimization technique to solve problems by breaking them into overlapping subproblems and storing results.

- **When to Use**: Problems with optimal substructure and overlapping subproblems, like recursive problems.
- **Common Problems**:
  - Fibonacci sequence
  - Longest common subsequence
  - 0/1 Knapsack
- [Examples & Solutions](./DynamicProgramming/)

### Divide and Conquer
Divide and conquer divides a problem into subproblems, solves them independently, and combines their results.

- **When to Use**: Recursive solutions that can be divided, like sorting and searching.
- **Common Problems**:
  - Merge sort
  - Quick sort
  - Search in rotated sorted array
- [Examples & Solutions](./DivideAndConquer/)

### Greedy Algorithms
Greedy algorithms make the locally optimal choice at each step to find a global optimum.

- **When to Use**: Problems that allow local optimization with globally optimal results.
- **Common Problems**:
  - Activity selection problem
  - Fractional knapsack
  - Huffman coding
- [Examples & Solutions](./GreedyAlgorithms/)

### Backtracking
Backtracking explores all possible solutions and backtracks when a solution path fails.

- **When to Use**: Problems with multiple possible configurations, like combinations and permutations.
- **Common Problems**:
  - N-Queens problem
  - Permutations of a string
  - Sudoku solver
- [Examples & Solutions](./Backtracking/)

### Breadth-First Search (BFS)
BFS explores nodes in layers, often used in tree and graph traversals to find the shortest path.

- **When to Use**: Trees and graphs where shortest path or layer-based traversal is required.
- **Common Problems**:
  - Shortest path in an unweighted graph
  - Level order traversal of a tree
  - Minimum steps to reach a target
- [Examples & Solutions](./BFS/)

### Depth-First Search (DFS)
DFS explores as far as possible down a path before backtracking, useful in graphs and trees.

- **When to Use**: Graph or tree problems that require exploring all nodes or paths.
- **Common Problems**:
  - Connected components in a graph
  - Path sum in binary tree
  - Island counting in a matrix
- [Examples & Solutions](./DFS/)

### Linked List Manipulation
Working with linked lists requires specific techniques due to their linear node structure.

- **When to Use**: Problems with linked lists where pointer manipulation is required.
- **Common Problems**:
  - Reverse a linked list
  - Detect cycle in a linked list
  - Merge two sorted linked lists
- [Examples & Solutions](./LinkedListManipulation/)

---

## How to Use This Repository

Each technique folder contains:
1. **Overview**: A description of the technique, common use cases, and links to resources.
2. **Example Problems**: Real-world coding problems that apply the technique.
3. **Solutions**: Solutions with explanations in Python.

You can clone this repo and work through the problems to master these patterns. Each example problem includes comments to explain the solution and thought process.

## Contributing

Feel free to contribute by adding new examples, improving explanations, or adding new problem-solving techniques. Your contributions will help make this repository a comprehensive resource for algorithm patterns.

## License

This project is open-source and available under the [MIT License](LICENSE).

Happy coding and problem-solving! 🚀
