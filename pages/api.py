import requests
import allure


class SearchApi:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token

    @ allure.step("Поиск книги в поле 'поиск'")
    def search_books(self, value: str):
        my_headers = {
            "Content - Type": "application / json",
            "Authorization": f"Bearer {self.token}"
            }
        my_params = {"phrase": value}
        response = requests.get(f"{self.url}/v2/search/product", headers=my_headers, params=my_params)
        return response
    
    @ allure.step("Добавление книги в корзину")
    def add_product_to_cart(self, product_id: int):
        my_headers = {
            "Content - Type": "application / json",
            "Authorization": f"Bearer {self.token}"
            }
        my_body = {"id": product_id, "adData": {"item_list_name": "product-page"}}
        response = requests.post(self.url + 'v1/cart/product', headers=my_headers, json=my_body)
        return response
    
    @ allure.step("Добавления количества выбранной книги")
    def quantity_product(self, id_product: int, quantity: int):
        my_headers = {
            "Content - Type": "application / json",
            "Authorization": f"Bearer {self.token}"
            }
        my_body = {"id": id_product, "quantity": quantity}
        response = requests.put(self.url+'v1/cart', headers=my_headers, json=my_body)
        return response
    
    @ allure.step("Получить содержимое корзины")
    def get_cart_contents(self):
        my_headers = {
            "Content - Type": "application / json",
            "Authorization": f"Bearer {self.token}"
            }
        response = requests.get(self.url+'v1/cart', headers=my_headers)
        return response
    
    @ allure.step("Очистить корзину")
    def cart_clear(self):
        my_headers = {
            "Content - Type": "application / json",
            "Authorization": f"Bearer {self.token}"
            }
        response = requests.delete(self.url+'v1/cart', headers=my_headers)
        return response
