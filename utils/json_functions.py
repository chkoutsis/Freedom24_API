import json
import os
from typing import List


class JsonHandler:
    """A class to handle JSON file creation and saving."""

    def __init__(self, data_dir: str = None):
        """
        Initializes the JsonHandler with a specified data directory.

        Args:
        - data_dir (str): The directory where JSON files will be saved. Defaults to a 'data' directory two levels up from the script.
        """
        # Set the data directory to the specified path or create a 'data' directory two levels up from the script
        # If the specified path does not exist, create it
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = data_dir or os.path.abspath(
            os.path.join(script_dir, "..", "data")
        )
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def save_json(self, json_string: str, filename: str = "data.json") -> None:
        """
        Saves a JSON string to a specified file in the data directory.

        Args:
        - json_string (str): A JSON string to be saved into a file.
        - filename (str): The name of the file to save the JSON string. Defaults to 'data.json'.

        Returns:
        - None
        """
        # Create the full file path by joining the data directory and the filename
        # Open the file in write mode and save the JSON string to it
        file_path = os.path.join(self.data_dir, filename)
        with open(file_path, "w") as file:
            file.write(json_string)

    def create_json(
        self,
        trading_account_user_info: List,
        filename: str = "data.json",
    ) -> str:
        """
        Creates a JSON structure with Trading Account information and saves it to a file.

        Args:
        - trading_account_user_info (list): A list containing dictionaries with trading account details.
        - filename (str): The name of the file to save the JSON string. Defaults to 'data.json'.

        Returns:
        - str: A string representation of the generated JSON.
        """
        # Create a dictionary to hold the data
        json_data = {
            "trading_account": trading_account_user_info,
        }
        # Convert the dictionary to a JSON string with indentation for readability
        # and save it to a file
        json_string = json.dumps(json_data, indent=4)
        self.save_json(json_string, filename)

        return json_string
