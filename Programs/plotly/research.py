import collections
import csv
import os


data = []

Show = collections.namedtuple(
    'Show',
    'show_id,type,title,director,cast,country,date_added,'
    'release_year,rating,duration,listed_in,description'
)


def init():
    base_folder = os.path.dirname(__file__)
    filename = os.path.join(base_folder, 'Data', 'netflix_titles.csv')

    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)

        data.clear()
        for row in reader:
            show = parse_row(row)
            data.append(show)


def parse_row(row):
    row['show_id'] = str(row['show_id'])
    row['type'] = str(row['type'])
    row['title'] = str(row['title'])
    row['director'] = str(row['director'])
    # row['cast'] = str(row['cast'])
    # row['country'] = str(row['country'])
    row['date_added'] = str(row['date_added'])
    row['release_year'] = str(row['release_year'])
    row['rating'] = str(row['rating'])
    # row['duration'] = str(row['duration'])
    row['listed_in'] = str(row['listed_in'])
    # row['description'] = str(row['description'])

    show = Show(
        **row
    )

    return show


init()
print(data[0])
