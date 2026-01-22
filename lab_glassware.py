from abc import ABC, abstractmethod


class LabGlassware(ABC):
    """
    Класс для лабораторной посуды

    Пример:
    >>> from glassware import Beaker
    >>> glass = Beaker("Стакан", 250.0)
    >>> glass.name
    'Стакан'
    """

    def __init__(self, name: str, max_volume: float):
        """
        Создает посуду

        name: название (не может быть пустым)
        max_volume: максимальный объем (должен быть > 0)
        """

        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        if max_volume <= 0:
            raise ValueError("Объем должен быть больше 0")

        self.name = name
        self.max_volume = max_volume
        self.current_volume = 0.0
        self.content = None

    @abstractmethod
    def get_glass_type(self) -> str:
        """
        Возвращает тип посуды

        Пример:
        >>> from glassware import Beaker
        >>> beaker = Beaker("Стакан", 200.0)
        >>> beaker.get_glass_type()
        'стакан'
        """
        pass

    def pour(self, liquid: str, volume: float) -> bool:
        """
        Наливает жидкость

        liquid: что наливаем
        volume: сколько

        Пример:
        >>> from glassware import Beaker
        >>> tube = Beaker("Пробирка", 50.0)
        >>> tube.pour("Вода", 30.0)
        True

        Пример с ошибкой:
        >>> tube.pour("Вода", -10.0)
        Traceback (most recent call last):
            ...
        ValueError: Объем должен быть больше 0

        >>> tube.pour("Вода", 60.0)
        False
        """

        if volume <= 0:
            raise ValueError("Объем должен быть больше 0")

        if volume <= self.max_volume:
            self.content = liquid
            self.current_volume = volume
            return True
        return False

    def empty(self) -> None:
        """
        Опустошает посуду

        Пример:
        >>> from glassware import Beaker
        >>> glass = Beaker("Стакан", 100.0)
        >>> glass.pour("Пиво", 50.0)
        True
        >>> glass.empty()
        >>> glass.content
        None
        """
        self.content = None
        self.current_volume = 0.0

    def __str__(self) -> str:
        if self.content:
            return f"{self.name}: {self.content} ({self.current_volume} мл)"
        return f"{self.name}: пустая"