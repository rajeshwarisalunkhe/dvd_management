# -*- coding: utf-8 -*-
import MySQLdb
from comman import print_entry
from constant import *


def SQL_LOOKUP_DVD(variable, value):
    # Open database connection
    db = MySQLdb.connect("localhost", "rajeshwari", "rss9860", "dvd_mgnt")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to search a record into the database.
    sql = "SELECT * FROM dvd WHERE %s = '%s'" % (variable, value)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            title = row[TITLE]
            star = row[STAR]
            costar = row[COSTAR]
            year = row[YEAR]
            genre = row[GENRE]
      
        print_entry(title, star, costar, year, genre)
    except:
        print "Error: unable to fecth data"

    # disconnect from server
    db.close()


def LOOKUP_DVD():
    print("===============================")
    print("DVD LOOKUP:")
    print("===============================")
    print("Enter the criteria to look up by:")
    print("1 - Movie title")
    print("2 - Star")
    print("3 - Costar")
    print("4 - Year released")
    print("5 - Genre")
    choice = int(raw_input("Type a number and press enter:"))

    if(choice == 1):
        title = raw_input("Enter the DVD title to search for:")
        variable = "title"
        SQL_LOOKUP_DVD(variable, title)
    elif(choice == 2):
        star = raw_input("Enter the name of the movie’s star:")
        variable = "star"
        SQL_LOOKUP_DVD(variable, star)
    elif(choice == 3):
        costar = raw_input("Enter the name of the movie’s costar:")
        variable = "costar"
        SQL_LOOKUP_DVD(variable, costar)
    elif(choice == 4):
        year = int(raw_input("Enter the year the movie was released:"))
        variable = "year"
        SQL_LOOKUP_DVD(variable, year)
    elif(choice == 5):
        genre = int(raw_input("Enter the genre:- 1 for Drama, 2 for horror, 3 for comedy, 4 for romance:"))
        variable = "genre"
        SQL_LOOKUP_DVD(variable, genre)
