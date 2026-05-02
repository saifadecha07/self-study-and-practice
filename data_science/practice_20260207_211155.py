# Session: Morning study session
# Note: Finally understood this concept!

import pandas as pd

# Source: Kaggle Pandas Tutorial
# Read CSV
df = pd.read_csv('data.csv')

# Display basic info
print(df.head())
print(df.info())
print(df.describe())