
import json
from datetime import datetime
from collections import Counter
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Function to identify connections between nodes based on 'z' values
def identify_connections(locations):
    sorted_locations = sorted(locations, key=lambda x: x['z'])
    connections = []
    for i in range(len(sorted_locations) - 1):
        for j in range(i + 1, len(sorted_locations)):
            connections.append((sorted_locations[i]['id'], sorted_locations[j]['id']))
    return connections

# Load the data
with open('your_dataset.json', 'r') as f:
    data_full = json.load(f)

# Convert datetime strings to datetime objects for easier manipulation
for entry in data_full:
    entry['datetime'] = datetime.fromisoformat(entry['datetime'])

# Initialize counters for features
node_counter = Counter()
connection_counter = Counter()
tuple_counter = Counter()
dict_key_counter = Counter()

# Populate counters with data from the full dataset
for entry in data_full:
    node_counter.update([loc['z'] for loc in entry['location']])
    connections = identify_connections(entry['location'])
    connection_counter.update(connections)
    tuple_counter.update(entry['tuple'])
    dict_key_counter.update(entry['dict'].keys())

# Create feature vectors for each game step (aggregated)
node_frequencies = []
connection_frequencies = []
tuple_frequencies = []
dict_key_frequencies = []
for entry in data_full:
    node_frequencies.append(sum([node_counter[loc['z']] for loc in entry['location']]))
    connections = identify_connections(entry['location'])
    connection_frequencies.append(sum([connection_counter[conn] for conn in connections]))
    tuple_frequencies.append(sum([tuple_counter[t] for t in entry['tuple']]))
    dict_key_frequencies.append(sum([dict_key_counter[k] for k in entry['dict'].keys()]))

# Create a NumPy array to hold the aggregated features
X_aggregated = np.array([node_frequencies, connection_frequencies, tuple_frequencies, dict_key_frequencies]).T

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_aggregated)

# Perform PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X_pca)

# Create a DataFrame to store the data and cluster labels
df = pd.DataFrame(data_full)
df['cluster'] = kmeans.labels_

# Visualize the clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='x')
plt.show()
