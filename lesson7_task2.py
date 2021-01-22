# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @abstractmethod
    def tissue_consumption(self):
        return 0

    @property
    def common_consumption(self):
        return round((self.V / 6.5 + 0.5) + (self.H * 2 + 0.3), 2)

class Coat(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def tissue_consumption(self):
        return round(self.V / 6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, V, H):
        super().__init__(V, H)

    def tissue_consumption(self):
        return round(self.H * 2 + 0.3, 2)

coat = Coat(2, 1)
suit = Suit(2, 1)

print(coat.tissue_consumption())
print(suit.tissue_consumption())

print(coat.common_consumption)
print(suit.common_consumption)