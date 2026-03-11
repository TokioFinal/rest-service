import requests
from app.config import settings
from app.schemas.auth import authRegister
from app.utils import handle_responses
from app.exceptions import BadRequestException, BadGatewayException, AuthFailedException

def login(data):
    form_data = {
        "username": data["username"],
        "password": data["password"]
    }
    res = requests.post("{0}/login".format(settings.AUTH_SERVICE_URL), data=form_data )
    if res.status_code == 200:
        return res.json()
    
    handle_responses(res)


def register(body: authRegister):
    print("inside auth client################################################")
    print("body")
    print(body)
    print("body_model_dump")
    print(body.model_dump_json())
    print("authservice_url")
    print(settings.AUTH_SERVICE_URL)

    res = requests.post("{0}/register".format(settings.AUTH_SERVICE_URL), json=body.model_dump_json())
    print("after request")
    print(res)
    if res.status_code == 200:
        return res.json()
    
    handle_responses(res)
 
    
    