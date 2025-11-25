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


def plot_gantt(sequence: List[int], processing_times: np.ndarray, release_dates: np.ndarray) -> None:
    """
    Plots a Gantt chart for the given job sequence with release date indicators.

    Args:
        sequence (List[int]): The sequence of job indices.
        processing_times (np.ndarray): Processing times for each job.
        release_dates (np.ndarray): Release dates for each job.
    """
    current_time = 0
    schedule_data = []

    # Build schedule with start times
    for position, job in enumerate(sequence):
        start = max(current_time, release_dates[job])
        finish = start + processing_times[job]
        idle = start - current_time

        schedule_data.append({
            'position': position,
            'job': job,
            'start': start,
            'finish': finish,
            'duration': processing_times[job],
            'release': release_dates[job],
            'idle': idle
        })

        current_time = finish

    # Create plot
    fig, ax = plt.subplots(figsize=(14, max(6, len(sequence) * 0.5)))

    # Plot each job
    for i, data in enumerate(schedule_data):
        # Plot idle time if exists
        if data['idle'] > 0:
            ax.barh(i, data['idle'], left=data['start'] - data['idle'],
                    color='lightgray', alpha=0.5, edgecolor='gray', linewidth=0.5,
                    label='Idle' if i == 0 and data['idle'] > 0 else '')

        # Plot job execution
        ax.barh(i, data['duration'], left=data['start'],
                color='skyblue', edgecolor='black', linewidth=1.5)

        # Label job in center of bar
        ax.text(data['start'] + data['duration'] / 2, i,
                f"Job {data['job']}",
                ha='center', va='center', fontweight='bold', fontsize=10)

        # Add release date marker (vertical line)
        ax.plot([data['release'], data['release']], [i - 0.4, i + 0.4],
                'r--', linewidth=2, label='Release' if i == 0 else '')

        # Add text showing release date
        if data['release'] < data['start']:
            ax.text(data['release'], i - 0.5, f"r={int(data['release'])}",
                    ha='center', va='top', fontsize=8, color='red')

    # Formatting
    ax.set_yticks(range(len(sequence)))
    ax.set_yticklabels([f"Position {i}" for i in range(len(sequence))])
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Execution Order', fontsize=12)
    ax.set_title('Gantt Chart: Single Machine Schedule (1|r_j|∑C_j)', fontsize=14, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)
    ax.set_xlim(0, current_time * 1.05)

    # Add legend (remove duplicates)
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), loc='upper right')

    plt.tight_layout()
    plt.show()
