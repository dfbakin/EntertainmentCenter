from enum import Enum


class MediaType(Enum):
	Unknown: 0
	Book: 1
	Movie: 2
	Game: 3
	Track: 4


class ListOperator:
	def __init__(self):
		self.media = []
		self.type = MediaType.Unknown

	def add(self):
		raise NotImplemented

	def sort(self):
		raise NotImplemented

	def filter(self):
		raise NotImplemented

	def save(self):
		raise NotImplemented

	def __and__(self, other):
		raise NotImplemented

	def __sub__(self, other):
		raise NotImplemented

	def __add__(self, other):
		raise NotImplemented

	def print(self):
		raise NotImplemented

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
