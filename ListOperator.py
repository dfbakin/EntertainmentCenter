import operator
from enum import Enum
from Media import Media
from random import choice


class MediaType(Enum):
    Unknown: 0
    Book: 1
    Movie: 2
    Game: 3
    Track: 4


# TODO can be done iterable
class ListOperator:
    def __init__(self, elem_type):
        self.media: list[Media] = []
        # TODO implement Enum (did't figure out how to)
        # self.type = MediaType.Unknown
        self.type = elem_type

    # adding a new element to the media
    def add(self, element: Media):
        return self.media.append(element)

    # sorting and returning collection by a key
    # view code sample in main.py
    def sort(self, key: str):
        # TODO
        # test this Value check
        # test for sorting by attributes, that are not in Media
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if key not in Media.__dir__:
            raise ValueError("Key must be a name of an attribute")

        self.media = sorted(self.media, key=operator.attrgetter(key))

    # the following method deletes instances that do not satisfy the key
    def filter(self, key: str, value):
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if key not in Media.__dir__:
            raise ValueError("Key must be a name of an attribute")

        # TODO
        # test this filtering
        self.media = [elem for elem in filter(lambda x: x.key == value, self.media)]

    # TODO fix
    # doesn't work because of comparasion of custom classes in python
    # hash? id?
    def __and__(self, other: list[Media]):
        set_of_media = set(self.media)
        set_of_other_media = set(other)
        return list(set_of_media.intersection(set_of_other_media))

    def __bool__(self):
        return bool(self.media)

    def __sub__(self, other: list[Media]):
        set_of_media = set(self.media)
        set_of_other_media = set(other)
        return list(set_of_media.difference(set_of_other_media))

    def __add__(self, other: list[Media]):
        # extends the self.media and returns it
        return self.media.extend(other)

    def print(self, lines_number: int):
        printing_str = ""
        for element in self.media[:lines_number]:
            printing_str += str(element.__repr__())
        return printing_str

    def pick_random(self):
        return choice(self.media)

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
