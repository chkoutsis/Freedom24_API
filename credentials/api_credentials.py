from typing import Tuple

from config import ConfigLoader
from utils import get_api_access


class APICredentialsLoader:
    """A class to load API credentials for Trading Account and D Account."""

    def __init__(self):
        """
        Initializes the APICredentialsLoader with a ConfigLoader instance.
        """
        self.config_loader = ConfigLoader()

    def load_credentials(self) -> Tuple:
        """
        Loads API credentials for Trading Account and D Account.

        Args:
        - None

        Returns:
        - Tuple: A tuple containing two instances of TraderNetAPI for Trading Account and D Account.
        """
        # Load the configuration using the ConfigLoader class
        trading_account_config, d_account_config = self.config_loader.load_all_configs()

        # Get API access for Trading Account using the provided credentials
        trading_account_api_access = get_api_access(
            trading_account_config[0],
            trading_account_config[1],
            trading_account_config[2],
            trading_account_config[3],
        )

        # Get API access for D Account using the provided credentials
        d_account_api_access = get_api_access(
            d_account_config[0],
            d_account_config[1],
            d_account_config[2],
            d_account_config[3],
        )

        return trading_account_api_access, d_account_api_access
