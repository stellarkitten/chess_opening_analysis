import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/data.csv")

nodes = df["nodes"]
labels = df.columns[1:]

for i in labels:
    if "1" in i:
        plt.plot(nodes, df[i], label=i)

plt.xscale("log")

plt.xlabel("Nodes")
plt.ylabel("Evaluation (centipawns)")
plt.title("Knight Moves")

plt.tight_layout()
plt.legend()
plt.show()

for i in labels:
    if "4" not in i and "1" not in i:
        plt.plot(nodes, df[i], label=i)

plt.xscale("log")

plt.xlabel("Nodes")
plt.ylabel("Evaluation (centipawns)")
plt.title("1-Square Pawn Moves")

plt.tight_layout()
plt.legend()
plt.show()

for i in labels:
    if "4" in i:
        plt.plot(nodes, df[i], label=i)

plt.xscale("log")

plt.xlabel("Nodes")
plt.ylabel("Evaluation (centipawns)")
plt.title("2-Square Pawn Moves")

plt.tight_layout()
plt.legend()
plt.show()

weighted_average = [np.average(df[i], weights=nodes) for i in labels]

plt.bar(labels, weighted_average)

for i, label in enumerate(weighted_average):
    if label >= 0:
        va_pos = "bottom"
    else:
        va_pos = "top"

    plt.annotate(label.round(1), (labels[i], weighted_average[i]), ha="center", va=va_pos)

plt.xticks(rotation="vertical")

plt.xlabel("Move")
plt.ylabel("Evaluation (centipawns)")
plt.title("Node-Weighted Average Evaluation")

plt.tight_layout()
plt.show()
