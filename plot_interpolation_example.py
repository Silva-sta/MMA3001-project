
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# --------------------------------------------------
# 1. Load and prepare the dataset
# --------------------------------------------------

project_folder = Path(__file__).parent

data = pd.read_csv(
    project_folder / "sensor_0869_clean.csv"
)

data["timestamp_utc"] = pd.to_datetime(
    data["timestamp_utc"],
    utc=True
)

data = data.sort_values("timestamp_utc").reset_index(drop=True)

# Convert timestamps to elapsed minutes.
times = (
    data["timestamp_utc"] - data["timestamp_utc"].iloc[0]
).dt.total_seconds().to_numpy() / 60

temperatures = data["temperature_c"].to_numpy(dtype=float)


# --------------------------------------------------
# 2. Select a representative section of data
# --------------------------------------------------

# Use a fixed random seed to make the example reproducible.
rng = np.random.default_rng(42)

# Select a section of 100 consecutive readings.
section_size = 100

section_start = rng.integers(
    0,
    len(temperatures) - section_size
)

section_end = section_start + section_size

section_times = times[section_start:section_end]
section_temperatures = temperatures[section_start:section_end]


# --------------------------------------------------
# 3. Hide six consecutive readings
# --------------------------------------------------

gap_length = 6

# Keep the hidden block away from the section boundaries.
gap_start = section_size // 2 - gap_length // 2

hidden_indices = np.arange(
    gap_start,
    gap_start + gap_length
)

# The remaining readings are treated as known measurements.
visible_mask = np.ones(
    section_size,
    dtype=bool
)

visible_mask[hidden_indices] = False

known_times = section_times[visible_mask]
known_temperatures = section_temperatures[visible_mask]

hidden_times = section_times[hidden_indices]
actual_temperatures = section_temperatures[hidden_indices]


# --------------------------------------------------
# 4. Estimate the missing temperatures
# --------------------------------------------------

# Linear interpolation
linear_predictions = np.interp(
    hidden_times,
    known_times,
    known_temperatures
)

# Cubic spline interpolation
spline = CubicSpline(
    known_times,
    known_temperatures,
    bc_type="natural"
)

spline_predictions = spline(hidden_times)


# --------------------------------------------------
# 5. Calculate errors for this example
# --------------------------------------------------

linear_mae = np.mean(
    np.abs(linear_predictions - actual_temperatures)
)

spline_mae = np.mean(
    np.abs(spline_predictions - actual_temperatures)
)

print("\n--- VISUAL INTERPOLATION EXAMPLE ---")
print(f"Hidden readings: {gap_length}")
print(f"Linear interpolation MAE: {linear_mae:.4f} °C")
print(f"Cubic spline interpolation MAE: {spline_mae:.4f} °C")


# --------------------------------------------------
# 6. Plot the temperature measurements and estimates
# --------------------------------------------------

plt.figure(figsize=(11, 6))

# Show the recorded measurements in the selected section.
plt.plot(
    section_times,
    section_temperatures,
    color="gray",
    linewidth=1.5,
    label="Original recorded temperatures"
)

# Highlight the measurements that would be missing.
plt.scatter(
    hidden_times,
    actual_temperatures,
    marker="o",
    s=75,
    label="Actual hidden temperatures",
    zorder=5
)

# Show linear interpolation estimates.
plt.scatter(
    hidden_times,
    linear_predictions,
    marker="x",
    s=90,
    label="Linear interpolation estimates",
    zorder=6
)

# Show cubic spline interpolation estimates.
plt.scatter(
    hidden_times,
    spline_predictions,
    marker="s",
    s=45,
    label="Cubic spline estimates",
    zorder=6
)

# Shade the missing-data interval.
plt.axvspan(
    hidden_times[0],
    hidden_times[-1],
    alpha=0.15,
    label="Missing-data interval"
)

plt.xlabel("Elapsed time since first measurement (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Reconstructing Missing Temperature Measurements")

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# Save the graph at high resolution.
plt.savefig(
    project_folder / "interpolation_example.png",
    dpi=300
)

plt.show()

print("\nGraph saved as: interpolation_example.png")
