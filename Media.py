import hashlib
from random import randint

import Author.author


class Media:
	"""
	# name -> str  # название книги
	# author -> Author  # автор книги
	# year -> int  # год написания
	# genre -> genre  # жанр
	# rating -> float  # оценка книги в широких массах
	# age_restriction -> int  # возрастное ограничение
	"""

	def __init__(self, name="Some media", author="Ivan Ivanov", year=0, genre="", rating=0, age_restriction=21):
		if not isinstance(name, str):
			raise TypeError("Name is not a string")
		self.name = name

		if not isinstance(author, Author.author):
			raise TypeError("Author is not an instance of Author class")
		self.author = author

		if not isinstance(year, int):
			raise TypeError("Year is not an integer")
		self.year = year

		if not isinstance(genre, str):
			raise TypeError("Genre is not a string")
		self.genre = genre

		if not isinstance(rating, float):
			raise TypeError("Rating is not a float")
		self.rating = rating

		if not isinstance(age_restriction, int):
			raise TypeError("Age_restriction is not an integer")
		self.age_restriction = age_restriction

		# generating hash for unique ID
		self.id = hashlib.md5(str(randint(1, 10 ** 4)).encode()).digest()[randint(0, 15):randint(16, 27)]

	@property
	def name(self):
		return self.name

	@name.setter
	def name(self, new_name):
		if isinstance(new_name, int):
			raise TypeError("The name must be a string.")

		self.name = new_name

	@property
	def author(self):
		return self.author

	@author.setter
	def author(self, new_author):
		if isinstance(new_author, str):
			raise TypeError("Author must be a str.")
		self.author = new_author

	@property
	def year(self):
		return self.year

	@year.setter
	def year(self, new_year):
		if isinstance(new_year, int):
			raise TypeError("The year must be an integer.")
		if new_year < 0:
			raise ValueError("The year must be a positive integer.")
		self.year = new_year

	@property
	def genre(self):
		return self.genre

	@genre.setter
	def genre(self, new_genre):
		if isinstance(new_genre, str):
			raise TypeError("Genre must be a string.")
		self.genre = new_genre

	@property
	def rating(self):
		return self.rating

	@rating.setter
	def rating(self, new_rating):
		if isinstance(new_rating, int):
			raise TypeError("Rating must be an integer.")
		if new_rating > 100 or new_rating < 0:
			raise ValueError("Rating is not in [0, 100] interval.")
		self.rating = new_rating

	@property
	def age_restriction(self):
		return self.age_restriction

	@age_restriction.setter
	def age_restriction(self, new_age_restriction):
		if isinstance(new_age_restriction, int):
			raise TypeError("Age_restriction must be an integer.")
		if new_age_restriction < 0 or new_age_restriction > 21:
			raise ValueError("Age restriction is not appropriate.")
		self.age_restriction = new_age_restriction

	def __str__(self):
		return f"A media with name: {self.name} authored by {self.author} in genre of {self.genre} and with rating of " \
		       f"{self.rating}, available only for people over {self.age_restriction}. "

# TODO
# save(inst_type, *args):
# save
# to
# csv
