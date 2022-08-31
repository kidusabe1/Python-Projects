#Customer Relationship Management Tool(CRM Tool)
import tkinter
from PIL import ImageTk,Image
import mysql.connector

root=tkinter.Tk()
root.title("CRM Tool")
root.geometry("400x400")

#my_database is just a connector with the mysql
my_database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Holly1232@abebe",
)

# Now we have to create a cursor, that will be 
# going through our database

my_cursor=my_database.cursor()

# This is the part where we create our own database

#  my_cursor.execute("CREATE DATABASE CRM")
#Since the Database is already created once, we dont 
#need to recreate it every time the program runs,
#therefore we can comment it out

#TO check if the database is created:

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)
# DATABASES CREATED SUCCESFULLY
my_cursor.execute("CREATE TABLE tasks()")




root.mainloop()
