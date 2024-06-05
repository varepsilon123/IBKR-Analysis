import os
import urllib3
from service.requests import post, get
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Suppress only the single InsecureRequestWarning from urllib3 needed for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
BASE_URL = os.getenv('BASE_URL')

def get_auth_status() :
    request_url = f"{BASE_URL}/iserver/auth/status"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {}

    response = post(url=request_url, headers=headers, payload=payload)
    return response

def test():
    try:
        response = get_auth_status()
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Body: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test()
