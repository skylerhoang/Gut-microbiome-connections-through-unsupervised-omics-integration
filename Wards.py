import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram

# Read the CSV file
df = pd.read_csv('input.csv', index_col='patient_id')

# Extract the microbes column
microbes = df.columns[1:]

# Create a distance matrix
distance_matrix = linkage(df[microbes], method='ward')

# Create a dendrogram
dendrogram = dendrogram(distance_matrix)

# Cluster the microbes
clusters = linkage(distance_matrix, 'ward', cutoff=0.5).flatten()

# Add the cluster labels to the dataframe
df['cluster'] = clusters

# Write the clustered dataframe to a new CSV file
df.to_csv('output.csv', index=True)
