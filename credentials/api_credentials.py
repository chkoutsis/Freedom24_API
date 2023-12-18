import config.config as config
from utils.account_functions import get_api_access


d_account_api_access = get_api_access(config.d_public_key, 
                                      config.d_private_key, 
                                      config.d_login, 
                                      config.d_password)

trading_account_api_access = get_api_access(config.trading_public_key, 
                                            config.trading_private_key, 
                                            config.trading_login, 
                                            config.trading_password)
    