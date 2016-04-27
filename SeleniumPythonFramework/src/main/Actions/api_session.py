import requests

from SeleniumPythonFramework.src.main.Utils.driver_utils import get_api_url

__author__ = 'Gino'


# This helps us as an utils, doing complex and repetitive actions
class ApiSession():
    def __init__(self, **kwargs):
        self.session = requests.session()

    def delete_account(self, user, password):
        current_user = self.auth_user_endpoint(user, password)
        self.delete_user_endpoint(current_user['user']['guid'])

    def auth_user_endpoint(self, user, password):
        user_credentials = {'username': user, 'password': password}
        response = self.session.post(get_api_url("/auth/login"), data=user_credentials)
        assert response.status_code == 200
        return response.json()

    def delete_user_endpoint(self, guid):
        assert self.session.delete(get_api_url("/store/user/{}").format(guid)).status_code == 200
