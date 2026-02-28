import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def brightness_ramp(levels=10):
    S = np.linspace(0, 1, levels)
    h, w = 80, 80
    img = np.zeros((h, w * levels))
    for i, v in enumerate(S):
        img[:, w*i:w*(i+1)] = v

    fig, ax = plt.subplots(figsize=(12, 3), constrained_layout=True)
    fig.patch.set_facecolor("#0b1020")
    ax.set_facecolor("#0b1020")

    ax.imshow(img, cmap="gray", vmin=0, vmax=1, interpolation="nearest")
    ax.axis("off")

    for i in range(levels):
        ax.text(w*i + w/2, h + 10, chr(65+i),
                ha="center", va="center", fontsize=12, color="#a6e3ff")

    ax.set_title("Brightness Ramp",
                 pad=15, color="white", fontsize=14)

    border = FancyBboxPatch(
        (-2, -2), w*levels+4, h+4,
        boxstyle="round,pad=0.02,rounding_size=12",
        linewidth=1.5, edgecolor="#3a4a6b", facecolor="none"
    )
    ax.add_patch(border)

    plt.show()

brightness_ramp(10)