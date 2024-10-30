import allure
import pytest
from pages.api import SearchApi

url = "https://web-gate.chitai-gorod.ru/api"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mjk3NTQ5OTIsImlhdCI6MTcyOTU4Njk5MiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImNjZmQ2NzE0Yjg4N2UyMjBhOTZkZmVlNGI5ZDRiN2E5MWQwN2QzMjhjZWZkYmE5OGRhYTlmNjkzZmVkNGNjODgiLCJ0eXBlIjoxMH0.Piorl8MibNwm_pInJVti1OEPvDd07k2oufrgCPPIQso"

@allure.title("Поиск на кириллице")
@allure.description("Тест проверяет поиск книги на кириллице")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_search_rus():
    api = SearchApi(url, token)
    title = "Гравити Фолз"
    resp_search = api.search_books(title)
    print(f"Status Code: {resp_search.status_code}")
    print(f"Respose Body: {resp_search.text}")
    assert resp_search.status_code == 200
    assert title in resp_search.text


@allure.title("Поиск на латинице")
@allure.description("Тест проверяет поиск книги на французском языке")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_search_fra():
    api = SearchApi(url, token)
    search = "Dans un mois dans un an"
    resp_search = api.search_books(search)
    assert resp_search.status_code == 200
    assert search in resp_search.text


@allure.title("Поиск сборника по 2-м авторам")
@allure.description("Тест проверяет поис книги по авторам")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_by_author():
    api = SearchApi(url, token)
    search = "Пушкин Есенин"
    resp_search = api.search_books(search)
    assert resp_search.status_code == 200
    assert search in resp_search.text


@allure.title("Пустой поиск")
@allure.description("Тест проверяет вылонение пустого поиска")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("trivial")
@pytest.mark.negative_test
def test_search_empty():
    api = SearchApi(url, token)
    search = ""
    resp_search = api.search_books(search)
    assert resp_search.status_code == 400
    assert resp_search.json()["title"] == "Phrase обязательное поле"


@allure.title("Поиск по слитному названию")
@allure.description("Проверка поиска книги по слитному названию")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_name_wrong():
    api = SearchApi(url, token)
    search = "Курочкаряба"
    resp_search = api.search_books(search)
    assert resp_search.status_code == 200, "Ожидался status code 422"
    assert search in resp_search.text, "Ожидался ответ 'Похоже, у нас такого нет'"


@allure.title("Поиск по спецсимволам")
@allure.description("Проверка поиска книги по символам")
@allure.feature("Проверка поля 'поиск'")
@allure.severity("blocker")
@pytest.mark.negative_test
def test_by_special_characters():
    api = SearchApi(url, token)
    search = "&< >"
    resp_search = api.search_books(search)
    assert resp_search.status_code == 422
    assert resp_search.json()["title"] == "Недопустимая поисковая фраза"


@allure.title("Добавление книги в корзину, увеличение кол-ва, очищение корзины")
@allure.feature("Управление корзиной")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_working_cart():
    api = SearchApi(url, token)
    with allure.step("Поиск книги в поле 'поиск'"):
        search = "Dans un mois dans un an"
        resp_search = api.search_books(search)
        assert resp_search.status_code == 200
        assert search in resp_search.text
    with allure.step("Добавление выбранной книги в корзину"):
        id_book = 2014891
        resp_cart = api.add_product_to_cart(id_book)
        assert resp_cart.status_code == 200
    with allure.step("Проверить содержимое корзины"):
        cart = api.get_cart_contents()
        assert cart.status_code == 200
        assert cart.json()
    with allure.step("Увеличить количество выбранной книги"):
        id_product = 149571839
        quantity = 2
        resp_product = api.quantity_product([id_product, quantity])
        assert resp_product
        assert resp_product.json()["quantity"] == 2
    with allure.step("Очистить корзину"):
        clear_cart = api.cart_clear()
        assert clear_cart.status_code == 204
        assert clear_cart.json() == ""
