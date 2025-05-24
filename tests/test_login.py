import pytest
from allure import title

class TestLoginUser:
    @title("Логин под существующим пользователем")
    def test_login_success(self, api, user):
        resp = api.login_user(user["email"], user["password"])
        assert resp.status_code == 200
        assert resp.json()["success"]

    @title("Логин с неверным логином или паролем")
    def test_login_failed(self, api, user):
        resp = api.login_user(user["email"]+"1", user["password"]+"1")
        assert resp.status_code == 401
        assert not resp.json()["success"]
