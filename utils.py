import requests
from pprint import pprint


def get_data(url):

    try:
        responce = requests.request("GET", url, verify=False)
        if responce.status_code == 200:
            return responce.json(), "INFO: Данные получены успено"
        return None, f"ERROR status_code:{responce.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"
