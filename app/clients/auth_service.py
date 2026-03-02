import requests
from app.config import settings
from app.schemas.auth import authRegister
from app.utils import handle_responses
from app.exceptions import BadRequestException, BadGatewayException, AuthFailedException

def login(form_data):
    res = requests.post("{0}/login".format(settings.AUTH_SERVICE_URL), data=form_data )
    if res.status_code == 200:
        return res.json()
    
    handle_responses(res)


def register(body: authRegister):
    res = requests.post("{0}/register".format(settings.AUTH_SERVICE_URL), data=body)
    if res.status_code == 200:
        return res.json()
    
    handle_responses(res)
 
    
    