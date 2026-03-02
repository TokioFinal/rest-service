from app.exceptions import BadRequestException, BadGatewayException, ForbiddenException, NotFoundException, AuthFailedException

def handle_responses(res):
    match res.status_code:
        case 400 | 422 :
            raise BadRequestException(detail=res.json()["detail"])
        case 401 :
            raise AuthFailedException(detail=res.json()["detail"])
        case 403 : 
            raise ForbiddenException(detail=res.json()["detail"])
        case 404 :
            raise NotFoundException(detail=res.json()["detail"])
        case _:
            raise BadGatewayException(detail=res.json()["detail"])