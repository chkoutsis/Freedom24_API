import configparser
from typing import Tuple

from cryptography.fernet import Fernet


class ConfigLoader:
    """A class to load and decrypt configuration files for trading account."""

    def __init__(self, main_config_path: str = "C:\\AppConfigs\\Freedom24"):
        """
        Initializes the ConfigLoader with the main configuration path.

        Args:
        - main_config_path (str): The base path for the configuration files.
        """
        self.main_config_path = main_config_path

    def load_decrypted_config(self, file_path: str) -> Tuple[str, str, str, str]:
        """
        Loads and decrypts the configuration file using the provided file path.

        Args:
        - file_path (str): The path to the encrypted configuration file.

        Returns:
        - Tuple: A tuple containing login, password, public_key, and private_key.
        """
        # Read the encryption key from the file
        with open(file_path + "_key.key", "rb") as key_file:
            key = key_file.read()

        # Read the encrypted data from the file
        with open(file_path + "_encrypted_config.bin", "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Create a Fernet cipher suite using the key and decrypt the data
        cipher_suite = Fernet(key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        config_string = decrypted_data.decode("utf-8")

        # Parse the decrypted data using configparser
        config = configparser.ConfigParser()
        config.read_string(config_string)

        # Extract the keys from the config
        public_key = config["KEYS"]["public_key"]
        private_key = config["KEYS"]["private_key"]
        login = config["KEYS"]["login"]
        password = config["KEYS"]["password"]

        return (
            public_key,
            private_key,
            login,
            password,
        )

    def load_all_configs(
        self,
    ) -> Tuple[str, str, str, str]:
        """
        Loads and decrypts the configuration for the trading account.

        Returns:
        - Tuple: A tuple with login, password, public_key, and private_key.
        """
        # Define the path for the trading account configuration file
        trading_account = self.main_config_path + "\\trading_account"

        # Load and decrypt the configuration for the trading account
        trading_account_config = self.load_decrypted_config(trading_account)

        return trading_account_config
