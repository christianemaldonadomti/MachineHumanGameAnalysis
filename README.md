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

## Data Preparation

### Overview:

The provided code is designed to extract and structure data from a large, unstructured file containing complex data types that are not natively JSON serializable. The primary objective is to convert these data types into a structured JSON format, making it easier to further process or analyze them.

### Method:

1. **Define Regular Expressions**: The script starts by defining regular expression patterns for each data type to recognize and extract the relevant information.
2. **Parsing Functions**: A set of parsing functions (`parse_datetime`, `parse_location`, `parse_tuple`, `parse_dict`, `parse_set`) are defined to convert the matched strings of each data type into a JSON-compatible format.
3. **Single Entry Parsing**: The `parse_single_entry` function takes a set of lines (representing a single entry) and identifies the data type present in each line. It then calls the appropriate parsing function to convert the data.
4. **Large File Parsing**: The `parse_large_file` function reads the large file line by line. For each entry, it accumulates lines until all fields of an entry are identified. It then invokes the `parse_single_entry` function and appends the parsed result to the `parsed_entries` list.
5. **File to JSON Conversion**: After parsing all entries from the file, the data is converted to a JSON format using the `json.dumps` function.

### How to Use:

1. **Set the File Path**: Replace the placeholder `file_path` with the path to the unstructured file you wish to process.
   ```python
   file_path = <</path/to/your/file.txt>>
   ```
2. **Run the Script**: Execute the entire script. 
3. **Output**: At the end of the script, `json_data_from_file` will contain the parsed data in a structured JSON format. You can save this to a new file or use it for further processing.
4. **Dataset completion**  Run over all files.

### Recommendations:

- Ensure the unstructured file adheres to the expected formats for each data type. If there are variations or additional data types, you may need to adjust the regular expressions or add new parsing functions.
- Always backup your original data file before running any parsing or data transformation scripts on it to prevent accidental data loss or corruption.
- Test the script on a small subset of your data first to ensure it works as expected before processing the entire file.


