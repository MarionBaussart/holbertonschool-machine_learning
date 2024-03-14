#!/usr/bin/env python3
"""
module containing function from_file
"""
import pandas as pd


def from_file(filename, delimiter):
    """
    function that loads data from a file as a pd.DataFrame
    Args:
        filename: file to load from
        delimiter: column separator
    Return:
        df: the loaded pd.DataFrame
    """
    df = pd.read_csv(filepath_or_buffer=filename, sep=delimiter)

    return df
