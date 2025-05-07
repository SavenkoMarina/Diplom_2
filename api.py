import requests
from allure import step

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

    @step("Регистрация пользователя")
    def register_user(self, email: str, password: str, name: str):
        url = f"{self.BASE_URL}/auth/register"
        payload = {"email": email, "password": password, "name": name}
        response = self.session.post(url, json=payload)

        data = response.json()
        self.access_token = data.get("accessToken")
        return response

    @step("Авторизация пользователя")
    def login_user(self, email: str, password: str):
        url = f"{self.BASE_URL}/auth/login"
        payload = {"email": email, "password": password}
        response = self.session.post(url, json=payload)

        data = response.json()
        self.access_token = data.get("accessToken")
        self.refresh_token = data.get("refreshToken")
        return response

    @step("Удаление пользователя")
    def delete_user(self):
        url = f"{self.BASE_URL}/auth/user"
        response = self.session.delete(url, headers=self._auth_headers())

        self.access_token = None
        self.refresh_token = None
        return response

    @step("Обновление информации пользователя")
    def update_user_info(self, email=None, name=None):
        url = f"{self.BASE_URL}/auth/user"
        payload = {}
        if email:
            payload["email"] = email
        if name:
            payload["name"] = name
        response = self.session.patch(url, json=payload, headers=self._auth_headers())
        return response

    @step("Получение ингридиентов")
    def get_ingredients(self):
        url = f"{self.BASE_URL}/ingredients"
        response = self.session.get(url)

        return response

    @step("Создание заказа")
    def create_order(self, ingredient_ids):
        url = f"{self.BASE_URL}/orders"
        payload = {}
        if ingredient_ids:
            payload["ingredients"]  = ingredient_ids
        response = self.session.post(url, json=payload, headers=self._auth_headers())

        return response

    @step("Получение заказов пользователя")
    def get_orders(self):
        url = f"{self.BASE_URL}/orders"
        response = self.session.get(url, headers=self._auth_headers())

        return response
