import MySQLdb

from add_dvd import ADD_DVD
from delete_dvd import DELETE_DVD
from modify_dvd import MODIFY_DVD
from lookup_dvd import LOOKUP_DVD
from csvreport_dvd import WRITE_CSV


while True:
    print("================================")
    print("DVD DATABASE")
    print("================================")
    print("1 - Add a DVD to the database")
    print("2 - Search inventory")
    print("3 - Modify DVD record")
    print("4 - Delete DVD record")
    print("5 - Export listing to CSV")
    print("6 - Exit")
    print("================================\n")

    choice = int(raw_input("Enter a choice and press enter:"))

    if(choice == 1):
        ADD_DVD()
    elif(choice == 2):
        LOOKUP_DVD()
    elif(choice == 3):
        MODIFY_DVD()
    elif(choice == 4):
        DELETE_DVD()
    elif(choice == 5):
        WRITE_CSV()
    elif(choice == 6):
        print("Exiting...")
        break
    else:
        print("Wrong choice, Enter choice from given number")



