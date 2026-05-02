# Session: Late night coding
# Note: Finally understood this concept!

import pandas as pd
import numpy as np

# Source: Towards Data Science - Data Cleaning
# Handling missing values
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})

# Fill missing values
df.fillna(value=0, inplace=True)
print(df)