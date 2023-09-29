import matplotlib.pyplot as plt

# Get the dendrogram coordinates
dendrogram_coords = dendrogram(distance_matrix, no_plot=True)

# Create a figure
fig, ax = plt.subplots()

# Plot the dendrogram
ax.plot(dendrogram_coords['leaves'], dendrogram_coords['ivl'], 'k', linewidth=2)

# Set the axis labels and title
ax.set_xlabel('Microbes')
ax.set_ylabel('Distance')
ax.set_title('Dendrogram of Clustered Microbes')

# Show the plot
plt.show()
