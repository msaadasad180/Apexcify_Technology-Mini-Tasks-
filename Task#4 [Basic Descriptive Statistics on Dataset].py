import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")                                            #Load dataset (Iris flowers dataset)

print("First 5 rows:\n", df.head())

print("\nDescriptive Statistics (describe):\n", df.describe())              # Descriptive statistics using describe()

print("\nMean:\n", df.mean(numeric_only=True))                              # Getting required statistics
print("\nMinimum:\n", df.min(numeric_only=True))
print("\nMaximum:\n", df.max(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))
