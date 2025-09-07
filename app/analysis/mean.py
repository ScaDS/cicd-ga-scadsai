import pandas as pd


def compute(series: pd.Series) -> float:
    """Compute the mean of a pandas Series.

    Args:
        series (pd.Series): Input series to compute the mean.

    Returns:
        float: The mean of the series.

    """
    return series.mean()
