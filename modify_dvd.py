# -*- coding: utf-8 -*-
import MySQLdb
from constant import *
from comman import print_entry
import pdb


def MODIFY(variable, old, new):
    # Open database connection
    db = MySQLdb.connect("localhost", "rajeshwari", "rss9860", "dvd_mgnt")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to UPDATE required records
    sql = "UPDATE dvd SET %s = '%s' WHERE %s = '%s'" % (variable, new, variable, old)

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


def SQL_MODIFY_DVD(title):
    # Open database connection
    db = MySQLdb.connect("localhost", "rajeshwari", "rss9860", "dvd_mgnt")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to delete a record into the database.
    sql = "SELECT * FROM dvd WHERE title = '%s'" % (title)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        # disconnect from server
        db.close()
    except:
        print "Error: unable to fecth data"

    for row in results:
        title = row[TITLE]
        star = row[STAR]
        costar = row[COSTAR]
        year = row[YEAR]
        genre = row[GENRE]
      
    print_entry(title, star, costar, year, genre)
    print("===============================")
    print("Type the number for the field")
    print("you want to modify and press Enter:")
    choice = int(raw_input())

    if(choice == 1):
        new_title = raw_input("Enter the new DVD title name:")
        variable = "title"
        MODIFY(variable, title, new_title)
    elif(choice == 2):
        new_star = raw_input("Enter the new DVD star name:")
        variable = "star"
        MODIFY(variable, star, new_star)
    elif(choice == 3):
        new_costar = raw_input("Enter the new DVD costar name:")
        variable = "costar"
        MODIFY(variable, costar, new_costar)
    elif(choice == 4):
        new_year = raw_input("Enter the new DVD year name:")
        variable = "year"
        MODIFY(variable, year, new_year)
    elif(choice == 5):
        new_genre = raw_input("Enter the new DVD genre name:")
        variable = "genre"
        MODIFY(variable, genre, new_genre)


def MODIFY_DVD():
    print("===============================")
    print("MODIFY A DVD RECORD:")
    print("===============================")
    title = raw_input("Enter the title of the DVD to modify:")
    print("===============================")
    print("DVD TO MODIFY:")
    print("===============================")
    SQL_MODIFY_DVD(title)