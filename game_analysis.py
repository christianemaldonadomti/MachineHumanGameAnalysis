# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import os
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Replace with your Google Drive folder path containing the JSON files
folder_path = <<.../plays>>

# Initialize a dictionary to store clustering results for each game
clustering_results = {}

# Loop through each JSON file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), 'r') as f:
            game_data = json.load(f)

        # Debugging: Check if game_data is empty or not
        if not game_data:
            print(f"Warning: {filename} appears to be empty or not in the expected format.")
            continue

        # Initialize data structures for node revisits, node weights, and time intervals
        node_visits = defaultdict(int)
        revisits_per_play = []
        average_weight_per_play = []
        time_intervals = []

        # Initialize previous_datetime variable for time interval calculation
        previous_datetime = None

        # Analyze each play
        for play in game_data:
            # Node Revisits
            active_nodes = play['tuple']
            revisits_this_play = 0
            for node in active_nodes:
                if node_visits[node] > 0:
                    revisits_this_play += 1
                node_visits[node] += 1
            revisits_per_play.append(revisits_this_play)

            # Node Weights
            total_weight_this_play = 0
            for node in active_nodes:
                weight = next((location['z'] for location in play['location'] if location['id'] == node), 0)
                total_weight_this_play += weight
            average_weight_this_play = total_weight_this_play / len(active_nodes) if active_nodes else 0
            average_weight_per_play.append(average_weight_this_play)

            # Time Intervals
            current_datetime = datetime.fromisoformat(play['datetime'])
            if previous_datetime:
                time_interval = (current_datetime - previous_datetime).total_seconds()
                time_intervals.append(time_interval)
            previous_datetime = current_datetime

        # Debugging: Check if lists are populated
        if not (revisits_per_play and average_weight_per_play and time_intervals):
            print(f"Warning: Data lists are not populated for {filename}. Skipping clustering.")
            continue

        # Create feature vectors for clustering (ensure equal lengths)
        min_length = min(len(revisits_per_play), len(average_weight_per_play), len(time_intervals))

        # Debugging: Check if min_length is zero
        if min_length == 0:
            print(f"Warning: Feature vectors have zero length for {filename}. Skipping clustering.")
            continue

        feature_vectors = np.array([
            revisits_per_play[:min_length],
            average_weight_per_play[:min_length],
            time_intervals[:min_length]
        ]).T

        # Perform k-means clustering with k=3
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        kmeans.fit(feature_vectors)
        cluster_means = np.mean(kmeans.cluster_centers_, axis=0)

        # Store the clustering results
        clustering_results[filename] = cluster_means


# Extract the numbers from the filenames and sort them
sorted_keys = sorted(clustering_results.keys(), key=lambda x: int(x.split("j")[1].split("_")[0]))

# Reorder the clustering_results dictionary based on the sorted keys
sorted_clustering_results = {key: clustering_results[key] for key in sorted_keys}

# Create the similarity matrix and DataFrame as before, but with sorted keys
games = [int(key.split("j")[1].split("_")[0]) for key in sorted_keys]
features = np.array([sorted_clustering_results[key] for key in sorted_keys])

# Calculate the similarity matrix
similarity_matrix = cosine_similarity(features)

# Create the DataFrame
similarity_df = pd.DataFrame(similarity_matrix, index=games, columns=games)

from sklearn.preprocessing import MinMaxScaler

# Assuming that games with numbers 10 and 11 are outliers, you can adjust this accordingly
outliers = [1, 2,3,4,5,6, 7, 9, 33]
outliers = [1,7]
# Remove outliers
filtered_similarity_df = similarity_df.drop(outliers, axis=0).drop(outliers, axis=1)

# Normalize the data
scaler = MinMaxScaler()
normalized_matrix = scaler.fit_transform(filtered_similarity_df)
normalized_similarity_df = pd.DataFrame(normalized_matrix, index=filtered_similarity_df.index, columns=filtered_similarity_df.columns)

# Create the heatmap using Seaborn
plt.figure(figsize=(48, 48))


import matplotlib.colors as mcolors

# Create a custom color map with lighter shades
colors = ["#ffffff", "#f0f0f0", "#d9d9d9", "#bdbdbd", "#969696", "#737373", "#525252", "#252525"]
cmap = mcolors.LinearSegmentedColormap.from_list("Custom", colors, N=256)

# Create the heatmap
sns.heatmap(normalized_similarity_df, annot=True, cmap=cmap, annot_kws={"size": 10}, fmt=".2f")
plt.xticks(fontsize=10, rotation=90)
plt.yticks(fontsize=10, rotation=0)
plt.title('Normalized Cosine Similarity Between Games', fontsize=44)
plt.show()
