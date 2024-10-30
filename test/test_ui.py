import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.ui import SearchByTitle

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
main_page = SearchByTitle(browser)


@allure.title("Тест открытие сайта")
@allure.description("Тест проверяет наличие связи с сайтом")
@allure.feature("Проверка связи с сайтом")
@allure.severity("blocker")
@pytest.mark.positive_test
def test_chitay_gorod():
    with allure.step("Открытие веб-страницы в Chrome"):
        main_page.set_cookie_policy()
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест поиск книги на кириллице")
@allure.description("Тест проверяет поиск книги на русском языке")
@allure.feature("Проверка поля поиск")
@allure.severity("bloker")
def test_rus_search():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Ввод названия книги на русском языке"):
        book_title = main_page.search_by_title("Гравити Фолз")
    with allure.step("Проверка текста с результатами поиска на странице"):
        assert book_title == "Показываем результаты по запросу «гравити фолз», 204 результата"
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест открытия страницы акций")
@allure.description("Проверка, что текст заголовка страницы акций соответствует ожидаемому")
@allure.feature("Проверка страниц")
@allure.severity("bloker")
def test_open_promotions_page():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Oткрытия страницы акций"):
        promotions_text = main_page.open_promotions()
    with allure.step("Проверка текста заголовка акций"):
        assert promotions_text == "АКЦИИ"
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест открытия страницы распродаж")
@allure.description("Проверка, что текст заголовка страницы распродаж соответствует ожидаемому")
@allure.feature("Проверка страниц")
@allure.severity("bloker")
def test_open_sales_page():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Oткрытия страницы распродаж"):
        sales_text = main_page.open_sales()
    with allure.step("Проверка текста заголовка распродаж"):
        assert sales_text == "РАСПРОДАЖА"
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест открытия страницы магазинов")
@allure.description("Проверка, что текст заголовка страницы магазинов соответствует ожидаемому")
@allure.feature("Проверка страниц")
@allure.severity("bloker")
def test_open_shops_page():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Oткрытия страницы магазинов"):
        shops_text = main_page.open_shops()
    with allure.step("Проверка текста заголовка магазинов"):
        assert shops_text == "НАШИ МАГАЗИНЫ"
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест открытия страницы журнала")
@allure.description("Проверка, что текст заголовка страницы журнала соответствует ожидаемому")
@allure.feature("Проверка страниц")
@allure.severity("bloker")
def test_open_articles_page():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Oткрытия страницы журнала"):
        articles_text = main_page.open_articles()
    with allure.step("Проверка текста заголовка журнала"):
        assert articles_text == "ЧТО ЕЩЁ ПОЧИТАТЬ?"
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест соответствия названия книги по запросу")
@allure.description("Проверяем, что название первой книги на странице результатов поиска соответствует введенному значению")
@allure.feature("Проверка названия книги из представленного списка по запросу")
@allure.severity("bloker")
def test_find_first_book_title():
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Ввод названия книги на русском языке"):
        title = "Колобок"
        main_page.search_by_title(title)
    with allure.step("Получаем название первой книги"):
        first_book = main_page.get_book_title()
    with allure.step("Проверяем введенное название и полученный результат"):
        assert title == first_book
    with allure.step("Закрытие браузера"):
        main_page.quit()


@allure.title("Тест открытия страницы корзины")
@allure.description("Проверка, что корзина пустая")
@allure.feature("Проверка страниц")
@allure.severity("bloker")
def test_open_cart_page():
    main_page = SearchByTitle(browser)
    with allure.step("Открытие веб-страницы в Chrome и выполнение поиска"):
        main_page.set_cookie_policy()
    with allure.step("Oткрытия страницы корзины"):
        catr_text = main_page.go_to_cart()
    with allure.step("Проверка, что корзина пустая"):
        assert catr_text == "В корзине ничего нет"
    with allure.step("Закрытие браузера"):
        main_page.quit()
