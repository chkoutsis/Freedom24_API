import json
import os


def save_json(json_string):
    """
    Saves a JSON string to a file named 'data.json' in a 'data' directory.

    Args:
    - json_string (str): A JSON string to be saved into a file.

    Returns:
    - None
    """
    # Get the directory of the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Move up two directories to reach the desired location for data.json
    desired_dir = os.path.abspath(os.path.join(script_dir, '..', 'data'))

    # Check if the directory exists; if not, create it
    if not os.path.exists(desired_dir):
        os.makedirs(desired_dir)

    # Define the path for data.json
    file_path = os.path.join(desired_dir, 'data.json')

    # Save the JSON string to a file
    with open(file_path, 'w') as file:
        file.write(json_string)


def create_json(d_account_user_info, trading_account_user_info):
    """
    Creates a JSON structure combining D Account and Trading Account information and saves it to a file.

    Args:
    - d_account_user_info (list): A list containing a dictionary with 'EUR' and 'USD' keys, representing the respective balances.
    - trading_account_user_info (list): A list containing dictionaries with trading account details.

    Returns:
    - str: A string representation of the generated JSON.
    """
    # Construct a JSON structure using collected user information
    json_data = {
        "d_account": d_account_user_info,  
        "trading_account": trading_account_user_info  
    }

    # Convert the JSON data into a formatted string with indentation for readability
    json_string = json.dumps(json_data, indent=4)

    save_json(json_string)
    return json_string