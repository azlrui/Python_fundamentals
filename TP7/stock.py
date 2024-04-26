from pprint import pprint
from bs4 import BeautifulSoup


class Stock:
    @staticmethod
    def abbreviation_to_float(number: str) -> float:
        multipliers = {"M": 1_000_000, "B": 1_000_000_000, "T": 1_000_000_000_000}
        unit = number[
            -1
        ]  # Prendre le dernier caractère pour identifier le multiplicateur
        num = float(number[:-1])  # Extraire le nombre et faire la multiplicaton
        if unit in multipliers:
            return num * multipliers[unit]
        else:
            return num

    @staticmethod
    def float_to_abbreviation(number: float) -> str:
        if number >= 1_000_000_000_000:  # Trillion
            return f"{number / 1_000_000_000_000:.0f}T"
        elif number >= 1_000_000_000:  # Billion
            return f"{number / 1_000_000_000:.0f}B"
        elif number >= 1_000_000:  # Million
            return f"{number / 1_000_000:.0f}M"
        else:
            return f"{number}"

    def __str__() -> str:
        ...
    
    __repr__ = __str__


if __name__ == '__main__':
    ...
