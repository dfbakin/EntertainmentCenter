import wikipediaapi
import webbrowser
from datetime import datetime

from main import Media, EntertainmentCenter, save


# TODO doc strings with required data types
#  probably comments (I can't imagine where they are necessary here)

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
    '''
    #filename -> str # private arg, sets only in initialization.
    #duration -> int # duration of the film
    #director -> str # Name of the director
    #main_actor -> str # Name of the main actor
    #short_description -> str, len(description) <= 500 (because short) # description of the film
    #year -> int # the year the film was shot
    '''

    def __init__(self, *args):
        filename, duration, director, main_actor, year, short_description = args[-6:]
        super(Media, args[:-6]).__init__()
        self.__filename = filename
        self.duration = duration
        self.director = director
        self.main_actor = main_actor
        self.short_description = short_description
        self.year = year

    # getters and setters
    @property
    def filename(self):
        return self.__filename

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):
        if type(duration) != int:
            raise TypeError('Duration must be an integer')
        self.duration = duration

    @property
    def director(self):
        return self.director

    @director.setter
    def director(self, name):
        if type(name) != str:
            raise TypeError('Name of director must be a string')
        self.director = name

    @property
    def main_actor(self):
        return self.main_actor

    @main_actor.setter
    def main_actor(self, name):
        if type(name) != str:
            raise TypeError('Name must be a string')
        self.main_actor = name

    @property
    def short_description(self):
        return self.short_description

    @short_description.setter
    def short_description(self, description):
        if type(description) != str:
            raise TypeError('Description must be a string')
        if len(description) > 500:
            raise ValueError('Length of description must be less than 500 symbols')
        self.short_description = description

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year):
        if type(year) != int:
            raise TypeError('Year must be an integer')
        if year > datetime.now().year:
            raise ValueError('Wow. The film from the future. LMAO')
        self.year = year

    def __str__(self):
        return f'Фильм снят режисером {self.director} в {self.year} году. В главной роли снимается {self.main_actor}. {self.short_description}'

    def __repr__(self):
        return f'Фильм снят режисером {self.director} в {self.year} году. В главной роли снимается {self.main_actor}. {self.short_description}'

    def open_wiki(self):
        '''
        This function open in browser the wiki page of film
        '''
        lang = lang_of_symbol(self.name[0])  # get lang of Wiki page
        wiki = wikipediaapi.Wikipedia(lang)
        page = wiki.page(f'{self.name}(film)')  # get Wiki page

        # checking the existence of page
        if page.exists():
            webbrowser.open(page.fullurl)
        else:
            raise WikiError(page)

    def save(self, ent_center_inst: EntertainmentCenter):
        save(ent_center_inst, self,
             [self.__filename, self.duration, self.director, self.main_actor, self.short_description, self.year])


class WikiError(BaseException):
    def __init__(self, page):
        self.page = page
