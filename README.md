# Algorithm Repository

This repository contains implementations of various algorithms, primarily focused on optimization and pathfinding problems. Algorithms are categorized by their solution approach to highlight differences in guarantees, efficiency, and applicability.

## Categories

- **exact/**: Algorithms that guarantee optimal solutions, often for smaller or tractable problems (e.g., Branch and Bound for integer optimization).
- **heuristic/**: General heuristic methods that provide good (approximate) solutions efficiently, without strict guarantees (e.g., Ant Colony Optimization for NP-hard problems like TSP).
- **approximation/**: Algorithms with provable approximation ratios, offering bounded performance for hard problems.
- **data/**: Shared datasets for testing and benchmarking algorithms (e.g., scheduling data for term projects).

## Getting Started

1. Clone the repository:

    ```bash
    # Clone the repository
    git clone https://github.com/whats2000/Algorithm.git
    ```

2. This project uses `uv` for dependency management. To set up the environment:

    ```bash
    # Install uv if not already installed
    pip install uv
    
    # Sync the environment
    uv sync
    
    # Activate the virtual environment (optional, for manual activation)
    # On Unix: source .venv/bin/activate
    # On Windows: .venv\Scripts\activate
    
    # Run Jupyter notebooks
    uv run jupyter notebook
    ```

## Examples

- **Heuristic**: Ant Colony for Traveling Salesman Problem (TSP) approximation in `heuristic/ant_colony/traveling_salesman.ipynb`.
- **Exact**: Branch and Bound implementations in `exact/branch_and_bound/`.

## Contributing

Feel free to add new algorithms or improve existing ones. Follow the folder structure and include documentation.

## License

See [LICENSE](LICENSE) for details.
