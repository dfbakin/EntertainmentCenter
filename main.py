import os
import csv
import datetime
from random import choice

# from Media import Media
if __name__ == '__main__':
    from Movies import Movie
    from Games import Game
    from ListOperator import ListOperator
    from Book import Book


class EntertainmentCenter:
    def __init__(self):
        # self.music = ListOperator(Track)
        self.books = ListOperator(Book)
        self.games = ListOperator(Game)
        self.movies = ListOperator(Movie)
        self.path_to_file = f"data/{int(datetime.datetime.now().timestamp())}.csv"

    def print_lines(self, num_of_lines=10, print_all=False):
        print('printing list of media instances...')
        i = 0
        for collection in (self.books, self.games, self.movies):
            for inst in collection.media:
                print(inst)
                i += 1
                if not print_all and i >= num_of_lines:
                    print('====================')
                    return

        print('====================')

    def print_random_media(self, num_of_lines=5):
        cnt = 0
        while cnt < num_of_lines:
            collection = choice([self.games, self.books, self.movies])
            print(choice(collection.media))
            cnt += 1
        print('====================')

    def load(self, path_to_file='data/sample.csv'):
        if not os.path.exists(path_to_file):
            raise FileNotFoundError(f"File {path_to_file} not found.")
        self.path_to_file = path_to_file
        with open(path_to_file, newline='', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',', quotechar='|')
            for row in reader:
                if not row:
                    continue
                if row[0] == '1':
                    self.books.add(Book(*row[1:]))
                # elif row[0] == '2':
                # self.music.add(Track(*row[1:]))
                elif row[0] == '3':
                    self.games.add(Game(*row[1:]))
                elif row[0] == '4':
                    self.movies.add(Movie(*row[1:]))
                else:
                    raise ValueError("CSV file is not correct")

    def save(self, special_path=None):
        csv_data = []
        for collection in (self.music, self.books, self.games, self.movies):
            for inst in collection.media:
                row = []
                if isinstance(inst, Book):
                    row.append('1')
                # elif isinstance(inst, Track):
                # row.append('2')
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
    sample.load('data/sample.csv')

    print('3 random media')
    sample.print_random_media(num_of_lines=3)

    # TODO test sorting: 1 ListOperator - 2 keys one by one
    print('sorted list of <what> by <key_1>:')
    # sample.music.sort()
    print('sorted list of <what> by <key_2>:')
    # sample.music.sort()
    print()

    center_1 = EntertainmentCenter()
    center_1.load('data/sample_1.csv')
    center_2 = EntertainmentCenter()
    center_2.load('data/sample_2.csv')

    print('books in common:')
    # for elem in (center_1.books & center_2.books):
    # print(elem)
    print()

    sample.games.add(Game('GTA5', 'Rockstar', 2015, 'Roleplay/Action', 96, 18, 'PC/PS4/PS3', True))
    sample.save('data/new_sample.csv')

    """quit()
    sample = EntertainmentCenter()
    sample.load('data/sample.csv')
    print(type(sample.games.media[0].has_multiplayer))
    quit()
    sample.save('data/sample.csv')
    quit()
    sample.movies.add(
        Movie("Some media", "Ivan Ivanov", 0, "fiction", 0, 16, '123', 12, 'qwe', 'ewq', 1974, '12345678'))
    sample.movies.add(
        Game("the media", "vitaliy", 0, "shooter", 0, 18, ))
    sample.save(special_path='data/test_sample.csv')"""


