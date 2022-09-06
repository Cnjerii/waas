from django.conf import settings
import requests
import json
from requests.auth import HTTPBasicAuth


def get_access_token():
    client_id = settings.WAAS_CLIENT_ID
    client_secret = settings.WAAS_CLIENT_SECRET
    token_url = settings.WAAS_TOKEN_URL
    params = {'grant_type': 'client_credentials'}
    try:
        response = requests.get(token_url, auth=HTTPBasicAuth(
            client_id, client_secret), params=params, verify=False)
        json_response = json.loads(response.text)
        print('token_respone:', json_response)
        access_token = json_response['access_token']
        return access_token
    except Exception as error:
        print('error:', str(error))
