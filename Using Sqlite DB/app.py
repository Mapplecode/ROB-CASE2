#importing the imp library that we have to use
from flask import Flask, flash,render_template, request,flash
import sqlite3 as sql
# sqlite libray use to connect and make all the action on the sqlite DB

app = Flask(__name__)
#create the object for the flask app

@app.route('/',methods = ['POST', 'GET'])
#create route to the host and route can handle two method GET and POST
def index():
    if request.method == 'POST':
        #condition is Post reaquest the come inside and insert into db
        try:
            #exception handling
            firstname = request.form['fname']
            lastname = request.form['lname']
            # firstname and lastname comming from the form
            with sql.connect("database.db") as con:
                #open the connection
                cur = con.cursor()
                #initialize the connection
                cur.execute("INSERT INTO Users (first, last) VALUES (?,?)",(firstname,lastname))
                #query to insert into users table
                msg = "Record successfully added"
                #message that appear as alert in the frontend
                con.commit()
                #commit the data into db
        except:
            #exception occurs and error apper then come to this block
            con.rollback()
            #get rollback to the 
            msg = "error in insert operation"
        finally:
            #always run this block
            con.close()
            #close the connection
            return render_template("index.html", msg=msg)
            #server template to the frontend
    return render_template("index.html")
    #return the template when get request come


if __name__ == '__main__':
    #flask app constructor
    app.run()
    #main a call for flask app