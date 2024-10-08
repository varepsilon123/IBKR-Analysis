import os
import urllib3
from service.requests import get, post
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Suppress only the single InsecureRequestWarning from urllib3 needed for self-signed certificates
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
BASE_URL = os.getenv('BASE_URL')

def get_auth_status():
    request_url = f"{BASE_URL}/iserver/auth/status"
    payload = {}
    response = post(url=request_url, payload=payload)

    return response

def init_brokerage_session():
    request_url = f"{BASE_URL}/iserver/auth/ssodh/init"
    payload = {
        "publish":True,
        "compete":True
    }
    response = post(url=request_url, payload=payload)
    
    return response

def tickle():
    request_url = f"{BASE_URL}/tickle"
    payload = {}
    response = post(url=request_url, payload=payload)

    return response

def validate_sso():
    request_url = f"{BASE_URL}/sso/validate"
    response = get(url=request_url)

    return response

def logout():
    request_url = f"{BASE_URL}/logout"
    payload = {}
    response = post(url=request_url, payload=payload)

    return response