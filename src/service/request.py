import requests

def get(url, params=None, headers=None):
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        if response.status_code == 200:
            data = response.json()  # Assuming the response is in JSON format
            return data
        else:
            print(f'Failed to retrieve data: {response.status_code}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')

def post(url, payload=None, headers=None):
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()

        if response.status_code == 201:
            data = response.json()
            return data
        else:
            print(f'Failed to post data: {response.status_code}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')

def put(url, payload):
    try:
        response = requests.put(url, json=payload, timeout=10)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 201:
            data = response.json()
            return data
        elif response.status_code == 204:
            print("Successfully updated the resource. No content returned.")
            return None
        else:
            print(f'Failed to update data: {response.status_code}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')

def delete(url, headers=None, params=None):
    try:
        response = requests.delete(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        if response.status_code == 204:
            print('Successfully deleted')
        else:
            print(f'Failed to delete data: {response.status_code}')
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occurred: {conn_err}')
    except requests.exceptions.Timeout as timeout_err:
        print(f'Timeout error occurred: {timeout_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occurred: {req_err}')
