import requests

class API:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    def __init__(self):
        self.session = requests.Session()
        self.access_token = None
        self.refresh_token = None

    def _auth_headers(self):
        if self.access_token:
            return {"Authorization": self.access_token}
        return {}

    def get_ingredients(self):
        url = f"{self.BASE_URL}/ingredients"
        response = self.session.get(url)

        return response

    def register_user(self, email: str, password: str, name: str):
        url = f"{self.BASE_URL}/auth/register"
        payload = {"email": email, "password": password, "name": name}
        response = self.session.post(url, json=payload)

        data = response.json()
        self.access_token = data.get("accessToken")
        return response

    def login_user(self, email: str, password: str):
        url = f"{self.BASE_URL}/auth/login"
        payload = {"email": email, "password": password}
        response = self.session.post(url, json=payload)

        data = response.json()
        self.access_token = data.get("accessToken")
        self.refresh_token = data.get("refreshToken")
        return response

    def logout_user(self):
        url = f"{self.BASE_URL}/auth/logout"
        payload = {"token": self.refresh_token}
        response = self.session.post(url, json=payload, headers=self._auth_headers())

        self.access_token = None
        self.refresh_token = None
        return response

    def get_user_info(self):
        url = f"{self.BASE_URL}/auth/user"
        response = self.session.get(url, headers=self._auth_headers())

        return response


    def delete_user(self):
        url = f"{self.BASE_URL}/auth/user"
        response = self.session.delete(url, headers=self._auth_headers())

        self.access_token = None
        self.refresh_token = None
        return response

    def update_user_info(self, email=None, name=None):
        url = f"{self.BASE_URL}/auth/user"
        payload = {}
        if email:
            payload["email"] = email
        if name:
            payload["name"] = name
        response = self.session.patch(url, json=payload, headers=self._auth_headers())
        return response

    def create_order(self, ingredient_ids: str):
        url = f"{self.BASE_URL}/orders"
        payload = {"ingredients": ingredient_ids}
        response = self.session.post(url, json=payload, headers=self._auth_headers())

        return response

    def initiate_password_reset(self, email: str):
        url = f"{self.BASE_URL}/password-reset"
        payload = {"email": email}
        response = self.session.post(url, json=payload)

        return response

    def reset_password(self, password: str, token: str):
        url = f"{self.BASE_URL}/password-reset/reset"
        payload = {"password": password, "token": token}
        response = self.session.post(url, json=payload)
        return response
