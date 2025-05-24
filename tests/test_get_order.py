from allure import title

class TestGetOrder:
    @title("Получение заказа авторизованного пользователя")
    def test_get_order_authorized(self, api, user, ingredients_ids):
        api.login_user(user["email"], user["password"])
        api.create_order(ingredients_ids)
        resp = api.get_orders()
        assert resp.status_code == 200

        resp_json = resp.json()
        assert resp_json["success"]
        assert len(resp_json["orders"]) == 1

    @title("Получение заказа не авторизованного пользователя")
    def test_get_order_unauthorized(self, api, ingredients_ids):
        api.create_order(ingredients_ids)
        resp = api.get_orders()
        assert resp.status_code == 401
        assert not resp.json()["success"]
