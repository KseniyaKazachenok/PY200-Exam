import hashlib
from typing import Union
import random


class IdCounter:

    def __init__(self):
        self.id = 0

    def get_id(self):
        self.id += 1
        return self.id


class Password:

    def __init__(self, your_password: str = None):
        self.your_password = None
        self.init_your_password(your_password)

    def init_your_password(self, your_password):
        if not isinstance(your_password, str):
            raise TypeError
        if len(your_password) < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов")
        if your_password.isdigit() or your_password.isalpha():
            raise ValueError("В пароле должны быть как цифры, так и буквы")
        self.your_password = self.get_hash(your_password)

    @staticmethod
    def get_hash(your_password):
        return hashlib.sha256(your_password.encode()).hexdigest()

    @staticmethod
    def check_your_password(your_password):
        if hashlib.sha256(your_password.encode()).hexdigest() != your_password.get_hash:
            raise TypeError


class Product:
    _id_counter = IdCounter()

    def __init__(self, name: str, price: Union[int, float], rating: Union[int, float]):
        self._id = self._id_counter.get_id()
        self._name = name
        self.price = None
        self.rating = None
        self.init_price(price)
        self.init_rating(rating)

    @property
    def name(self):
        return self._name

    def init_price(self, price):
        if not isinstance(price, Union[int, float]):
            raise TypeError
        if price <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.price = price

    def init_rating(self, rating):
        if not isinstance(rating, Union[int, float]):
            raise TypeError
        if rating < 0:
            raise ValueError("Рейтинг не может быть меньше нуля")
        self.rating = rating

    def __repr__(self) -> str:
        return f"Product({self._name}, {self.price}, {self.rating})"

    def __str__(self) -> str:
        return f"Продукт ID {self._id} _ {self._name}"


class Cart:

    def __init__(self, product_list: list = None):
        self.product_list = product_list

    def add_to_product_list(self, obj):
        self.product_list.append(obj)

    def remove_from_product_list(self, obj):
        self.product_list.remove(obj)


class User:
    _id_counter = IdCounter()
    _password = Password()

    def __init__(self, username: str, password: str):
        self._id = self._id_counter.get_id()
        self.cart = Cart()
        self.username = None
        self.init_username(username)
        self.password = self._password.get_hash(password)

    def init_username(self, username):
        if not isinstance(username, str):
            raise TypeError
        self.username = username

    def __repr__(self) -> str:
        return f"User({self.username}, {'password1'})"

    def __str__(self) -> str:
        return f"Пользователь {self.username} пароль {'password1'}"


class Generator:
    name_list = ['apple', 'orange', 'banana', 'pineapple', 'peach', 'mango']
    product_name = random.choices(name_list)
    product_price = round(random.uniform(1, 50), 2)
    product_rating = round(random.uniform(1, 10), 2)

    def get_product(self):
        return Product(self.product_name, self.product_price, self.product_rating)


class Store:
    generator = Generator()

    def __init__(self):
        self.user = None
        self.login = None
        self.passw = None
        self.check_user()

    def check_user(self):
        self.login = input('Введите имя пользователя\n')
        self.passw = input('Введите пароль\n')
        self.user = User(self.login, self.passw)

    def add_to_cart(self):
        self.user.cart.add_to_product_list(self.generator.get_product())

    def cart_view(self):
        print(self.user.cart)


if __name__ == '__main__':

    store1 = Store()
    store1.add_to_cart()
    store1.cart_view()
