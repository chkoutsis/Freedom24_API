from config import ConfigLoader
from utils import get_api_access


class APICredentialsLoader:
    """A class to load API credentials for Trading Account."""

    def __init__(self):
        """
        Initializes the APICredentialsLoader with a ConfigLoader instance.
        """
        self.config_loader = ConfigLoader()

    def load_credentials(self):
        """
        Loads API credentials for Trading Account.

        Args:
        - None

        Returns:
        - TraderNetAPI: An instance of TraderNetAPI for Trading Account.
        """
        # Load the configuration using the ConfigLoader class
        trading_account_config = self.config_loader.load_all_configs()

        # Get API access for Trading Account using the provided credentials
        trading_account_api_access = get_api_access(
            trading_account_config[0],
            trading_account_config[1],
            trading_account_config[2],
            trading_account_config[3],
        )

        return trading_account_api_access
