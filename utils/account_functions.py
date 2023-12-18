from tradernet import TraderNetAPI


def get_api_access(public_key, private_key, login, password):
    """
    Creates and returns an instance of TraderNetAPI to access the API.

    Args:
    - public_key (str): The public key for authentication.
    - private_key (str): The private key for authentication.
    - login (str): The login for authentication.
    - password (str): The password for authentication.

    Returns:
    - TraderNetAPI: An instance of TraderNetAPI initialized with the provided credentials.
    """
    return TraderNetAPI(public_key, 
                        private_key, 
                        login, 
                        password)


def get_d_account_user_info(api_access):
    """
    Retrieves the EUR and USD Account balances for a user via TraderNetAPI.

    Args:
    - api_access (TraderNetAPI): An instance of TraderNetAPI for accessing user account information.

    Returns:
    - list: A list containing a dictionary with 'EUR' and 'USD' keys, representing the respective balances.
    """
    eur_amount = TraderNetAPI.account_summary(api_access)['result']['ps']['acc'][0]['s']
    usd_amount = TraderNetAPI.account_summary(api_access)['result']['ps']['acc'][1]['s']

    data = {'EUR': eur_amount,
            'USD': usd_amount
    }
    return [data]


def get_trading_account_user_info(api_access):
    """
    Retrieves Trading Account information for a user via TraderNetAPI.

    Args:
    - api_access (TraderNetAPI): An instance of TraderNetAPI for accessing user account information.

    Returns:
    - list: A list containing dictionaries with trading account details.
    """
    all_data = []
    positions = TraderNetAPI.account_summary(api_access)['result']['ps']['pos']

    for i in range(len(positions)):
        data = {
            'Ticker': positions[i]['base_contract_code'],
            'Qty': positions[i]['q'],
            'Entry Price': float(f"{positions[i]['price_a']:.2f}"),
            'Price': positions[i]['mkt_price'],
            'Value': float(f"{positions[i]['mkt_price']*positions[i]['q']:.2f}"),
            'Profit': positions[i]['profit_close']
        }
        all_data.append(data)
    return all_data


