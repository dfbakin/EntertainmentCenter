import os
import csv
import datetime

# from Media import Media
if __name__ == '__main__':
    from Movies import Movie
    from Games import Game
    from ListOperator import ListOperator


class Track:
    pass


class Book:
    pass


class EntertainmentCenter:
    def __init__(self):
        self.music = ListOperator(Track)
        self.books = ListOperator(Book)
        self.games = ListOperator(Game)
        self.movies = ListOperator(Movie)
        self.path_to_file = f"data/{int(datetime.datetime.now().timestamp())}.csv"

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
        csv_data = []
        for collection in (self.music, self.books, self.games, self.movies):
            for inst in collection.media:
                row = []
                if isinstance(inst, Book):
                    row.append('1')
                elif isinstance(inst, Track):
                    row.append('2')
                elif isinstance(inst, Game):
                    row.append('3')
                elif isinstance(inst, Movie):
                    row.append('4')
                row.extend([inst.name, inst.author, inst.year,
                            inst.genre, inst.rating, inst.age_restriction, *inst.get_args()])
                csv_data.append(list(map(str, row)))
        if os.path.exists(self.path_to_file):
            os.remove(self.path_to_file)
        with open(self.path_to_file, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|')
            writer.writerows(csv_data)


# BOOK: '<type:1 - book>,<name>,<author>,<year>,<genre>,<ration>,<age_restriction>,<filename>'


# method from Media class
def save(self, center_inst, obj_inst, *args):
    if obj_inst.__class__ not in [Book, Track, Movie, Game]:
        raise TypeError(f'Expected from [Book, Track, Movie, Game], got {obj_inst.__class__} instead')
    with open(center_inst.path_to_file, mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|')
        data = []
        if isinstance(obj_inst, Book):
            data.append('1')
        elif isinstance(obj_inst, Track):
            data.append('2')
        elif isinstance(obj_inst, Game):
            data.append('3')
        elif isinstance(obj_inst, Movie):
            data.append('4')
        data.extend([obj_inst.id, obj_inst.name, obj_inst.author, obj_inst.year,
                     obj_inst.genre, obj_inst.rating, obj_inst.age_restriction, *args])
        writer.writerow(list(map(str, data)))


if __name__ == '__main__':
    sample = EntertainmentCenter()
    sample.movies.add(
        Movie("Some media", "Ivan Ivanov", 0, "fiction", 0, 16, '123', 12, 'qwe', 'ewq', 1974, '12345678'))
    sample.movies.add(
        Game("the media", "vitaliy", 0, "shooter", 0, 18, ))
    sample.save()
