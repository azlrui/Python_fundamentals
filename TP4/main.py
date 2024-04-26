from random import randint
from typing import override


class Product:
    __general_discount = 0
    __delay_expiration = 1
    __date = 5

    @classmethod
    def set_general_discount(cls, gen_discount: int) -> int:
        cls.__general_discount = gen_discount
        cls.discount_check(gen_discount)
        return cls.__general_discount

    @staticmethod
    def discount_check(x: int) -> None:
        if isinstance(x, int):
            pass
        else:
            raise ValueError("Invalid number, please enter an int")

    def __init__(self, name: str, price: float, expire_date: int, discount: int = 0):
        self.__name = name
        if discount > 100:
            raise ValueError("Enter a value between 0 and 100")
        self.__discount = discount
        self.discount_check(self.__discount)
        if expire_date > 100:
            raise ValueError("Enter a value between 0 and 365")
        self.__expire_date = int(expire_date)
        self.discount_check(expire_date)
        if float(price) < 0:
            raise ValueError("The price can not be negative")
        self.__price = float(price)

    def get_final_price(self):
        return self.__price * (1 - self.__discount / 100) * (1 - Product.__general_discount / 100)

    def get_initial_price(self):
        return self.__price

    def price_setter(self, discount: int) -> int:
        self.__discount = discount
        self.discount_check()
        return self.__discount

    def set_discount(self, discount: int) -> int:
        self.__discount = discount
        self.discount_check(self.__discount)
        return self.__discount

    def is_expired(self) -> bool:
        return self.__expire_date < Product.__date

    def soon_expired(self) -> bool:
        delay = Product.__expire_date - Product.__date
        return Product.__delay_expiration < delay

    def __str__(self):
        if self.get_final_price() == self.__price:
            return f"[{type(self).__name__}]{self.__name} ({self.__price})"
        else:
            return f"[PRODUCT] {self.__name} ({self.get_final_price()} CHF, costed before {self.get_initial_price()} CHF)"


class Supermarket:
    def __init__(self):
        self.__products = []

    def add_product(self, Product) -> list:
        if Product not in self.__products:
            self.__products.append(Product)
        else:
            raise ValueError(f"The product is already sold in the supermarket")

    def remove_product(self):
        self.__products.remove(Product)
        return self.__products

    def update_products(self) -> list:
        for item in self.__products:
            if item.is_expired():
                item.set_discount(50)
                self.__products.remove(item)

        return self.__products

    def __str__(self):
        txt = "[SUPERMARKET]"
        for i in self.__products:
            txt = txt + f"\n{i}"
        return txt


class FreshProduct(Product):
    __delay_expiration = 3

    def __init__(self, name: str, price: float, expire_date: int, packing_date: int = 0, discount: int = 0):
        super().__init__(name, price, expire_date, discount)
        self.packing_date = packing_date
        super().discount_check(self.packing_date)

    def __str__(self):
        return super().__str__() + f", Packing date : {self.packing_date}"



if __name__ == '__main__':
    rayon = Supermarket()
    pf = FreshProduct("Saumon", 10.0, 6, 2)
    print(pf)
    rayon.add_product(FreshProduct("Saumon", 10.0, 6, 2))  # la réduction pour le saumon devrait apparaître dès le jour 3
    rayon.add_product(Product("Pain", 3.0, 2, 1))
    rayon.add_product(Product("Sauce", 6.0, 10))
    print(rayon)
    print()
    for date in range(12):
        print("Day " + str(date))
        if date == 4:
            Product.set_general_discount(20)
        if date == 7:
            Product.set_general_discount(0)
        rayon.update_products()
        print(rayon)
