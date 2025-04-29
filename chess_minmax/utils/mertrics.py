import matplotlib.pyplot as plt
import json
import os

def save_metrics(metrics, filename="metrics_alpha.json"):
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=4)

def plot_metrics(metrics, output_folder="metrics_plots", algo_name="AlphaBeta"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Plot steps
    plt.figure()
    plt.plot(metrics["steps_per_move"], marker='o')
    plt.title(f"{algo_name} - Steps per Move")
    plt.xlabel("Move #")
    plt.ylabel("Steps")
    plt.savefig(os.path.join(output_folder, f"{algo_name}_steps.png"))

    # Plot nodes evaluated
    plt.figure()
    plt.plot(metrics["nodes_per_move"], marker='o', color='red')
    plt.title(f"{algo_name} - Nodes Evaluated per Move")
    plt.xlabel("Move #")
    plt.ylabel("Nodes")
    plt.savefig(os.path.join(output_folder, f"{algo_name}_nodes.png"))
