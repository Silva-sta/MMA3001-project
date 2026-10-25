
from pathlib import Path
import pandas as pd

# Locate the project files.
project_folder = Path(__file__).parent

# Load the extracted temperature data.
temps = pd.read_csv(project_folder / "temperature_data.csv")

# Convert columns to the correct data types.
temps["timestamp_utc"] = pd.to_datetime(
    temps["timestamp_utc"],
    utc=True,
    errors="coerce"
)

temps["temperature_c"] = pd.to_numeric(
    temps["temperature_c"],
    errors="coerce"
)

# Select our candidate sensor.
sensor_id = 6012002000869

data = temps[temps["sensorid"] == sensor_id].copy()

# Remove invalid measurements.
data = data.dropna(
    subset=["timestamp_utc", "temperature_c"]
)

# Sort by measurement time and remove duplicate timestamps.
data = (
    data.sort_values("timestamp_utc")
    .drop_duplicates(subset=["timestamp_utc"])
    .reset_index(drop=True)
)

# Calculate the time interval between measurements.
data["interval_minutes"] = (
    data["timestamp_utc"]
    .diff()
    .dt.total_seconds() / 60
)

# Save the cleaned dataset.
output_file = project_folder / "sensor_0869_clean.csv"

data[
    ["timestamp_utc", "temperature_c", "interval_minutes"]
].to_csv(output_file, index=False)

# Report the results.
print("\n--- CLEAN DATASET SUMMARY ---")
print(f"Sensor ID: {sensor_id}")
print(f"Number of measurements: {len(data)}")
print(f"Distinct temperatures: {data['temperature_c'].nunique()}")
print(f"Minimum temperature: {data['temperature_c'].min():.1f} °C")
print(f"Maximum temperature: {data['temperature_c'].max():.1f} °C")
print(f"Mean temperature: {data['temperature_c'].mean():.2f} °C")
print(f"Median temperature: {data['temperature_c'].median():.1f} °C")

print("\nMeasurement interval (minutes):")
print(data["interval_minutes"].describe().round(2))

print("\nFirst 5 measurements:")
print(data.head().to_string(index=False))

print("\nLast 5 measurements:")
print(data.tail().to_string(index=False))

print(f"\nClean dataset saved to: {output_file.name}")
