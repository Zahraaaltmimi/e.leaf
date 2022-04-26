import imp
from flask import Flask, jsonify, render_template, request, redirect
from flask_session import Session
from cs50 import SQL
import json
import sqlite3

app = Flask(__name__)
# DB = SQL('sqlite:///database.db')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# main page
@app.route("/")
def index():
    conn = db_connection()
    cursor = conn.cursor()
    data = cursor.execute('SELECT * FROM Product order by random() limit 8').fetchall()
    print(data)
    return render_template("HOME.html", context=data)

#Amyen code 
def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite")
    except sqlite3.error as error:
        print(error)
    return conn


@app.route("/signup", methods=["GET", "POST"])
def adduser():
    print (request)

    # if request.method == "GET":
    #     cursor = conn.execute("SELECT * FROM User")
    #     users = [
    #         dict(name=row[1],surname=row[2],email=row[3],phone=row[4])
    #         for row in cursor.fetchall()
    #     ]
    #     if users is not None:
    #         return jsonify(users)
    if request.method == "POST":
        # check if post works
        conn = db_connection()
        cursor = conn.cursor()
        name = request.form.get("name")
        surname = request.form.get("surname")
        email = request.form.get("email")
        phone = request.form.get("phone")

        #return f'{name} {email} {surname} {phone}'
        insert_query = """INSERT INTO User(name,surname,email,phone)
        VALUES (?,?,?,?)"""
        cursor = cursor.execute(insert_query,(name,surname,email,phone))
        conn.commit()
        return f"User with the id: {cursor.lastrowid} created!"
    return render_template("Sign_up.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("Sign_in.html")

@app.route("/about")
def about():
    return render_template("ABOUT_US.html")

@app.route("/blog")
def blog():
    return render_template("Blog.html")

@app.route("/candle")
def candle():
    conn = db_connection()
    cursor = conn.cursor()
    data = cursor.execute('SELECT * FROM Product WHERE categories = "candels"').fetchall()
    print(data)
    return render_template("candle.html", context=data)

@app.route("/cart")
def cart():
    return render_template("Cart.html")

@app.route("/products/<page_id>/")
def product(page_id=0):
    db = SQL("sqlite:///db.sqlite")
    try:
        data = db.execute('SELECT * FROM Product WHERE id = ?', page_id)
    
        conn = db_connection()
        cursor = conn.cursor()
        related = cursor.execute('SELECT * FROM Product WHERE id != ? AND categories = ?', (data[0]['id'], data[0]['categories'])).fetchall()
    except:
        return redirect("/")
    print(data)
    return render_template("cartproduct.html", context=[data, related])

@app.route("/checkout")
def checkout():
    return render_template("Checkout.html")

@app.route("/contact")
def contact():
    return render_template("CONTACT.html")

@app.route("/faq")
def faq():
    return render_template("FAQ.html")

@app.route("/order-complite")
def order_complite():
    return render_template("order-complite.html")

@app.route("/plants")
def plants():
    conn = db_connection()
    cursor = conn.cursor()
    data = cursor.execute('SELECT * FROM Product WHERE categories = "plants"').fetchall()
    print(data)
    return render_template("plants.html", context=data)

@app.route("/plastic")
def plastic():
    
    conn = db_connection()
    cursor = conn.cursor()
    data = cursor.execute('SELECT * FROM Product WHERE categories = "plastic Alternatives"').fetchall()
    print(data)
    return render_template("plastic.html", context=data)

@app.route("/plastic2")
def plastic2():
    return render_template("plastic2.html")

@app.route("/self-care")
def self_care():
    conn = db_connection()
    cursor = conn.cursor()
    data = cursor.execute('SELECT * FROM Product WHERE categories = "self-care"').fetchall()
    print(data)
    return render_template("Self_Care.html", context=data)

@app.route("/self2")
def self2():
    return render_template("self2.html")

@app.route("/self3")
def self3():
    return render_template("self3.html")

if __name__ == '__main__':
    app.run()
