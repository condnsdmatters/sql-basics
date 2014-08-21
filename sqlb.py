#Create a SQLite3 database and table
#UPDATE: now including error handler

#import the sqlite3 library
import sqlite3

#create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()


try:
#insert data
    cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)") 
    cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

#commit the changes
    conn.commit()

except sqlite3.OperationalError:
    print "Oops! Something went wrong. Try again, bud..."
#close database connection
conn.close()




