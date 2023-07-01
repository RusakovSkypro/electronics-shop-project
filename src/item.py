import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f'Item: {self.__name}'


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return int(self.price * self.quantity)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name_private(self):
        """атрибут `name` сделать приватным"""
        return self.__name

    @name_private.setter
    def name_private(self, name):
        """в сеттере `name` проверяем, что длина наименования товара не больше 10 симвовов.
        В противном случае, обрезаем строку (оставлем первые 10 символов)."""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        items = []
        with open('items.csv', newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                items.append(cls(row["name"], row["price"], row["quantity"]))
        return items

    @staticmethod
    def string_to_number(asd):
        """статический метод, возвращающий число из числа-строки"""
        result = ''
        for i in asd:
            if i.isdigit():
                result += i
        return int(result)

