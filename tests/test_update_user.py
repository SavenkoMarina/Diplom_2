import pytest
from allure import title

from helpres import generate_random_string


class TestUpdateUser:
    @pytest.mark.parametrize("user_data", [
        {
            "email": f"{generate_random_string(8)}@gmail.com",
            "name": generate_random_string(8),
        },
        {
            "email": None,
            "name": generate_random_string(8),
        },
        {
            "email": f"{generate_random_string(8)}@gmail.com",
            "name": None,
        }
    ])
    @title("Изменение пользователя с авторизаций")
    def test_update_user_success(self, api, user, user_data):
        api.login_user(user["email"], user["password"])
        resp = api.update_user_info(**user_data)
        assert resp.status_code == 200
        assert resp.json()["success"]

    @title("Изменение пользователя без авторизаций")
    def test_update_user_failed(self, api, user):
        email = f"{generate_random_string(8)}@gmail.com"
        name = generate_random_string(8)
        resp = api.update_user_info(email=email, name=name)
        assert resp.status_code == 401
        assert not resp.json()["success"]
