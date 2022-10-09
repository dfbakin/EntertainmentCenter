import operator
from enum import Enum

import Media


class MediaType(Enum):
	Unknown: 0
	Book: 1
	Movie: 2
	Game: 3
	Track: 4


class ListOperator:
	def __init__(self):
		self.media: list[Media.Media] = []
		self.type = MediaType.Unknown

	def add(self, element: Media.Media):
		return self.media.append(element)

	def sort(self, key: str):
		#TODO
		# test this Value check
		# test for sorting by attributes, that are not in Media
		if not isinstance(key, str):
			raise TypeError("Key must be a string")
		if key not in Media.Media.__dir__:
			raise ValueError("Key must be a name of an attribute")

		self.media = sorted(self.media, key=operator.attrgetter(key))
		return None

	def filter(self, key: str, value):

		if not isinstance(key, str):
			raise TypeError("Key must be a string")
		if key not in Media.Media.__dir__:
			raise ValueError("Key must be a name of an attribute")

		#TODO
		# test this filtering
		self.media = [elem for elem in filter(self.media, lambda x: x.key == value)]
		return None

	def save(self):
		raise NotImplemented

	def __and__(self, other: list[Media.Media]):
		set_of_media = set(self.media)
		set_of_other_media = set(other)
		return list(set_of_media.intersection(set_of_other_media))

	def __sub__(self, other: list[Media.Media]):
		set_of_media = set(self.media)
		set_of_other_media = set(other)
		return list(set_of_media.difference(set_of_other_media))

	def __add__(self, other: list[Media.Media]):
		# extends the self.media and returns it
		return self.media.extend(other)

	def print(self, lines_number: int):
		printing_str = ""
		for element in self.media[:lines_number]:
			printing_str += str(element.__repr__())
		return printing_str

# 	@methods
#
# 	add -> if not isinstance(new_inst, type)
# 		filter(author=None, below_rating=0, name=None,
# 		       earlier_year=datetime.datetime.now().year(?), below_age_restrictions = 21)->int = cnt(how
# 		many
# 		books
# 		were
# 		deleted)
# 		if cnt == 0:
# 			Warning('...')
#
# 	get_random
# 	save() - implement
# 	save()
# 	to
# 	all
# 	instances
#
# 	print(lines=10, print_all=False) -> < lines > strs
#
# 	override - & +
