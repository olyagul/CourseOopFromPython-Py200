from chemical_element import ChemicalElement
from chemical_compound import ChemicalCompound
from lab_glassware import LabGlassware


class Metal(ChemicalElement):
    """
    Металл
    """
    def get_type(self) -> str:
        return "металл"


class NonMetal(ChemicalElement):
    """
    Неметалл
    """
    def get_type(self) -> str:
        return "неметалл"


class Acid(ChemicalCompound):
    """
    Кислота
    """
    def get_compound_type(self) -> str:
        return "кислота"


class Salt(ChemicalCompound):
    """
    Соль
    """
    def get_compound_type(self) -> str:
        return "соль"


class Beaker(LabGlassware):
    """
    Стакан
    """
    def get_glass_type(self) -> str:
        return "стакан"


class Flask(LabGlassware):
    """
    Колба
    """
    def get_glass_type(self) -> str:
        return "колба"
