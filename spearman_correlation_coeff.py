import numpy as np
import pandas as pd
from scipy.stats import spearmanr

def spearman_correlation(df1, df2):
  """Computes the Spearman's correlation coefficient between two DataFrames.

  Args:
    df1: A Pandas DataFrame containing the first vector.
    df2: A Pandas DataFrame containing the second vector.

  Returns:
    A NumPy array containing the Spearman's correlation coefficient.
  """

  # Get the correlation coefficient.
  r_spearman, p_value = spearmanr(df1, df2)

  return r_spearman

# Get a list of all the representative vector CSV files.
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Create a new DataFrame to store the Spearman's correlation coefficients.
correlation_matrix = pd.DataFrame(columns=['vector_1', 'vector_2', 'spearman_correlation'])

# Iterate over the CSV files.
for i in range(len(csv_files)):
  for j in range(i + 1, len(csv_files)):

    # Read the CSV files.
    df1 = pd.read_csv(csv_files[i])
    df2 = pd.read_csv(csv_files[j])

    # Compute the Spearman's correlation coefficient between the two DataFrames.
    r_spearman = spearman_correlation(df1, df2)

    # Add the correlation coefficient to the correlation matrix DataFrame.
    correlation_matrix = correlation_matrix.append({'vector_1': csv_files[i], 'vector_2': csv_files[j], 'spearman_correlation': r_spearman}, ignore_index=True)

# Save the correlation matrix DataFrame to a CSV file.
correlation_matrix.to_csv('correlation_matrix.csv', index=False)
