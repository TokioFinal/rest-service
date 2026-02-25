import requests
from app.config import settings
from app.schemas.auth import authRegister
from app.exceptions import BadRequestException, BadGatewayException, AuthFailedException

def login(form_data):
    res = requests.post("{0}/login".format(settings.AUTH_SERVICE_URL), data=form_data )
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 401:
        raise AuthFailedException(detail=res.json()["detail"])

def register(body: authRegister):
    res = requests.post("{0}/register".format(settings.AUTH_SERVICE_URL), data=body)
    if res.status_code == 200:
        return res.json()
    
    elif res.status_code == 500:
        raise BadGatewayException(detail=res.json()["detail"])
    
    else:
        raise BadRequestException(detail=res.json()["detail"])
    
    