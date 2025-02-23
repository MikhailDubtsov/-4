class Vehicle:
    """ Базовый класс для транспортных средств. """

    def __init__(self, make: str, model: str, year: int):
        """
        Инициализирует базовое транспортное средство.

        :param make: Производитель
        :param model: Модель
        :param year: Год выпуска
        """
        self._make = make  # Непубличный атрибут
        self._model = model  # Непубличный атрибут
        self._year = year  # Непубличный атрибут

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def start_engine(self) -> str:
        """ Запускает двигатель транспортного средства. """
        return f"{self.make} {self.model} запускает двигатель."

    def __str__(self) -> str:
        """ Возвращает строковое представление транспортного средства. """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """ Возвращает официальное строковое представление транспортного средства. """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year})"


class Car(Vehicle):
    """ Класс легкового автомобиля, наследуется от Vehicle. """

    def __init__(self, make: str, model: str, year: int, doors: int):
        """
        Инициализирует легковой автомобиль.

        :param make: Производитель
        :param model: Модель
        :param year: Год выпуска
        :param doors: Количество дверей
        """
        super().__init__(make, model, year)
        self._doors = doors  # Непубличный атрибут

    @property
    def doors(self) -> int:
        return self._doors

    def start_engine(self) -> str:
        """ Переопределяет запуск двигателя, добавляя специфическое поведение для легковых автомобилей. """
        return super().start_engine() + " Готов к поездке!"

    def __str__(self) -> str:
        """ Возвращает строковое представление легкового автомобиля. """
        return f"{super().__str__()} с {self.doors} дверями."

    def __repr__(self) -> str:
        """ Возвращает официальное строковое представление легкового автомобиля. """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year}, doors={self.doors})"


class Truck(Vehicle):
    """ Класс грузового автомобиля, наследуется от Vehicle. """

    def __init__(self, make: str, model: str, year: int, payload_capacity: float):
        """
        Инициализирует грузовой автомобиль.

        :param make: Производитель
        :param model: Модель
        :param year: Год выпуска
        :param payload_capacity: Грузоподъемность в тоннах
        """
        super().__init__(make, model, year)
        self._payload_capacity = payload_capacity  # Непубличный атрибут

    @property
    def payload_capacity(self) -> float:
        return self._payload_capacity

    def start_engine(self) -> str:
        """ Переопределяет запуск двигателя, добавляя специфическое поведение для грузовых автомобилей. """
        return super().start_engine() + " Готов к перевозке груза!"

    def __str__(self) -> str:
        """ Возвращает строковое представление грузового автомобиля. """
        return f"{super().__str__()} с грузоподъемностью {self.payload_capacity} тонн."

    def __repr__(self) -> str:
        """ Возвращает официальное строковое представление грузового автомобиля. """
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year}, payload_capacity={self.payload_capacity})"


if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Corolla", year=2020, doors=4)
    my_truck = Truck(make="Ford", model="F-150", year=2019, payload_capacity=2.5)

    print(my_car)          # Отображает информацию о легковом автомобиле
    print(repr(my_car))   # Официальная строка представления легкового автомобиля

    print(my_truck)       # Отображает информацию о грузовом автомобиле
    print(repr(my_truck)) # Официальная строка представления грузового автомобиля

    print(my_car.start_engine())  # Запускает двигатель легкового автомобиля
    print(my_truck.start_engine()) # Запускает двигатель грузового автомобиля