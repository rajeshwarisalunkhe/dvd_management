# -*- coding: utf-8 -*-
import MySQLdb
from constant import *


def SQL_ADD_DVD(title, star, costar, year, genre):
    db = MySQLdb.connect("localhost", "rajeshwari", "rss9860", "dvd_mgnt")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO dvd(title, star, costar, year, genre) \
           VALUES ('%s', '%s', '%s', '%d', '%d' )" % \
           (title, star, costar, year, genre)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def ADD_DVD():
    add_title = raw_input("Enter the DVD title:")
    add_star = raw_input("Enter the name of the movie’s star:")
    add_costar = raw_input("Enter the name of the movie’s costar:")
    add_year = int(raw_input("Enter the year the movie was released:"))
    for key in GENRE_TYPE:
        print("Enter %s for %s" % (key, GENRE_TYPE[key]))
    add_genre = int(raw_input())

    SQL_ADD_DVD(add_title, add_star, add_costar, add_year, add_genre)
