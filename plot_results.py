
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Load the interpolation results
# --------------------------------------------------

project_folder = Path(__file__).parent

results = pd.read_csv(
    project_folder / "interpolation_results.csv"
)

# Use the number of hidden readings as the x-axis.
x = results["readings_hidden_per_trial"]


# --------------------------------------------------
# 2. Graph 1: Mean Absolute Error (MAE)
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    results["linear_MAE_C"],
    marker="o",
    label="Linear interpolation"
)

plt.plot(
    x,
    results["spline_MAE_C"],
    marker="s",
    label="Cubic spline interpolation"
)

plt.xlabel("Number of consecutive hidden readings")
plt.ylabel("Mean Absolute Error (°C)")
plt.title("Interpolation Accuracy: MAE vs Gap Size")

plt.xticks(x)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    project_folder / "mae_comparison.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# 3. Graph 2: Root Mean Square Error (RMSE)
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    results["linear_RMSE_C"],
    marker="o",
    label="Linear interpolation"
)

plt.plot(
    x,
    results["spline_RMSE_C"],
    marker="s",
    label="Cubic spline interpolation"
)

plt.xlabel("Number of consecutive hidden readings")
plt.ylabel("Root Mean Square Error (°C)")
plt.title("Interpolation Accuracy: RMSE vs Gap Size")

plt.xticks(x)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    project_folder / "rmse_comparison.png",
    dpi=300
)

plt.show()


# --------------------------------------------------
# 4. Confirm that the graphs were saved
# --------------------------------------------------

print("\nGraphs generated successfully!")
print("Saved: mae_comparison.png")
print("Saved: rmse_comparison.png")
