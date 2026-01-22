from abc import ABC, abstractmethod


class ChemicalElement(ABC):
    """
    Класс для химического элемента.

    Пример:
    >>> from elements import Metal
    >>> iron = Metal("Железо", "Fe", 26)
    >>> iron.name
    'Железо'
    """

    def __init__(self, name: str, symbol: str, atomic_number: int):
        """
        Создает элемент.

        name: название
        symbol: символ
        atomic_number: номер
        """

        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        if not symbol or not symbol.strip():
            raise ValueError("Символ не может быть пустым")
        if atomic_number <= 0:
            raise ValueError("Атомный номер должен быть больше 0")

        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number

    @abstractmethod
    def get_type(self) -> str:
        """
        Возвращает тип.

        Пример:
        >>> from elements import Metal
        >>> gold = Metal("Золото", "Au", 79)
        >>> gold.get_type()
        'металл'
        """
        pass

    def is_light(self) -> bool:
        """
        Проверяет легкий ли элемент.

        Пример:
        >>> from elements import Metal
        >>> h = Metal("Водород", "H", 1)
        >>> h.is_light()
        True
        """
        return self.atomic_number < 20

    def __str__(self) -> str:
        return f"{self.name} ({self.symbol})"