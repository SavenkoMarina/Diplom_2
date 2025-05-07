from allure import title

class TestCreateOrder:
    @title("Создание заказа")
    def test_create_order_success(self, api, user, ingredients_ids):
        api.login_user(user["email"], user["password"])
        resp = api.create_order(ingredients_ids)
        assert resp.status_code == 200
        assert resp.json()["success"]

    @title("Создание заказа неавторизованным пользователем")
    def test_create_order_unauthorized(self, api, ingredients_ids):
        resp = api.create_order(ingredients_ids)
        assert resp.status_code == 200
        assert resp.json()["success"]

    @title("Создание заказа без ингридиентов")
    def test_create_order_without_ingredients(self, api, user):
        resp = api.create_order([])
        assert resp.status_code == 400
        assert not resp.json()["success"]

    @title("Создание заказа с неверным хэшем ингридиентов")
    def test_create_order_with_invalid_ingredients(self, api, user):
        resp = api.create_order(["60d3b41abdacab0026a733c6b"])
        assert resp.status_code == 500
