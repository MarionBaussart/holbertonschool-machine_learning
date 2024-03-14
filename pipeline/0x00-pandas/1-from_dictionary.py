#!/usr/bin/env python3
"""
python script that created a pd.DataFrame from a dictionary
"""
import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "First": np.arange(0.0, 2.0, 0.5),
        "Second": ["one", "two", "three", "four"]
    },
    index=list("ABCD")
)
