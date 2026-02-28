import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def depth_squares():
    depth_levels = np.linspace(0, 0.8, 6)
    labels = ["A", "B", "C", "D", "E", "F"]

    fig, ax = plt.subplots(figsize=(10, 4), constrained_layout=True)
    ax.set_aspect("equal")
    ax.axis("off")

    x_positions = np.linspace(0, 12, len(depth_levels))

    for x, depth, label in zip(x_positions, depth_levels, labels):
        ax.add_patch(Rectangle((x, 0), 1, 1, fill=False, linewidth=2))
        ax.add_patch(Rectangle((x + depth, depth), 1, 1, fill=False, linestyle="--"))
        ax.text(x + 0.5, -0.5, label, ha='center')

    ax.set_xlim(-1, 14)
    ax.set_ylim(-1, 3)
    ax.set_title("Perceived Depth")

    plt.show()

depth_squares()