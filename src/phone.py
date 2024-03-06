from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Cannot add Phone with non-Phone object")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
