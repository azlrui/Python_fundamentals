class Product:
    __general_discount = 0
    __time_expiration_date = 1

    @classmethod
    def set_general_discount(cls, value):
        cls.check_discount(value)
        cls.__general_discount = value
    def __init__(self, name : str, price : float, discount : int = 0, last_date : int = 0):
        self.check_str(name)
        self.check_float(price)
        self.check_int(discount)
        self.check_int(last_date)
        self.check_discount(discount)
        self.__name = name
        self.__price = price
        self.__discount = discount
        self.__final_price = self.get_final_price()
        self.__last_date = last_date
        self.check_date()

    @staticmethod
    def check_discount(discount):
        if discount < 0 or discount > 100:
            raise ValueError("Les réductions doivent être comprises entre 0 et 100 (%)")

    def check_date(self):
        if self.__last_date < 0 or self.__last_date > 365:
            raise ValueError("Introduisez une date valide")

    def check_int(self, value):
        if not isinstance(value,int):
            return ValueError

    def check_float(self, value):
        if not isinstance(value, float):
            return ValueError

    def check_str(self, value):
        if not isinstance(value, str):
            return ValueError

    def set_reduction(self, value):
        self.__reduction = value

    def get_initial_price(self):
        return f"{self.__price}"

    def get_final_price(self):
        return f"{self.__price * (1-self.__discount/100) * (1-self.__class__.__general_discount/100)}"

    def is_expired(self, value):
        if value < self.__last_date:
            return True

    def is_soon_expired(self):
        if self.__last_date - self.__class__.__time_expiration_date < 0:
            return True

    def __str__(self):
        if self.get_final_price() == self.__price:
            return f"[{self.__class__.__name__}] {self.__name} ({self.__final_price} CHF)"
        else:
            return f"[{self.__class__.__name__}] {self.__name} ({self.__final_price} CHF, valait {self.__price} CHF)"

class Hypermarket:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else :
            raise ValueError("On ne peut ajouter que des produits")

    def update(self, value):
        self.__products = [product for product in self.__products if product.is_expired(value)]
        for product in self.__products:
            if product.is_soon_expired():
                product.set_reduction(50)
    def __str__(self):
        return f"[Hypermarket]\n {"\n ".join([ f"-{product}" for product in self.__products])}"

class FreshProduct(Product):
    __time_expiration_date = 3
    def __init__(self, name: str, price: float, discount: int, last_date: int = 30, pack_date: int = 0):
        super().__init__(name, price, discount, last_date)
        self.check_date()
        self.__pack_date = pack_date

    def __str__(self):
        return super().__str__() + f" - Date d'emballage : {self.__pack_date}"



if __name__ == "__main__":
    rayon = Hypermarket()
    pf = FreshProduct("Saumon", 10.0, 6, 2)
    print(pf)
    rayon.add_product(FreshProduct("Saumon", 10.0, 6, 2))  # la réduction pour le saumon devrait apparaître dès le jour 3
    rayon.add_product(FreshProduct("Pain", 3.0, 2, 1))
    rayon.add_product(FreshProduct("Sauce", 6.0, 10))
    print(rayon)
    print()
    for date in range(12):
        print("Day " + str(date))
        if date == 4:
            Product.set_general_discount(20)
        if date == 7:
            Product.set_general_discount(0)
        rayon.update(date)
        print(rayon)
