from random import randint


class Product:
    __general_discount = 0
    __date = randint(1, 365)
    __delay_expiration = 1

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

    def __init__(self, name: str, price: float, expire_date: int, discount: int = 0,):
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
        self


    def is_expired(self) -> bool:
        return self.__expire_date < Product.__date

    def soon_expired(self) -> bool:
        delay = self.__expire_date - Product.__date
        return Product.__delay_expiration < delay

    def __str__(self):
        if self.get_final_price() == self.__price:
            return f"[PRODUCT] {self.__name} ({self.__price})"
        else:
            return f"[PRODUCT] {self.__name} ({self.get_final_price()} CHF, costed before {self.get_initial_price()} CHF)"

class Supermarket:
    def __init__(self):
        self.__products = []

    def add_product(self, Product) -> list:
        if not Product not in self.__products:
            self.__products.append(Product)
        else:
            raise ValueError(f"The product is already sold in the supermarket")

    def remove_product(self):
        self.__products.remove(Product)
        return self.__products

    def update_products(self):
        for item in self.__products:
            if item.is_expired():
                item.

    def __str__(self):
        txt = "[SUPERMARKET]"
        for i in self.__products:
            txt = txt + f"\n{i}"
        return txt

if __name__ == "__main__":
    P1 = Product("bread",2.4,10, 50)
    P2 = Product("milk", 1.5, 0, 34)
    supermarket = Supermarket()
    supermarket.add_product(P1)
    supermarket.add_product(P2)
    print(supermarket)

