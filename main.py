import csv
import datetime
import os
from random import choice

# import only if file is run, not imported
if __name__ == '__main__':
    from Movies import Movie
    from Games import Game
    from ListOperator import ListOperator
    from Book import Book


# main class of the project: manages collections of media
class EntertainmentCenter:
    def __init__(self):
        # self.music = ListOperator(Track)
        self.books = ListOperator(Book)
        self.games = ListOperator(Game)
        self.movies = ListOperator(Movie)
        # default path to the save file is generated with the current timestamp
        self.path_to_file = f"data/{int(datetime.datetime.now().timestamp())}.csv"

    # the following methods prints as many lines as requires
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
        if not (self.games or self.books or self.movies):
            raise ValueError('All collections are empty')
        while cnt < num_of_lines:
            # random collection
            collection = choice([self.games, self.books, self.movies])
            print(choice(collection.media))
            cnt += 1
        print('====================')

    # method to load data from CSV file
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
                elif row[0] == '3':
                    self.games.add(Game(*row[1:]))
                elif row[0] == '4':
                    self.movies.add(Movie(*row[1:]))
                else:
                    raise ValueError("CSV file is not correct")

    # method to save all data of media to default or custom CSV file
    def save(self, special_path=None):
        csv_data = []

        for collection in (self.books, self.games, self.movies):
            for inst in collection.media:
                row = []
                # type of obj  is the first parameter in CSV file
                if isinstance(inst, Book):
                    row.append('1')
                elif isinstance(inst, Game):
                    row.append('3')
                elif isinstance(inst, Movie):
                    row.append('4')
                # adding the rest of the attributes
                row.extend([inst.name, inst.author, inst.year,
                            inst.genre, inst.rating, inst.age_restriction, *inst.get_args()])
                csv_data.append(list(map(str, row)))
        current_path = special_path if special_path else self.path_to_file
        if os.path.exists(current_path):
            os.remove(current_path)
        with open(current_path, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=',', quotechar='|')
            writer.writerows(csv_data)


# BOOK: '<type:1 - book>,<name>,<author>,<year>,<genre>,<rating>,<age_restriction>,<filename>'


if __name__ == '__main__':
    sample = EntertainmentCenter()
    sample.load('data/sample.csv')

    print('3 random media')
    sample.print_random_media(num_of_lines=3)

    center_1 = EntertainmentCenter()
    center_1.load('data/sample_1.csv')
    center_2 = EntertainmentCenter()
    center_2.load('data/sample_2.csv')

    print('sorted list of Movies by "year":')
    sample.movies.sort('year', print_res=True)
    print('=============')
    sample.movies.sort('year', print_res=True, reverse=True)
    print()
    print('sorted list of movies by name:')
    sample.movies.sort('name', print_res=True)
    print('=============')
    sample.movies.sort('name', print_res=True, reverse=True)

    print()

    print('====================')
    print('6 random media')
    center_2.print_random_media(num_of_lines=6)

    print('books in common:')
    for elem in (center_1.books & center_2.books):
        print(elem)
    print()

    new_game = Game('GTA5', 'Rockstar', '2015', 'Roleplay/Action', '96', '18', 'PC/PS4/PS3', True)
    print(f'adding{new_game}')
    sample.games.add(new_game)
    print()
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
