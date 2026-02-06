class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

        @property
        def name(self) -> str:
            return self.name

        @name.setter
        def name(self, value: str):
            raise AttributeError

        @property
        def author(self) -> str:
            return self._author

        @author.setter
        def author(self, value: str):
            raise AttributeError

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        # self.name = name
        # self.author = author
        super().__init__(name, author)
        self.pages = pages

        @property
        def pages(self) -> int:
            return self.pages

        @pages.setter
        def pages(self, value):
            if not isinstance(value, int):
                raise TypeError("Количество страниц целое число")
            if value <= 0:
                raise ValueError("Количество страниц положительно")
            self.pages = value


    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"

    def __str__(self):
        return f"{super().__str__()}. Страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        # self.name = name
        # self.author = author
        super().__init__(name, author)
        self.duration = duration

        @duration.setter
        def duration(self, value):
            if not isinstance(value, (int, float)):
                raise TypeError("Продолжительность должна быть числом")
            if value <= 0:
                raise ValueError("Продолжительность должна быть положительным числом")
            self._duration = float(value)

        def __str__(self):
            return f"{super().__str__()}. Продолжительность: {self.duration:.2f} ч."

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

    # def __str__(self):
    #     return f"Книга {self.name}. Автор {self.author}"
