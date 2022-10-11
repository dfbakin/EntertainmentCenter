from Media import Media


class Book(Media):
    def __init__(self, *args):
        super().__init__(*args[:-2])
        filename, num_of_pages = args[-2:]
        self.filename = filename
        self.num_of_pages = num_of_pages

    @property
    def num_of_pages(self):
        return self._num_of_pages

    @num_of_pages.setter
    def num_of_pages(self, new_num):
        if new_num.isdigit():
            self._num_of_pages = new_num
        else:
            raise ValueError('Number of pages must be integer!')

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, new_filename):
        print('setter is called')
        self._filename = new_filename

    def get_file_obj(self):
        return open(self.filename, mode='r', encoding='utf-8')

    def quote_for_article(self):
        return f'{self.author}, {self.name}. {self.year}. {self.num_of_pages} с.'

    def get_content(self):
        return self.get_file_obj().read().strip()


Book('123')
