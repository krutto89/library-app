import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class MpesaC2bCredential:
    consumer_key = '7dxSed8LGljxchklpnDmsYviGcuoHXI7TzItNsMAWj4Gzard'
    consumer_secret = 'JHkEtTMlLUYvZmTN2pwArkWdfqkRcGIl0tGppis8jD0LA9sGXAEIdz30hGvxneih'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken: # fetching and storing the access token
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


class LipanaMpesaPpassword: # generating the password required for the STK Push using the business short code and passkey and timestamp
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode()) # base64 encoding the password for security purposes
    decode_password = online_password.decode('utf-8')