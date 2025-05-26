from src.controllers.interfaces.login_creator import LoginCreatorInterface
from src.views.http_types import http_request
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class LoginCreatorView(ViewInterface):
    def __init__(self, controller: LoginCreatorInterface) -> None:
        self.controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        username = http_request.body.get("username")
        password = http_request.body.get("password")
        self.__validate_input(username, password)

        response = self.controller.create(username, password)
        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_input(self, username: any, password: any) -> None:
        if (
            not username
            or not password
            or not isinstance(username, str) or not isinstance(password, str)
        ): raise Exception("Invalid Input")