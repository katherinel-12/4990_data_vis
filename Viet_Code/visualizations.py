"""
Stevens' Law Human Perception Experiment - Visualization Generator

Generates 3 charts (bar, pie, 3D bar) with questions for judging
length, angle/area, and volume perception respectively.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

QUESTIONS_Y = 0.08  
QUESTIONS_FONT = 10


def save_bar_chart():
    """Bar chart testing LENGTH perception."""
    categories = ["Product A", "Product B", "Product C", "Product D", "Product E", "Product F"]
    values = [57, 52, 61, 59, 44, 58]
    

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(bottom=0.22)

    colors = plt.cm.Set2(np.linspace(0, 1, len(categories)))
    ax.bar(categories, values, color=colors, edgecolor="white", width=0.6)

    ax.set_yticks([])
    ax.set_ylabel("")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_title("Product Sales Comparison", fontsize=14, pad=12)

    questions = (
        "How many times bigger is Product A than Product E?\n"
        "A) 1.1x    B) 1.3x    C) 1.6x    D) 2.0x"
    )
    fig.text(0.5, QUESTIONS_Y, questions, ha="center", fontsize=QUESTIONS_FONT,
             fontstyle="italic", linespacing=1.8)

    fig.savefig("bar_chart.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved bar_chart.png")


def save_pie_chart():
    """Pie chart testing ANGLE/AREA perception."""
    labels = ["Region 1", "Region 2", "Region 3", "Region 4", "Region 5", "Region 6"]
    values = [18, 22, 15, 20, 13, 12]

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.subplots_adjust(bottom=0.18)

    colors = plt.cm.Pastel1(np.linspace(0, 1, len(labels)))
    ax.pie(values, labels=labels, colors=colors, startangle=90,
           wedgeprops={"edgecolor": "white", "linewidth": 1.5})

    ax.set_title("Regional Market Share", fontsize=14, pad=12)

    questions = (
        "How many times bigger is Region 2 than Region 5?\n"
        "A) 1.2x    B) 1.5x    C) 1.7x    D) 2.0x"
    )
    fig.text(0.5, QUESTIONS_Y, questions, ha="center", fontsize=QUESTIONS_FONT,
             fontstyle="italic", linespacing=1.8)

    fig.savefig("pie_chart.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved pie_chart.png")


def save_3d_chart():
    """3D bar chart testing VOLUME perception."""
    items = ["Item A", "Item B", "Item C", "Item D", "Item E"]
    values = [62, 53, 48, 60, 58]

    fig = plt.figure(figsize=(10, 9))
    fig.subplots_adjust(bottom=0.28, top=0.92)
    ax = fig.add_subplot(111, projection="3d")

    x_pos = np.arange(len(items)) * 1.2
    colors = plt.cm.Set2(np.linspace(0, 0.8, len(items)))

    ax.bar3d(x_pos, np.zeros(len(items)), np.zeros(len(items)),
             dx=0.7, dy=0.7, dz=values, color=colors, edgecolor="gray",
             linewidth=0.5, alpha=0.9)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    ax.set_title("Inventory Volume by Item", fontsize=14, pad=12)
    ax.view_init(elev=25, azim=-55)

    for x, v, name in zip(x_pos, values, items):
        ax.text(x + 0.35, 0.35, v + 2, name, ha="center", va="bottom", fontsize=10, fontweight="bold")

    questions = (
        "How many times bigger is Item A than Item C?\n"
        "A) 1.1x    B) 1.3x    C) 1.6x    D) 2.0x"
    )
    fig.text(0.5, 0.06, questions, ha="center", fontsize=QUESTIONS_FONT,
             fontstyle="italic", linespacing=1.8)

    fig.savefig("3d_chart.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Saved 3d_chart.png")


if __name__ == "__main__":
    save_bar_chart()
    save_pie_chart()
    save_3d_chart()
    print("All visualizations generated.")
