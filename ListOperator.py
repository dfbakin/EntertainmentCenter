import operator
from random import choice

from Media import Media


class ListOperator:
    def __init__(self, elem_type):
        self.media: list[Media] = []
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

    def __and__(self, other: "ListOperator"):
        set_of_media = set(self.media)
        set_of_other_media = set(other.media)
        return list(set_of_media.intersection(set_of_other_media))

    def __bool__(self):
        return bool(self.media)

    def __sub__(self, other: "ListOperator"):
        set_of_media = set(self.media)
        set_of_other_media = set(other.media)
        return list(set_of_media.difference(set_of_other_media))

    def __add__(self, other: "ListOperator"):
        # extends the self.media and returns it
        return self.media.extend(other.media)

    def print(self, lines_number: int):
        printing_str = ""
        for element in self.media[:lines_number]:
            printing_str += str(element.__repr__())
        return printing_str

    def pick_random(self):
        return choice(self.media)

    def __getitem__(self, item_number):
        if item_number >= len(self.media):
            IndexError("Wrong index")
        else:
            return self.media[item_number]
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
