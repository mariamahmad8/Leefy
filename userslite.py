import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

def createUserTable():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # according to google if you add not exists then it wont create it again and again so we don't get error
    c.execute("""CREATE TABLE IF NOT EXISTS users( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            
    )""")
    conn.commit()
    conn.close()

def createPlantTable(): 
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS plants( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            
    )""")
    conn.commit()
    conn.close()





# Call the function to create the user table
createUserTable()

# to connect to home page
@app.route('/signup')
def signup():  # according to video, 'home' is standard naming convention, cuz home page is the first page you see, but I changed it to signup, cuz homepage is different
    return render_template('sign_up.html')


@app.route('/signin')
def signin(): 
    return render_template('sign_in.html')

# OKAY NOW WE GOTTA GO GET /METHOD POST THINGY FROM HTML
# since we are retrieving information, we need "cursor" from that dude's video
@app.route("/signup", methods=['POST', 'GET'])  # Fixed to use a list
def user_information(): 
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # okay so now we have RETRIEVED THE information, 
    # we need to ADD into the database. remember CURSOR and EXECUTE from man

    if flask.request.method == 'POST':
        #add an if statement here checking if its post
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()  # cursor lets us connect to the DB and edit
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
    elif flask.request.method == 'GET': 
        pass
        #add an if statemetn here checking if its get instead
        #retrieve the information

    conn.close()
    return("worked")

if __name__ == '__main__':
    app.debug = True
    app.run()


