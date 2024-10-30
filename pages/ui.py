from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.description("Тестирование сайта Читай-город")
class SearchByTitle:

    def __init__(self, driver: WebDriver):
        self._driver: WebDriver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Политика куки")
    def set_cookie_policy(self): 
        cookie = {"name": "cookie_policy", "value": "1"}
        self._driver.add_cookie(cookie)

    @allure.step("Поиск книги в поле 'поиск'")
    def search_by_title(self, term: str):
        self._driver.find_element(By.CLASS_NAME, "header-search__input").send_keys(term + Keys.RETURN)
        title = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-search__button")))
        title.click()
        txt = self._driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/p').text
        return txt

    @allure.step("Cтраницa акций")
    def open_promotions(self) -> None:
        promotions_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/promotions"]')))
        promotions_button.click()
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1")
        return txt.text

    @allure.step("Cтраницa распродаж")
    def open_sales(self) -> None:
        sales_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/sales"]')))
        sales_button.click()
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1")
        return txt.text

    @allure.step("Cтраницa 'Что ещё почитать?'")
    def open_articles(self) -> None:
        articles_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/collections"]')))
        articles_button.click()
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1")
        return txt.text

    @allure.step("Cтраницa магазинов")
    def open_shops(self)-> None:
        shops_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/shops"]')))
        shops_button.click()
        txt = self._driver.find_element(By.CSS_SELECTOR, "h1")
        return txt.text

    @allure.step("Cтраницa 'корзинa'")
    def go_to_cart(self) -> None:
        cart_button = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']")))
        cart_button.click()
        cart_text = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".empty-title")))
        return cart_text.text

    @allure.step("Получить заголовок первой книги")
    def get_book_title(self) -> str:
        book = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/section/div/article[1]/div[2]/a/div/div[1]')))
        return book.text

    @allure.step("Закрытие браузера")
    def quit(self):
        self._driver.quit()
