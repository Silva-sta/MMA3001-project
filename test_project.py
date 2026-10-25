
import numpy as np


def test_linear_interpolation():
    """Check that linear interpolation gives the expected midpoint."""
    result = np.interp(
        [5],
        [0, 10],
        [20, 30]
    )

    assert result[0] == 25


def test_mae_calculation():
    """Check that mean absolute error is calculated correctly."""
    actual = np.array([10, 20, 30])
    predicted = np.array([12, 18, 30])

    mae = np.mean(np.abs(predicted - actual))

    assert mae == 4 / 3


def test_rmse_calculation():
    """Check that root mean square error is calculated correctly."""
    actual = np.array([10, 20])
    predicted = np.array([11, 18])

    rmse = np.sqrt(np.mean((predicted - actual) ** 2))

    assert np.isclose(rmse, np.sqrt(2.5))


def test_interpolation_values_are_finite():
    """Check that interpolation produces finite numerical values."""
    result = np.interp(
        [2, 5, 8],
        [0, 10],
        [20, 30]
    )

    assert np.all(np.isfinite(result))