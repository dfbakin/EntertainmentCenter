import wikipediaapi
import webbrowser

from main import Media


# TODO doc strings with required data types
#  probably comments (I can't imagine where they are necessary here)

def lang_of_symbol(c: str):
    if 122 >= ord(c.lower()) >= 97:
        return 'en'
    else:
        return 'ru'


class Movie(Media):
    def __init__(self, *args):
        filename, duration, director, main_actor, year, short_description = args[-6:]
        super(Media, args[:-6]).__init__()
        self.__filename = filename
        self.duration = duration
        self.director = director
        self.main_actor = main_actor
        self.short_description = short_description
        self.year = year

    def get_filename(self):
        pass

    # TODO get-set to all unique parameters for Movie: duration, director, etc.

    def __str__(self):
        return f'Фильм снят режисером {self.director} в {self.year} году. В главной роли снимается {self.main_actor}. {self.short_description}'

    def __repr__(self):
        return f'Фильм снят режисером {self.director} в {self.year} году. В главной роли снимается {self.main_actor}. {self.short_description}'

    def open_wiki(self):
        lang = lang_of_symbol(self.name[0])
        wiki = wikipediaapi.Wikipedia(lang)
        page = wiki.page(f'{self.name}(film)')
        if page.exists():
            webbrowser.open(page.fullurl)
        else:
            # TODO change print to raise error
            print('Wiki page not found')
    # TODO method save...
    #  def save(self, ent_center_inst: EntertainmentCenter)
    #  call method save(ent_center_inst, self, *argd),
    #  where args is the list with all the parameters unique for class Movie
