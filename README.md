# Freedom24_API

This application allows users to retrieve account information from their D-Account and Trading Account using their respective API keys, securely manage configurations and create a JSON structure by combining the information. 

## Usage
### 1. Configuration Setup
Before running the application, set up the configuration files for your accounts:
```bash
python create_config.py
```

### 2. Encrypt Configuration
Encrypt the configuration files for security:
```bash
python create_key_encrypted_config.py
```

### 3. Main Functionality
Run the application to retrieve account information and create a JSON file:
```bash
python main.py
```

Note: Saves a JSON file named **data.json** in a dynamically created **data** directory within the **Freedom24** repository.

## API Key Retrieval and Key Pair Generation
### Obtain API Key from Freedom24
1. Visit [Freedom24 Tradernet API](https://freedom24.com/tradernet-api/auth-api)
2. Log in to your account.
3. Navigate to the API section to access your API keys.

### Generate a New Key Pair
To generate a new key pair for API access:
1. Look for the option to generate new keys.
2. Follow the instructions to generate a new key pair.
3. Ensure to securely save your public and private keys for API authentication.

Note: Always keep your API keys confidential and avoid sharing them publicly.

## License
This project is licensed under the [MIT License](./LICENSE).
