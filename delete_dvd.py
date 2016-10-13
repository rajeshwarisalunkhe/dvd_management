# -*- coding: utf-8 -*-
import MySQLdb
from constant import *
from comman import print_entry



def SQL_DELETE_DVD(title):
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

        print("===============================")
        print("DVD TO DELETE:")
        print("===============================")
        for row in results:
            title = row[TITLE]
            star = row[STAR]
            costar = row[COSTAR]
            year = row[YEAR]
            genre = row[GENRE]
      
        print_entry(title, star, costar, year, genre)
        print("===============================")
        print("Are you sure you want to delete?")
        print("Y/y = yes, Anything else = No")
        choice = raw_input("Enter a choice and press enter:")

        if(choice == 'y' or choice == 'Y'):
            sql = "DELETE FROM dvd WHERE title = '%s'" % (title)

            try:
            # Execute the SQL command
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
                print("Item deleted")
            except:
                # Rollback in case there is any error
                db.rollback()

    except:
        print "Error: unable to fecth data"

    # disconnect from server
    db.close()


def DELETE_DVD():
    print("===============================")
    print("DELETE A DVD RECORD:")
    print("===============================")
    title = raw_input("Enter the title of the DVD to delete:")

    SQL_DELETE_DVD(title)
