import os
import urllib3
from dotenv import load_dotenv
from ..service.requests import get


# Load environment variables from .env file
load_dotenv()

# Suppress only the single InsecureRequestWarning from urllib3 needed for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
BASE_URL = os.getenv('BASE_URL')

def account_pnl():
    request_url = f"{BASE_URL}/iserver/account/pnl/partitioned"
    response = get(url=request_url)

    return response

def accounts_test():
    try:
        response = account_pnl()
        print(f"Response Body: {response}")

    except Exception as e:
        print(f"Error: {e}")