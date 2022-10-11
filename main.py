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

    def print_lines(self, num_of_lines=10, print_all=False):
        i = 0
        for collection in (self.music, self.books, self.games, self.movies):
            for inst in collection.media:
                print(inst)
                i += 1
                if not print_all and i >= num_of_lines:
                    print('====================')
                    return

        print('====================')

    def load(self, path_to_file='data/sample.csv'):
        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"File {path_to_file} not found.")
        self.path_to_file = path_to_file
        with open(path_to_file, newline='') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for row in reader:
                if not row:
                    continue
                if row[0] == '1':
                    self.books.add(Book(*row[1:]))
                elif row[0] == '2':
                    self.music.add(Track(*row[1:]))
                elif row[0] == '3':
                    self.music.add(Game(*row[1:]))
                elif row[0] == '4':
                    self.books.add(Movie(*row[1:]))
                else:
                    raise ValueError("CSV file is not correct")

    def save(self, special_path=None):
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
        current_path = special_path if special_path else self.path_to_file
        if os.path.exists(current_path):
            os.remove(current_path)
        with open(current_path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|')
            writer.writerows(csv_data)


# BOOK: '<type:1 - book>,<name>,<author>,<year>,<genre>,<ration>,<age_restriction>,<filename>'


if __name__ == '__main__':
    sample = EntertainmentCenter()
    sample.load('data/test_sample.csv')
    sample.print_lines()
    quit()
    sample.save('data/new_test.csv')
    quit()
    sample.movies.add(
        Movie("Some media", "Ivan Ivanov", 0, "fiction", 0, 16, '123', 12, 'qwe', 'ewq', 1974, '12345678'))
    sample.movies.add(
        Game("the media", "vitaliy", 0, "shooter", 0, 18, ))
    sample.save(special_path='data/test_sample.csv')
