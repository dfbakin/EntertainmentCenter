from Media import Media

'''
Book
    args list consists of all necessary params for Media and:
        filename: str
        num_of_pages: int
        every attribute has getter and setter that returns int if apropriate, else str
        
        
    def get_file_obj -> stream.io
    FileNotFound 

    def quote_for_article -> str

    def get_content(self) -> str with file content

    def get_args(self) -> list of unique from class Media attributes 

'''

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
        self._filename = new_filename

    def get_file_obj(self):
        return open(self.filename, mode='r', encoding='utf-8')

    def quote_for_article(self):
        return f'{self.author}, {self.name}. {self.year}. {self.num_of_pages} с.'

    def get_content(self):
        return self.get_file_obj().read().strip()

    def get_args(self):
        return [self.filename,
                self.num_of_pages]
