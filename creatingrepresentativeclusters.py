import numpy as np
import pandas as pd

def compute_representative_vectors(df, cluster_labels):
  """Computes representative vectors of means for each cluster.

  Args:
    df: A Pandas DataFrame containing the omics data.
    cluster_labels: A NumPy array containing the cluster labels for each sample.

  Returns:
    A Pandas DataFrame containing the representative vectors of means for each cluster.
  """

  # Create a new DataFrame to store the representative vectors of means.
  representative_vectors = pd.DataFrame()

  # Iterate over the clusters.
  for cluster_label in np.unique(cluster_labels):

    # Get the indexes of the samples in the current cluster.
    cluster_indexes = np.where(cluster_labels == cluster_label)[0]

    # Get the mean abundance of each microbe in the current cluster.
    cluster_means = df.iloc[cluster_indexes].mean()

    # Add the cluster mean to the representative vectors DataFrame.
    representative_vectors[cluster_label] = cluster_means

  return representative_vectors

# Get the clustered dataframe.
df_clustered = df.copy()
df_clustered['cluster'] = cluster_labels

# Compute the representative vectors of means for each cluster.
representative_vectors = compute_representative_vectors(df_clustered, cluster_labels)

# Save the representative vectors DataFrame to a CSV file.
representative_vectors.to_csv('representative_vectors.csv', index=False)
