from abc import ABC, abstractmethod


class Mesurable2D(ABC):

    @abstractmethod
    def perimeter(self) -> float:
        """compute perimeter of this instance
        """

    @abstractmethod
    def surface(self) -> float:
        """compute surface of this instance
        """