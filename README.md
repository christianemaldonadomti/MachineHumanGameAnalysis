# Game Strategy Analysis

This repository contains Python code to analyze player strategies in a computer game. The game involves players visiting and connecting nodes on a map. The code uses machine learning techniques to cluster similar strategies together, providing insights into player behavior.

---

## Game Play Analysis and Clustering

This Python script offers an in-depth analysis of game plays by clustering them based on specific features. The primary purpose is to identify patterns and similarities among different games by leveraging machine learning techniques.

### Features:

1. **Drive Integration**: Uses Google Colab's drive integration to fetch game data stored on Google Drive.
2. **Data Collection**: Iterates through JSON files in a specified directory to gather game data.
3. **Game Analysis**:
   - **Node Revisits**: Analyzes how often nodes are revisited in each play.
   - **Node Weights**: Computes the average weight of nodes in each play.
   - **Time Intervals**: Measures the time intervals between consecutive game plays.
4. **K-means Clustering**: Employs the K-means algorithm to cluster game plays based on the three features mentioned above. By default, it clusters the plays into three categories.
5. **Similarity Measurement**: Uses cosine similarity to measure the similarity between different game plays.
6. **Heatmap Visualization**: Displays a heatmap showcasing the normalized cosine similarity between games, providing a visual representation of how different games are related to each other.

### Instructions:

1. Ensure you have all the required libraries installed.
2. Set the `folder_path` variable to the directory containing your JSON game files.
3. If you know of any outliers in your game data, add their numbers to the `outliers` list.
4. Run the script in a Google Colab environment or adjust the drive integration accordingly for other platforms.
5. Observe the heatmap generated at the end of the script to gain insights into game play similarities.

### Output:

A heatmap will be generated showcasing the normalized cosine similarity between different games. Darker shades represent higher similarity, while lighter shades indicate less similarity.

### Dependencies:

- `sklearn`: For clustering and similarity measurement.
- `numpy`: For numerical operations.
- `json`: For reading JSON files.
- `os`: For directory and file operations.
- `collections`: For advanced data structures like defaultdict.
- `datetime`: For parsing and calculating time intervals.
- `matplotlib`: For visualization and plotting.
- `pandas`: For data manipulation and analysis.
- `seaborn`: For advanced visualization, particularly the heatmap.

---

To use this script, it's recommended to have a basic understanding of Python programming, clustering techniques, and the libraries mentioned above. Adjustments might be necessary based on your specific data structure and requirements.


