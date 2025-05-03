import json

import requests


def get_cross_rates(base_currency="EUR", currencies=["USD"]):
    """
    Fetches cross currency rates from Tradernet API for the current date.

    Args:
        base_currency (str): The base currency (e.g., "EUR"). Default is "EUR".
        currencies (list): List of target currency codes (e.g., ["USD"]). Default is ["USD"].

    Returns:
        dict: API response as a dictionary.
    """
    # Define the payload for the API request
    payload = {
        "cmd": "getCrossRatesForDate",
        "params": {
            "base_currency": base_currency,
            "currencies": currencies,
        },
    }

    # Make the API request
    response = requests.get(
        "https://tradernet.com/api/", params={"q": json.dumps(payload)}
    )

    # Check if the request was successful
    # If successful, return the rates from the response
    # If not, raise an exception with the error message
    if response.status_code == 200:
        return response.json()["rates"]
    else:
        raise Exception(
            f"API request failed with status {response.status_code}: {response.text}"
        )
