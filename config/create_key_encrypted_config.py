import os

from cryptography.fernet import Fernet


def encrypt_config(original_file, key_file, encrypted_file):
    """
    Encrypts the content of the configuration file and stores the encrypted data in a separate file.

    Args:
    - original_file (str): Path to the original configuration file.
    - key_file (str): Path to save the encryption key.
    - encrypted_file (str): Path to save the encrypted configuration data.

    Returns:
    - None
    """
    # Generate a key for encryption and decryption
    key = Fernet.generate_key()

    # Save the key to a file for later decryption
    with open(key_file, 'wb') as key_file:
        key_file.write(key)

    # Read the content of the configuration file
    with open(original_file, 'rb') as file:
        config_data = file.read()

    # Encrypt the configuration file content
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(config_data)

    # Write the encrypted content to a new file
    with open(encrypted_file, 'wb') as encrypted_file:
        encrypted_file.write(cipher_text)

    # Delete the original configuration file
    if os.path.exists(original_file):
        os.remove(original_file)
        print(f"File {original_file} deleted successfully.")
    else:
        print(f"File {original_file} does not exist.")

def run():
    # Trading Account
    encrypt_config('C:\\AppConfigs\\Freedom24\\trading_account_config.ini', 'C:\\AppConfigs\\Freedom24\\trading_account_key.key', 'C:\\AppConfigs\\Freedom24\\trading_account_encrypted_config.bin')

    # D Account
    encrypt_config('C:\\AppConfigs\\Freedom24\\d_account_config.ini', 'C:\\AppConfigs\\Freedom24\\d_account_key.key', 'C:\\AppConfigs\\Freedom24\\d_account_encrypted_config.bin')

if __name__ == '__main__':
    run()