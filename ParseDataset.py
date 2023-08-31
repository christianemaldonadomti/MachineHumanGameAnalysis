import json
import re

# Define the regular expression patterns for each data type
patterns = {
    "float": r"'([\\d.]+)'",
    "datetime": r"datetime\\.datetime\\(([\\d, ]+)\\)",
    "location": r"Location\\((\\d+), (\\d+), (\\d+), (\\d+)\\)",
    "tuple": r"\\(([\\d, ]+)\\)",
    "dict": r"\\{([\\d: ,]+)\\}",
    "set": r"set\\(\\[([\\d, ]*)\\]\\)"
}

# Function to parse datetime string to a JSON-compatible string
def parse_datetime(match):
    dt_tuple = tuple(map(int, match.group(1).split(", ")))
    return f"{dt_tuple[0]:04d}-{dt_tuple[1]:02d}-{dt_tuple[2]:02d}T{dt_tuple[3]:02d}:{dt_tuple[4]:02d}:{dt_tuple[5]:02d}.{dt_tuple[6]:06d}"

# Function to parse location string to a dictionary
def parse_location(match):
    return {
        "id": int(match.group(1)),
        "x": int(match.group(2)),
        "y": int(match.group(3)),
        "z": int(match.group(4))
    }

# Function to parse tuple string to a list
def parse_tuple(match):
    return list(map(int, match.group(1).split(", ")))

# Function to parse dictionary string to a dictionary
def parse_dict(match):
    dict_str = match.group(1)
    dict_str = re.sub(r"(\\d+):", r'"\\1":', dict_str)
    return json.loads(f"{{{{dict_str}}}}")

# Function to parse set string to a list
def parse_set(match):
    elements = match.group(1).split(",")
    return list(set(map(int, filter(bool, elements))))

# Function to parse a single entry
def parse_single_entry(lines):
    entry = {}
    for line in lines:
        if re.search(patterns["float"], line):
            entry["float"] = float(re.search(patterns["float"], line).group(1))
        elif re.search(patterns["datetime"], line):
            entry["datetime"] = parse_datetime(re.search(patterns["datetime"], line))
        elif re.search(patterns["location"], line):
            entry["location"] = [parse_location(m) for m in re.finditer(patterns["location"], line)]
        elif re.search(patterns["tuple"], line):
            entry["tuple"] = parse_tuple(re.search(patterns["tuple"], line))
        elif re.search(patterns["dict"], line):
            entry["dict"] = parse_dict(re.search(patterns["dict"], line))
        elif re.search(patterns["set"], line):
            entry["set"] = parse_set(re.search(patterns["set"], line))
    return entry

# Function to parse multiple entries from a large file
def parse_large_file(file_path):
    parsed_entries = []
    temp_lines = []
    
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # Ignore empty lines
                temp_lines.append(line)
                
                # If all fields are filled, parse the entry and clear temp_lines
                if all(re.search(pattern, "\\n".join(temp_lines)) for pattern in patterns.values()):
                    parsed_entry = parse_single_entry(temp_lines)
                    parsed_entries.append(parsed_entry)
                    temp_lines = []
    
    return parsed_entries

# File path (replace this with the path to your large file)
file_path = "/path/to/your/large_file.txt"

# Parse multiple entries from the large file
parsed_entries_from_file = parse_large_file(file_path)

# Convert to JSON format
json_data_from_file = json.dumps(parsed_entries_from_file, indent=4)
