# Numerical Reconstruction of Missing Building Temperature Measurements

## 1. Project Overview

This project investigates how accurately missing building temperature measurements can be estimated using numerical interpolation methods.

Environmental sensors are commonly used to monitor building conditions and support building management and HVAC (heating, ventilation, and air conditioning) systems. Missing sensor readings can interrupt temperature monitoring and affect subsequent data analysis. Numerical interpolation provides a way to estimate missing values from surrounding measurements.

The project aims to compares two numerical methods:

- **Linear interpolation**
- **Cubic spline interpolation**

The objective is to determine how the accuracy of these methods changes as the number of consecutive missing readings increases.

## 2. Research Question

How accurately can linear interpolation and cubic spline interpolation reconstruct missing building temperature measurements, and how does the length of the missing-data gap affect their accuracy?

## 3. Dataset

The project uses environmental sensor data supplied for the MMA3001 project.

While he original dataset contains temperature readings alongside other environmental measurements. The data was processed to select one sensor and prepare a consistent time series for analysis.
**Selected sensor ID:** 6012002000869

The cleaned dataset contains the following:

| Property | Value |
|---|---:|
| Number of measurements | 13,800 |
| Mean temperature | 23.09 °C |
| Median temperature | 23.3 °C |
| Minimum temperature | 19.0 °C |
| Maximum temperature | 28.5 °C |
| Median measurement interval | 10 minutes |

Data preparation included selecting the chosen sensor, removing records with missing timestamps or temperatures, sorting measurements , and removing duplicate timestamps. Where duplicate timestamps existed, their recorded temperatures were consistent.

The cleaned dataset is stored in `sensor_0869_clean.csv`.

## 4. Numerical Methods

### 4.1 Linear Interpolation

Linear interpolation estimates a missing temperature by assuming that temperature changes linearly between two known measurements.

It is computationally simple and provides a baseline for comparison with a more flexible interpolation method.

### 4.2 Cubic Spline Interpolation

Cubic spline interpolation estimates missing temperatures using piecewise cubic polynomials fitted to the available measurements.

The implementation uses a natural cubic spline, which applies zero second-derivative boundary conditions at the endpoints of the fitted data.

Cubic spline interpolation can represent smoother curves than linear interpolation, but this additional flexibility does not necessarily produce more accurate estimates for every dataset.

## 5. Validation Method

The methods are evaluated by deliberately hiding temperature measurements whose recorded values are known.

For each trial:

1. A consecutive block of temperature readings is selected.
2. The selected readings are temporarily hidden from the interpolation methods.
3. Linear interpolation estimates the hidden temperatures.
4. Cubic spline interpolation estimates the same hidden temperatures.
5. The estimated temperatures are compared with the original recorded values.
6. The prediction errors are collected for evaluation.

The experiment uses a fixed random seed of `42` and performs 100 trials for each gap size.

Three gap sizes are investigated:

- One consecutive hidden reading.
- Three consecutive hidden readings.
- Six consecutive hidden readings.

These gap sizes represent numbers of consecutive measurements rather than guaranteed durations of exactly 10, 30, and 60 minutes, because the actual measurement intervals vary.

### Evaluation Metrics

**Mean Absolute Error (MAE)** measures the average absolute difference between estimated and recorded temperatures.

**Root Mean Square Error (RMSE)** measures the square root of the average squared prediction error, giving greater weight to larger errors.

For both metrics, lower values indicate more accurate estimates relative to the recorded measurements.

## 6. Results

The following results were obtained from the interpolation experiments.

| Consecutive readings hidden | Linear MAE (°C) | Spline MAE (°C) | Linear RMSE (°C) | Spline RMSE (°C) |

| 1 | 0.0655 | 0.0770 | 0.0998 | 0.1014 |
| 3 | 0.0751 | 0.0905 | 0.1041 | 0.1271 |
| 6 | 0.1038 | 0.1349 | 0.1795 | 0.1994 |

