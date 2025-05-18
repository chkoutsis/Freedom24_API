from typing import Dict, List, Optional

from tradernet import TraderNetAPI

import utils as get_cross_rates


def get_api_access(
    public_key: str, private_key: str, login: str, password: str
) -> TraderNetAPI:
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
    return TraderNetAPI(public_key, private_key, login, password)


def get_d_account_user_info(api_access: TraderNetAPI) -> List[Dict]:
    """
    Retrieves the EUR and USD Account balances for a user via TraderNetAPI.

    Args:
    - api_access (TraderNetAPI): An instance of TraderNetAPI for accessing user account information.

    Returns:
    - List: A list containing a dictionary with 'EUR' and 'USD' keys, representing the respective balances.
    """
    # Get the account summary
    # The account summary contains the account balances in different currencies
    eur_amount = TraderNetAPI.account_summary(api_access)["result"]["ps"]["acc"][0]["s"]
    usd_amount = TraderNetAPI.account_summary(api_access)["result"]["ps"]["acc"][1]["s"]

    data = {"EUR": eur_amount, "USD": usd_amount}
    return [data]


def get_trading_account_user_info(
    api_access: TraderNetAPI, currency: Optional[str] = "EUR"
) -> List[Dict]:
    """
    Retrieves Trading Account information for a user via TraderNetAPI.

    Args:
    - api_access (TraderNetAPI): An instance of TraderNetAPI for accessing user account information.
    - currency Optional[str]: The currency in which to retrieve the account information. Default is "EUR".

    Returns:
    - List: A list containing dictionaries with trading account details.
    """
    all_data = []

    # Get liquidity information
    liquidity = TraderNetAPI.account_summary(api_access)["result"]["ps"]["acc"]

    # Iterate through the liquidity information and extract relevant amounts
    for item in liquidity:
        if item["curr"] == "EUR":
            eur_amount = item["s"]
        elif item["curr"] == "USD":
            usd_amount = item["s"]
        else:
            raise ValueError("Invalid currency")

    # Add the EUR and USD amounts to the data list
    liquidity_data = {"liquidity": {"EUR": eur_amount, "USD": usd_amount}}
    all_data.append(liquidity_data)

    # Get  positions
    positions = TraderNetAPI.account_summary(api_access)["result"]["ps"]["pos"]

    # Get the EUR to USD rate
    eurusd_currecy_rate = get_cross_rates.get_cross_rates(
        base_currency="EUR", currencies=["USD"]
    )
    eurusd_currecy_rate_value = eurusd_currecy_rate["USD"]

    # Compute USD to EUR as reciprocal
    usdeur_currecy_rate_value = 1 / eurusd_currecy_rate_value

    # Set up the positions data structure
    all_positions_data = {"positions": []}

    # Iterate through the positions and extract relevant information
    for position in positions:

        # Check if the position is in the specified currency
        base_currency = position["base_currency"]

        # Get the position details
        qty = position["q"]
        price = position["mkt_price"]
        entry_price = round(position["price_a"], 2)
        profit = position["profit_close"]
        conversion_rate = 1

        # Determine the conversion rate based on the base currency and the specified currency
        if base_currency == "EUR" and currency == "USD":
            conversion_rate = eurusd_currecy_rate_value
        elif base_currency == "USD" and currency == "EUR":
            conversion_rate = usdeur_currecy_rate_value

        # Calculate the profit in the specified currency
        position_data = {
            "Ticker": position["base_contract_code"],
            "Qty": qty,
            "Entry Price": entry_price,
            "Price": price,
            "Value": round(price * qty * conversion_rate, 2),
            "Profit": round(profit * conversion_rate, 2),
        }

        # Append position data to the all positions data
        all_positions_data["positions"].append(position_data)

    # Append the positions data to the list
    all_data.append(all_positions_data)

    return all_data
