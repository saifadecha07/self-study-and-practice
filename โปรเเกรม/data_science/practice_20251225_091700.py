# Session: Reviewing docs before bed
# Note: Need to memorize this syntax.

import pandas as pd

# Source: Kaggle Pandas Tutorial
# Read CSV
df = pd.read_csv('data.csv')

# Display basic info
print(df.head())
print(df.info())
print(df.describe())