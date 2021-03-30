from flask import Flask, render_template, request,flash
from flask_mysqldb import MySQL
# MySql library use to connect the  mysqlclient to our code 

app = Flask(__name__)
#create the object for the flask app

#initialize all the MYSQL client to connect to communicate with flask app 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'
app.secret_key = 'supersecretkey'
mysql = MySQL(app)
#create mysql object call

@app.route('/', methods=['GET', 'POST'])
#create route to the host and route can handle two method GET and POST
def index():
    if request.method == "POST":
        #condition is Post reaquest the come inside and insert into db
        details = request.form
        #getting data from the form and store that data into datails varibale
        firstName = details['fname']
        lastName = details['lname']   
        flash("Sucessfully inserted!!")   
        # cur = mysql.connection.cursor()
        #open the connection
        # cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        # query to insert into users table
        # mysql.connection.commit()
        #commit the data into db
        # cur.close()
        # close the mysql connection
        # return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    #flask app constructor
    app.run()
    #main a call for flask app