import getpass
import logging
import os
from typing import Tuple

from cryptography.fernet import Fernet


class ConfigCreator:
    """A class to create and encrypt configuration files for trading account."""

    def __init__(self, main_config_path: str = "C:\\AppConfigs\\Freedom24"):
        """
        Initializes the ConfigCreator with the main config path for configuration files.

        Args:
        - main_config_path (str): The base main_config_path for storing encrypted configuration files.
        """
        self.main_config_path = main_config_path
        if not os.path.exists(self.main_config_path):
            os.makedirs(self.main_config_path)
            logging.info(f"Created main config directory at {self.main_config_path}.")
        else:
            logging.info(
                f"Using existing main config directory at {self.main_config_path}."
            )

    def encrypt_data(self, data: bytes) -> Tuple[bytes, bytes]:
        """
        Encrypts the provided data using Fernet encryption.

        Args:
        - data (bytes): Data to be encrypted.

        Returns:
        - tuple: Encrypted data and the encryption key.
        """
        try:
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)
            encrypted_data = cipher_suite.encrypt(data)
            logging.info("Data encrypted successfully.")
            return encrypted_data, key
        except Exception as e:
            logging.error(f"Failed to encrypt data: {e}", exc_info=True)
            raise

    def create_and_encrypt_config(
        self, account_type: str, login: str, password: str
    ) -> None:
        """
        Creates a configuration, encrypts it, and saves the encrypted file and key.
        Skips if the encrypted file already exists.

        Args:
        - account_type (str): The type of account ('Trading' or 'D').
        - login (str): Login for the accounts.
        - password (str): Password for the accounts.
        """
        account_types = {"Trading": "trading_account"}
        encrypted_config_file = os.path.join(
            self.main_config_path, f"{account_types[account_type]}_encrypted_config.bin"
        )
        key_file = os.path.join(
            self.main_config_path, f"{account_types[account_type]}_key.key"
        )

        if os.path.exists(encrypted_config_file) and os.path.exists(key_file):
            logging.info(
                f"{account_type} Account encrypted config already exists. Skipping."
            )
            return

        try:
            public_key = input(f"\nEnter {account_type} Account public key: ")
            private_key = getpass.getpass(f"Enter {account_type} Account private key: ")

            config_string = f"""[KEYS]
            login = {login}
            password = {password}
            public_key = {public_key}
            private_key = {private_key}
            """

            encrypted_config, encryption_key = self.encrypt_data(config_string.encode())

            with open(encrypted_config_file, "wb") as enc_file:
                enc_file.write(encrypted_config)
                logging.info(f"Encrypted config saved to {encrypted_config_file}.")

            with open(key_file, "wb") as key_f:
                key_f.write(encryption_key)
                logging.info(f"Encryption key saved to {key_file}.")

            logging.info(
                f"{account_type} Account config encrypted and saved successfully!"
            )

        except Exception as e:
            logging.error(
                f"Failed to create and encrypt {account_type} Account config: {e}",
                exc_info=True,
            )

    def run(self):
        """
        Main function to execute the script.

        This function retrieves user credentials and creates encrypted configuration files
        for Trading account. It prompts the user for login and password, and
        generates an encrypted configuration file.
        """
        try:
            logging.info("Starting configuration creation process.")
            login = input("\nEnter Account login: ")
            password = getpass.getpass("Enter Account password: ")

            self.create_and_encrypt_config("Trading", login, password)

            logging.info("Configuration creation process completed successfully.")
        except Exception as e:
            logging.error(
                f"An error occurred during the configuration creation process: {e}",
                exc_info=True,
            )


def setup_logging():
    """
    Configures the logging settings for the script.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Set to DEBUG for more detailed logs
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


if __name__ == "__main__":
    setup_logging()
    creator = ConfigCreator()
    creator.run()
