import credentials.api_credentials as cred
from utils.account_functions import (get_d_account_user_info,
                                     get_trading_account_user_info)
from utils.json_functions import create_json


def run():    
    # Retrieve D Account user information using the D Account API access
    d_account_info = get_d_account_user_info(cred.d_account_api_access)

    # Retrieve Trading Account user information using the Trading Account API access
    trading_account_info = get_trading_account_user_info(cred.trading_account_api_access)

    # Create a JSON file using the collected account information
    create_json(d_account_info, trading_account_info)
    
if __name__ == '__main__':
    run()