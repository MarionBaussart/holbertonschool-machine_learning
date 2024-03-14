#!/usr/bin/env python3
"""
module containing function from_numpy
"""
import pandas as pd


def from_numpy(array):
    """
    function that creates a pd.DataFrame from a np.ndarray
    Args:
        array: np.ndarray from which you should create the pd.DataFrame
    Return:
        df: the newly created pd.DataFrame
    """
    df = pd.DataFrame(array)
    df.columns = [chr(ord('a') + x).upper() for x in df.columns]
    pd.options.display.max_rows = 26

    return df
