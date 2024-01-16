import json
import os

# Define a function to modify the JSON file
def modify_json_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Open and read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Modify the 'encode_decode' field
    if data.get('encode_decode') == 'decode':
        data['encode_decode'] = 'encode'
    elif data.get('encode_decode') == 'encode':
        data['encode_decode'] = 'decode'
    else:
        print("Invalid 'encode_decode' value.")
        return

    # Save the modified data to 'input.json'
    with open('input.json', 'w') as new_file:
        json.dump(data, new_file, indent=4)

    # Remove the old file if it's different from the input file
    if file_path != 'input.json':
        os.remove(file_path)

    print("File modified and saved as 'input.json'.")

# Example usage
modify_json_file('output.json')
