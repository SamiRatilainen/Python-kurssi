import numpy as np
import matplotlib.pyplot as plt

# x-arvot välillä -10 ja 20
x = np.linspace(-10, 20, 500)

# Määritellään keskiarvot ja keskihajonnat
means = [0, 10]
std_devs = [1, 4]

# Luo 2x2 kuviot
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for i, mean in enumerate(means):
    for j, std in enumerate(std_devs):
        ax = axes[i, j]
        y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
        ax.plot(x, y, color='blue', label=f"mean={mean}, std={std}")
        ax.legend()
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title(f"μ={mean}, σ={std}")

plt.suptitle("Gaussian distributions with varying parameters")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()