# TODO all integers and bools to str and then valid data:
#  whether it's possible to convert to required type
class Media:
    """
    # name -> str  # название книги
    # author -> str  # автор книги
    # year -> int  # год написания
    # genre -> genre  # жанр
    # rating -> float  # оценка книги в широких массах
    # age_restriction -> int  # возрастное ограничение
    """

    def __init__(self, name: str = "Some media", author: str = "Ivan Ivanov", year: str = "1970", genre: str =
    "default_genre",
                 rating: str = "0",
                 age_restriction: str = "21"):

        self.name = name

        if not year.isdigit():
            raise TypeError("Year is not an integer")
        self.year = int(year)

        if not rating.isdigit():
            raise TypeError("Rating is not an integer")
        self.rating: int = int(rating)

        if not age_restriction.isdigit():
            raise TypeError("Age_restriction is not an integer")
        self.age_restriction: int = int(age_restriction)

        self.author = author

        self.genre = genre

    def __hash__(self):
        return hash(self.name)

    # property can't be called the same as attribute.
    #  "RecursionError: maximum recursion depth exceeded" because return self.name calls @property
    #  that's why we use "_" in front of a var name (I didn't know the reason too)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("The name must be a string.")

        self._name = new_name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author: str):
        if not isinstance(new_author, str):
            raise TypeError("Author must be a str.")
        self._author = new_author

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year: int):
        if not isinstance(new_year, int):
            raise TypeError("The year must be an integer.")
        if new_year < 0:
            raise ValueError("The year must be a positive integer.")
        self._year = new_year

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, new_genre: str):
        if not isinstance(new_genre, str):
            raise TypeError("Genre must be a string.")
        self._genre = new_genre

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating: int):
        if not isinstance(new_rating, int):
            raise TypeError("Rating must be an integer.")
        if new_rating > 100 or new_rating < 0:
            raise ValueError("Rating is not in [0, 100] interval.")
        self._rating = new_rating

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, new_age_restriction: int):
        if not isinstance(new_age_restriction, int):
            raise TypeError("Age_restriction must be an integer.")
        if new_age_restriction < 0 or new_age_restriction > 21:
            raise ValueError("Age restriction is not appropriate.")
        self._age_restriction = new_age_restriction

    def __str__(self):
        return f"Name: {self.name}; Authored by {self.author}; Genre:  {self.genre}; Rating of " \
               f"{self.rating}; For people over {self.age_restriction}."

    def __eq__(self, other: "Media"):
        if self.__hash__() == other.__hash__():
            return 1
        else:
            return 0

# TODO
# save(inst_type, *args):
# save
# to
# csv
