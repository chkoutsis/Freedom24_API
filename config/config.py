import configparser

from cryptography.fernet import Fernet


def load_decrypted_config(file_path):
    """
    Loads and decrypts the configuration file using the provided file path.

    Args:
    - file_path (str): The path to the encrypted configuration file.

    Returns:
    - tuple: A tuple containing login, password, public_key and private_key.
    """
    with open(file_path + '_key.key', 'rb') as key_file:
        key = key_file.read()

    with open(file_path + '_encrypted_config.bin', 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    config_string = decrypted_data.decode('utf-8')

    config = configparser.ConfigParser()
    config.read_string(config_string)

    login = config['KEYS']['login']
    password = config['KEYS']['password']
    public_key = config['KEYS']['public_key']
    private_key = config['KEYS']['private_key']

    return login, password, public_key, private_key

# Trading Account
trading_login, trading_password, trading_public_key, trading_private_key = load_decrypted_config('C:\\AppConfigs\\Freedom24\\trading_account')

# D Account
d_login, d_password, d_public_key, d_private_key = load_decrypted_config('C:\\AppConfigs\\Freedom24\\d_account')