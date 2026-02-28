import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def circle_area_scaling(edge_gap=0.6):
    # True area ratios relative to Circle A
    area_ratios = [1, 1.5, 2, 3, 4, 5]
    labels = list("ABCDEF")

    # Base radius for Circle A
    base_radius = 0.55

    radii = np.array([base_radius * np.sqrt(r) for r in area_ratios])
    max_radius = float(radii.max())

    x_positions = [0.0]
    for i in range(1, len(radii)):
        prev_x = x_positions[-1]
        prev_r = radii[i - 1]
        curr_r = radii[i]
        x_positions.append(prev_x + prev_r + edge_gap + curr_r)
    x_positions = np.array(x_positions)

    fig, ax = plt.subplots(figsize=(14, 5), constrained_layout=True)
    fig.patch.set_facecolor("#0b1020")
    ax.set_facecolor("#0b1020")
    ax.set_aspect("equal")
    ax.axis("off")

    for x, radius, label in zip(x_positions, radii, labels):
        ax.add_patch(Circle((x, 0), radius,
                            facecolor="#4cc9f0", alpha=0.28,
                            edgecolor="none"))
        
        ax.add_patch(Circle((x, 0), radius,
                            fill=False, linewidth=2.2,
                            edgecolor="#a6e3ff"))

        ax.text(x, -max_radius - 0.65, label,
                ha="center", va="center",
                fontsize=14, color="white")

    left = float(x_positions[0] - radii[0] - 0.8)
    right = float(x_positions[-1] + radii[-1] + 0.8)
    ax.set_xlim(left, right)
    ax.set_ylim(-max_radius - 1.3, max_radius + 1.0)

    ax.set_title("Area Scaling Circles",
                 color="white", fontsize=16, pad=10)

    plt.show()

circle_area_scaling(edge_gap=0.7)