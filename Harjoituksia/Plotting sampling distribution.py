import numpy as np
import matplotlib.pyplot as plt

sample_sizes = [10, 100, 1000, 10000]
bins = 31

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, size in enumerate(sample_sizes):
    sample = np.random.normal(loc=0, scale=1, size=size)
    axes[i].hist(sample, bins=bins, color='blue', edgecolor='black')
    axes[i].set_title(f"Sample size = {size}")
    axes[i].set_xlabel("Value")
    axes[i].set_ylabel("Frequency")

fig.suptitle("Sampling from the Standard Normal Distribution")
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.savefig("sampling_histograms.png")
plt.show()