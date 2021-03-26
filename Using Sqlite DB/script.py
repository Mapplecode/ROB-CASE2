import sqlite3
#importing the library

#connect to the sqlite database as well open the connection
conn = sqlite3.connect('database.db')
print("Opened database successfully")

#query to create table in the database
conn.execute('CREATE TABLE Users (first TEXT, last TEXT)')
print("Table created successfully")   

#close the connection
conn.close()
