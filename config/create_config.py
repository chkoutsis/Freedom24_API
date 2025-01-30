import getpass
import os

from cryptography.fernet import Fernet


def encrypt_data(data):
    """
    Encrypts the provided data using Fernet encryption.

    Args:
    - data (bytes): Data to be encrypted.

    Returns:
    - (bytes): Encrypted data.
    - (bytes): Encryption key used to encrypt the data.
    """
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    
    return encrypted_data, key

def create_and_encrypt_config(account_type, login, password):
    """
    Creates a configuration, encrypts it, and saves the encrypted file and key.
    Skips if the encrypted file already exists.

    Args:
    - account_type (str): The type of account ('Trading' or 'D').
    - login (str): Login for the accounts.
    - password (str): Password for the accounts.

    Returns:
    - None
    """
    account_types = {
        'Trading': 'trading_account',
        'D': 'd_account'
    }

    # Define paths for the encrypted files
    directory = 'C:\\AppConfigs\\Freedom24'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Paths for the encrypted files
    encrypted_config_file = os.path.join(directory, f"{account_types[account_type]}_encrypted_config.bin")
    key_file = os.path.join(directory, f"{account_types[account_type]}_key.key")

    # Check if the encrypted config file and key file already exist
    if os.path.exists(encrypted_config_file) and os.path.exists(key_file):
        print(f"\n{account_type} Account encrypted config already exists.")
        return

    # Get user input for the specific account keys
    public_key = input(f"\nEnter {account_type} Account public key: ")
    private_key = getpass.getpass(f"Enter {account_type} Account private key: ")

    # Manually build the configuration string
    config_string = f"""[KEYS]
    login = {login}
    password = {password}
    public_key = {public_key}
    private_key = {private_key}
    """

    # Encrypt the configuration data and get the encryption key
    encrypted_config, encryption_key = encrypt_data(config_string.encode())

    # Save the encrypted data to the encrypted file
    with open(encrypted_config_file, 'wb') as enc_file:
        enc_file.write(encrypted_config)

    # Save the encryption key
    with open(key_file, 'wb') as key_f:
        key_f.write(encryption_key)

    print(f"{account_type} Account config encrypted and saved successfully!")

def run():
    # Get login and password
    login = input("\nEnter Account login: ")
    password = getpass.getpass("Enter Account password: ")

    # Create and encrypt configuration for Trading and D accounts
    create_and_encrypt_config('Trading', login, password)
    create_and_encrypt_config('D', login, password)

if __name__ == '__main__':
    run()
