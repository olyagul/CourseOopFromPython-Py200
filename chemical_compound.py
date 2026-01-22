from abc import ABC, abstractmethod

class ChemicalCompound(ABC):
    """
    Класс для химического соединения

    Пример:
    >>> from compounds import Acid
    >>> water = Acid("Вода", "H2O", 18.0)
    >>> water.name
    'Вода'
    """

    def __init__(self, name: str, formula: str, molar_mass: float):
        """
        Создает соединение

        name: название
        formula: формула
        molar_mass: масса
        """

        if not name or not name.strip():
            raise ValueError("Название не может быть пустым")
        if not formula or not formula.strip():
            raise ValueError("Формула не может быть пустой")
        if molar_mass <= 0:
            raise ValueError("Масса должна быть больше 0")

        self.name = name
        self.formula = formula
        self.molar_mass = molar_mass

    @abstractmethod
    def get_compound_type(self) -> str:
        """
        Возвращает тип соединения

        Пример:
        >>> from compounds import Acid
        >>> hcl = Acid("Соляная кислота", "HCl", 36.5)
        >>> hcl.get_compound_type()
        'кислота'
        """
        pass

    def get_mass(self, moles: float) -> float:
        """
        Считает массу

        moles: количество молей (должно быть > 0)

        Пример:
        >>> from compounds import Acid
        >>> co2 = Acid("Углекислый газ", "CO2", 44.0)
        >>> co2.get_mass(2)
        88.0
        """
        if moles <= 0:
            raise ValueError("Количество молей должно быть больше 0")
        return self.molar_mass * moles

    def __str__(self) -> str:
        return f"{self.name} - {self.formula}"