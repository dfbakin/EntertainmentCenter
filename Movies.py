import webbrowser

import wikipediaapi

from Media import Media
import webbrowser
from datetime import datetime
import os
from main import EntertainmentCenter


def lang_of_symbol(c: str):
    """

    :param c: symbol from line
    :return: 'en' - if the lang of symbol is english
             'ru' - in other situation
    """
    if 122 >= ord(c.lower()) >= 97:
        return 'en'
    return 'ru'


class Movie(Media):
    """
	#filename -> str # private arg, sets only in initialization.
	#duration -> int # duration of the film
	#director -> str # Name of the director
	#main_actor -> str # Name of the main actor
	#short_description -> str, len(description) <= 500 (because short) # description of the film
	#year -> int # the year the film was shot
	"""

    def __init__(self, *args):
        filename, duration, director, main_actor, short_description = args[-5:]
        super().__init__(*args[:-5])
        self.__filename = filename
        if not os.path.exists(filename):
            open(filename, mode='w').close()
        self._duration = duration
        self._director = director
        self._main_actor = main_actor
        self._short_description = short_description

    # getters and setters
    @property
    def filename(self):
        return self.__filename

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if type(duration) != int:
            raise TypeError('Duration must be an integer')
        self._duration = duration

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, name):
        if type(name) != str:
            raise TypeError('Name of director must be a string')
        self._director = name

    @property
    def main_actor(self):
        return self._main_actor

    @main_actor.setter
    def main_actor(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        self._main_actor = name

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, description):
        if type(description) != str:
            raise TypeError('Description must be a string')
        if len(description) > 500:
            raise ValueError('Length of description must be less than 500 symbols')
        self._short_description = description

    def __str__(self):
        return f'Фильм снят режиссером {self.director} в {self.year} году. В главной роли снимается' \
               f' {self.main_actor}. {self.short_description}'

    def __repr__(self):
        return f'Фильм снят режиссером {self.director} в {self.year} году. В главной роли снимается' \
               f' {self.main_actor}. {self.short_description}'

    def open_wiki(self):
        """
		This function open in browser the wiki page of film
		"""
        lang = lang_of_symbol(self.name[0])  # get lang of Wiki page
        wiki = wikipediaapi.Wikipedia(lang)
        page = wiki.page(f'{self.name}(film)')  # get Wiki page

        # checking the existence of page
        if page.exists():
            webbrowser.open(page.fullurl)
        else:
            raise WikiError(page)

    def get_args(self):
        return [self.filename, self.duration, self.director, self.main_actor, self.year, self.short_description]

    def save(self, ent_center_inst: EntertainmentCenter):
        save(ent_center_inst, self,
             [self.__filename, self.duration, self.director, self.main_actor, self.short_description])


Movie("Some media", "Ivan Ivanov", "1970", "fiction", "0", "21", '123', "12", 'qwe', 'ewq',
      '12345678')


class WikiError(BaseException):
    def __init__(self, page):
        self.page = page
