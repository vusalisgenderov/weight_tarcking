from fastapi import HTTPException,status

class DetailHTTPException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "server error"
    def __init__(self):
        super().__init__(status_code=self.STATUS_CODE,detail=self.DETAIL)



class DetailHTTPException1(HTTPException):
    STATUS_CODE = 406
    DETAIL = "server error"
    def __init__(self):
        super().__init__(status_code=self.STATUS_CODE,detail=self.DETAIL)


class UserNottFoundException(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "user is not found"

class UserIsExists(DetailHTTPException):
    STATUS_CODE=status.HTTP_406_NOT_ACCEPTABLE
    DETAIL = "User is exists"

class UserNotWeight(DetailHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "your weight havn't in base"


