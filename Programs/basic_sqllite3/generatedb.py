#!python3

from contextlib import contextmanager
import sqlite3

name = ""


@contextmanager
def create_db(name):
    try:
        conn = sqlite3.connect('%s.db' % name)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.close()


def prompt_for_name():
    name = input("What would you like to name your test db file?: ")
    return name


if __name__ == "__main__":
    name = prompt_for_name()
    with create_db(name) as cursor:
        cursor.execute("""CREATE TABLE Information
                        (Name TEXT, Address TEXT, Phone_Number INT, Birthday TEXT)
                        """)
        print(f'{name} has been created')