### Interpretation

Linear interpolation produced lower MAE and RMSE than cubic spline interpolation for all three tested gap sizes.

Both methods showed increasing prediction errors as the number of consecutive hidden readings increased. This suggests that reconstructing longer gaps is more difficult because more information about the temperature changes within the missing interval is unavailable.

For this dataset and validation procedure, linear interpolation provided the more accurate estimates of the two methods tested.

These findings are specific to the selected sensor, dataset, gap sizes, and validation procedure. They do not establish that linear interpolation will outperform cubic spline interpolation for all environmental datasets.

The project also produces graphs comparing MAE and RMSE and a visual example of the interpolation methods estimating a hidden section of temperature measurements.

## 7. Limitations

Several limitations should be considered when interpreting the results.

- **Recorded measurements are not perfect ground truth.** The validation compares predictions against the sensor's recorded temperatures, which may themselves contain measurement error.
- **The dataset represents one sensor.** Results may differ for other sensors, buildings, or environmental conditions.
- **Measurement intervals vary.** Hiding consecutive readings does not always correspond to an exact time duration.
- **Long gaps may be more difficult to reconstruct.** Rapid temperature changes within a missing interval may not be represented accurately by either method.
- **Only two interpolation methods were compared.** Other numerical methods may produce different results.
- **Validation uses artificially hidden readings.** The experiment evaluates reconstruction where surrounding measurements are available and does not guarantee reliable estimates for every real-world sensor failure.

## 8. Project Files

The main project files are:

| File | Purpose |
|---|---|
| `extract_temperature.py` | Extracts temperature measurements from the original dataset. |
| `prepare_dataset.py` | Cleans and prepares the selected sensor's temperature time series. |
| `sensor_0869_clean.csv` | Cleaned temperature dataset used by the interpolation model. |
| `compare_interpolation.py` | Runs the linear and cubic spline interpolation experiments and calculates error metrics. |
| `interpolation_results.csv` | Stores the interpolation comparison results. |
| `plot_results.py` | Generates the MAE and RMSE comparison graphs. |
| `mae_comparison.png` | Graph comparing MAE for both interpolation methods. |
| `rmse_comparison.png` | Graph comparing RMSE for both interpolation methods. |
| `plot_interpolation_example.py` | Generates a visual example of reconstructing hidden temperature readings. |
| `interpolation_example.png` | Visual example comparing recorded and estimated temperatures. |
| `test_project.py` | Contains basic automated tests for interpolation and error calculations. |
| `requirements.txt` | Lists the required Python packages. |

## 9. Installation and Execution

Python 3 and the packages listed in `requirements.txt` are required.

Install the dependencies using:

python -m pip install -r requirements.txt


Run the scripts from the project directory in the following order when reproducing the workflow from the original dataset:


python extract_temperature.py
python prepare_dataset.py
python interpolation_model.py
python plot_results.py
python plot_interpolation_example.py


The original dataset must be available at the file path expected by the extraction script. Generated CSV files must also be saved where subsequent scripts expect to find them.

Run the automated tests using:


python -m pytest -v test_project.py


The current test suite contains four basic tests covering a known linear interpolation result, MAE calculation, RMSE calculation, and finite interpolation outputs.

These tests check selected numerical operations; they do not constitute comprehensive testing of the entire project pipeline.

## 10. Conclusion

This project applies numerical interpolation to the reconstruction of missing building temperature measurements.

The experimental results show that linear interpolation achieved lower MAE and RMSE than natural cubic spline interpolation for all three tested gap sizes. Prediction errors increased as more consecutive readings were hidden.

Within the scope of this investigation, linear interpolation is a simple and effective method for estimating missing temperature readings. However, the accuracy of either method depends on the characteristics of the temperature data and the length of the missing interval.

The results highlight the importance of validating numerical methods against known measurements before applying them to practical environmental monitoring problems.