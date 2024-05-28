import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the provided dictionary and save it to the specified file in JSON format.
    
    :param data: A Python Dictionary with data to be serialized
    :param filename: The filename of the output JSON file. If the output file already exists, it should be replaced.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from the specified file into a Python dictionary.
    
    :param filename: The filename of the input JSON file
    :return: A Python dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)

# Test the functions
if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)

