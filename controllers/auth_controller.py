from services.auth_service import AuthService


class AuthController:

    @staticmethod
    def register(username, email, password):
        success, message = AuthService.register_user(username, email, password)
        return success, message

    @staticmethod
    def login(username, password):
        success, message, user = AuthService.login_user(username, password)
        return success, message, user