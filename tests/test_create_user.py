import pytest
from allure import title

class TestCreateUser:
    @title("Создание пользователя который уже зарегистрирован")
    def test_create_duplicate_user(self, api, user):
        resp = api.register_user(user["email"], user["password"], user["name"])
        assert resp.status_code == 403
        assert not resp.json()["success"]

    @title("Создание пользователя с пропущенными обязательными полями")
    @pytest.mark.parametrize("user_data", [
        (None, "password", "name"),
        ("email@example.com", None, "name"),
        ("email@example.com", "password", None),
    ])
    def test_create_skip_required_field(self, api, user_data):
        resp = api.register_user(*user_data)
        assert resp.status_code == 403
        assert not resp.json()["success"]
