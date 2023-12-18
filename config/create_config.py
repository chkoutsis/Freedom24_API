import configparser
import getpass
import os


def create_config_file(account_type):
    """
    Creates a configuration file for a specific account type.

    Args:
    - account_type (str): The type of account ('Trading' or 'D') for which the configuration file will be created.

    Returns:
    - None
    """
    account_types = {
        'Trading': 'trading_account_config.ini',
        'D': 'd_account_config.ini'
    }

    config_file_path = os.path.join('C:\\AppConfigs\\Freedom24', account_types.get(account_type, 'config.ini'))

    # Get user input for keys
    login = input(f"Enter {account_type} Account login: ")
    password = getpass.getpass(f"Enter {account_type} Account password: ")
    public_key = input(f"Enter {account_type} Account public key: ")
    private_key = getpass.getpass(f"Enter {account_type} Account private key: ")

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Add keys to the 'KEYS' section
    config['KEYS'] = {
        'login': login,
        'password': password,
        'public_key': public_key,
        'private_key': private_key
    }

    # Write the configuration data to a file
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    print(f"{account_type} Account Config file created successfully!")


def run():
    # Define the directory path
    directory = r'C:\AppConfigs\Freedom24'

    # Check if the directory exists; if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")

    # Trading Account
    create_config_file('Trading')

    # D Account
    create_config_file('D')

if __name__ == '__main__':
    run()