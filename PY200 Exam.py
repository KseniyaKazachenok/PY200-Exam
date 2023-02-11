import hashlib
from typing import Union


class IdCounter:
    def __init__(self):
        self.id = 0

    def get_id(self):
        self.id += 1
        return self.id

    def __str__(self) -> str:
        return f"ID {self.id}"


class Password:
    def __init__(self, your_password: str):
        self.your_password = None
        self.init_your_password(your_password)

    def init_your_password(self, your_password):
        if not isinstance(your_password, str):
            raise TypeError
        if len(your_password) < 8:
            raise ValueError("Длина пароля должна быть не менее 8 символов")
        if your_password.isdigit() or your_password.isalpha():
            raise ValueError("В пароле должны быть как цифры, так и буквы")
        self.your_password = your_password

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
        self._id = self._id_counter.id
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
    def __init__(self, product_list: list):
        self.product_list = product_list

    def add_to_product_list(self, obj):
        self.product_list.append(obj)

    def remove_from_product_list(self, obj):
        self.product_list.remove(obj)


class User:
    _id_counter = IdCounter()

    def __init__(self, username: str, password: str):
        self._id = self._id_counter.id
        self._cart = Cart([])
        self.username = None
        self.init_username(username)
        self._password = password

    def init_username(self, username):
        if not isinstance(username, str):
            raise TypeError
        self.username = username

    @property
    def password(self):
        self._password = hashlib.sha256(self._password.encode()).hexdigest()
        return self._password

    def __repr__(self) -> str:
        return f"User({self.username}, {'password1'})"

    def __str__(self) -> str:
        return f"Пользователь {self.username} пароль {'password1'}"
