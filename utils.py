import random
import numpy as np
from typing import List
import matplotlib.pyplot as plt


def set_seed(seed: int) -> None:
    """
    Set the random seed for reproducibility.

    Args:
        seed (int): The seed value to set.
    """
    random.seed(seed)
    np.random.seed(seed)


def plot_gantt(sequence: List[int], processing_times: List[float], release_dates: List[float]) -> None:
    """
    Plots a Gantt chart for the given job sequence.
    
    Args:
        sequence (List[int]): The sequence of job indices.
        processing_times (List[float]): Processing times for each job.
        release_dates (List[float]): Release dates for each job.
    """
    current_time = 0
    starts = []
    for job in sequence:
        start = max(current_time, release_dates[job])
        starts.append(start)
        current_time = start + processing_times[job]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for i, job in enumerate(sequence):
        ax.barh(job, processing_times[job], left=starts[i], color='skyblue', edgecolor='black')
        ax.text(starts[i] + processing_times[job]/2, job, f'J{job}', ha='center', va='center')
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Job')
    ax.set_title('Gantt Chart of Optimal Schedule')
    ax.grid(True, axis='x')
    plt.show()
