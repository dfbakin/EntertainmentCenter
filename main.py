import os
import csv
import datetime


class ListOperator:
    pass


class EntertainmentCenter:
    def __init__(self):
        self.music = ListOperator(Track)
        self.books = ListOperator(Book)
        self.games = ListOperator(Game)
        self.movies = ListOperator(Movie)
        self.path_to_file = str(datetime.datetime.now().time())
        pass

    def load(self, path_to_file='data/sample.csv'):
        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"File {path_to_file} not found.")
        self.path_to_file = path_to_file
        with open(path_to_file, newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for row in reader:
                if row[0] == '1':
                    self.books.add(Book(row[1:]))
                elif row[0] == '2':
                    self.music.add(Track(row[1:]))
                elif row[0] == '3':
                    self.music.add(Game(row[1:]))
                elif row[0] == '4':
                    self.books.add(Movie(row[1:]))
                else:
                    raise ValueError("CSV file is not correct")

    def save(self):
        for collection in (self.music, self.books, self.games, self.movies):
            for inst in collection:
                inst.save(self)


BOOK: '<type:1 - book>,<name>,<author>,<year>,<genre>,<ration>,<age_restriction>,<filename>'


def read_csv_data(path):
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',', quotechar='|')
        return [line for line in reader if line]


# method from Media class
def save(self, center_inst, obj_inst, *args):
    prev_data = read_csv_data(center_inst.path_to_file)
    if obj_inst.__class__ not in [Book, Track, Movie, Game]:
        raise TypeError(f'Expected from [Book, Track, Movie, Game], got {obj_inst.__class__} instead')
    with open(center_inst.path_to_file, mode='w+', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|')
        current_id = obj_inst.id
        data = []
        if isinstance(obj_inst, Book):
            data.append('1')
        elif isinstance(obj_inst, Track):
            data.append('2')
        elif isinstance(obj_inst, Game):
            data.append('3')
        elif isinstance(obj_inst, Movie):
            data.append('4')
        data.extend([str(obj_inst.id), obj_inst.name, obj_inst.author, str(obj_inst.year),
                     obj_inst.genre, str(obj_inst.rating),
                     str(obj_inst.age_restriction), *list(map(str, args))])
        for i in range(len(prev_data)):
            if prev_data[i][1] == current_id:
                prev_data[i] = data

        writer.writerows(list(map(str, prev_data)))


if __name__ == '__main__':
    print(read_csv_data('data/sample.csv'))
    # print(EntertainmentCenter().__class__)
