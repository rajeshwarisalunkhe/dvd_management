import csv
import MySQLdb
from constant import *
from comman import print_entry




def WRITE_CSV():

    print("===============================")
    print("EXPORT DATABASE TO CSV:")
    print("===============================")

    file = raw_input("Enter base filename (will be given a .csv extension):")
    file = file + ".csv"

    db = MySQLdb.connect("localhost", "rajeshwari", "rss9860", "dvd_mgnt")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to select all record of the database.
    sql = "SELECT * FROM dvd"

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        with open(file, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['title', 'star', 'costar', 'year', 'genre']) # write headers
            csv_writer.writerows(results)

    except:
        print "Error: unable to fecth data"

    print file
    print("created successfully")
    db.close()
