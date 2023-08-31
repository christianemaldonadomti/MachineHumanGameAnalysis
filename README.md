# Game Strategy Analysis

This repository contains Python code to analyze player strategies in a computer game. The game involves players visiting and connecting nodes on a map. The code uses machine learning techniques to cluster similar strategies together, providing insights into player behavior.

## Data Format

The data should be in a JSON file, where each entry represents a game step and contains the following fields:

- `datetime`: The timestamp of the game step.
- `location`: A list of dictionaries, each representing a node. Each dictionary contains an `id` and a `z` value representing the node's ID and type, respectively.
- `tuple`: A list of integers or floats, representing some game metrics.
- `dict`: A dictionary containing additional game metrics.

Example:

```json
[
    {
        "datetime": "2022-01-01T12:00:00",
        "location": [
            {"id": 1, "z": 1},
            {"id": 2, "z": 2}
        ],
        "tuple": [1, 2, 3],
        "dict": {"key1": "value1", "key2": "value2"}
    },
    ...
]
How to Run
Replace 'your_dataset.json' 
