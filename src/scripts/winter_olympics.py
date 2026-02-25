import os
import matplotlib.pyplot as plt

from ..config.config import COUNTRIES, GOLD_MEDALS, SCORES, VISUALIZATIONS_DIR

def visualization1_bar():
    """Bar chart of gold medals by country"""
    fig, ax = plt.subplots(figsize=(9, 6))
    fig.suptitle("Bar Chart - Gold Medals by Country", fontsize=12)

    x = list(range(len(COUNTRIES)))
    ax.bar(x, GOLD_MEDALS)
    ax.set_xticks(x)
    ax.set_xticklabels(COUNTRIES, rotation=20, ha="center")
    ax.set_yticks([])
    ax.set_ylim(0, 30)

    q = "Question: Which country has the fewest gold medals?"
    fig.text(0.5, 0.01, q, ha="center", fontsize=10)
    return fig

def visualization2_pie():
    """Pie chart of gold medals by country"""
    fig, ax = plt.subplots(figsize=(9, 6))
    fig.suptitle("Pie Chart - Gold Medals by Country", fontsize=12)

    pie_colors = ["#f1c40f", "#3498db", "#27ae60", "#e74c3c", "#800080"]
    ax.pie(
        GOLD_MEDALS,
        labels=COUNTRIES,
        colors=pie_colors,
    )

    q = "Question: Which country has the most gold medals?"
    fig.text(0.5, 0.01, q, ha="center", fontsize=10)
    return fig

def visualization3_3D():
    """3D bar chart of ski jumping scores by country"""
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111, projection="3d")
    fig.suptitle("3D Bar Chart - Ski Jumping Scores", fontsize=12)

    # 3D bar positions
    n = len(COUNTRIES)
    x_pos = list(range(n))
    y_pos = [0] * n
    z_pos = [0] * n
    dx = dy = 0.6
    dz = SCORES

    colors = ["#1a5276", "#2874a6", "#3498db", "#5dade2", "#85c1e9"]
    ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, shade=True)

    ax.set_xticks([x + dx / 2 for x in x_pos])
    ax.set_xticklabels(COUNTRIES, rotation=25, ha="right")
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_zlim(0, 250)
    
    q = "Question: Which country has the highest score in ski jumping?"
    fig.text(0.5, 0.01, q, ha="center", fontsize=10)
    return fig

def main(save=False):
    """Main function to run the winter olympics visualizations."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    visualizations_dir = os.path.join(project_root, VISUALIZATIONS_DIR)
    os.makedirs(visualizations_dir, exist_ok=True)

    plt.rcParams["font.size"] = 10
    figs = [visualization1_bar(), visualization2_pie(), visualization3_3D()]
    if save:
        for i, fig in enumerate(figs):
            plt.show()
            fig_path = os.path.join(visualizations_dir, f"winter_olympics_{i + 1}.png")
            fig.savefig(fig_path, dpi=120, bbox_inches="tight")
            print(f"Saved {fig_path}")

if __name__ == "__main__":
    main(save=True)