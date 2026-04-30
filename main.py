import argparse
import logging

from credentials import APICredentialsLoader
from utils import JsonHandler, get_trading_account_user_info


def setup_logging():
    """
    Configures the logging settings for the script.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def parse_arguments():
    """
    Parses command-line arguments for the script.

    Returns:
    - argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Fetch and save account information as JSON."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data.json",
        help="The name of the output JSON file (default: data.json).",
    )
    return parser.parse_args()


def run(output_file: str):
    """
    Main function to execute the script.

    This function retrieves user information from Trading Account API
    using the provided API access credentials. It then creates a JSON file with the
    collected account information.

    Args:
    - output_file (str): The name of the output JSON file.
    """
    try:
        logging.info("Starting the script...")

        # Load API credentials using the APICredentialsLoader class
        cred_loader = APICredentialsLoader()
        cred = cred_loader.load_credentials()
        logging.info("API credentials loaded successfully.")

        # Retrieve Trading Account user information using the Trading Account API access
        trading_account_user_info = get_trading_account_user_info(cred)
        logging.info("Trading account information retrieved successfully.")

        # Create an instance of JsonHandler to handle JSON file creation
        json_handler = JsonHandler()
        json_handler.create_json(
            trading_account_user_info=trading_account_user_info, filename=output_file
        )
        logging.info(f"Account information saved successfully to {output_file}.")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    setup_logging()
    args = parse_arguments()
    run(output_file=args.output)
