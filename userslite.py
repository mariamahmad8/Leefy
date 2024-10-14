import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='public')

def createUserTable():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    # according to google if you add not exists then it wont create it again and again so we don't get error
    c.execute("""CREATE TABLE IF NOT EXISTS users( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

# Call the function to create the user table
createUserTable()

# to connect to home page
@app.route('/')
def home():  # according to video, 'home' is standard naming convention, cuz home page is the first page you see
    return render_template('./sign_up.html')

# OKAY NOW WE GOTTA GO GET /METHOD POST THINGY FROM HTML
# since we are retrieving information, we need "cursor" from that dude's video
@app.route("/signup", methods=['POST'])  # Fixed to use a list
def user_information(): 
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # okay so now we have RETRIEVED THE information, 
    # we need to ADD into the database. remember CURSOR and EXECUTE from man
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()  # cursor lets us connect to the DB and edit
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

    print("worked")

if __name__ == '__main__':
    app.debug = True
    app.run()
