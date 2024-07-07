from flask import Flask, render_template, request, redirect, session
import mysql.connector

    # pip install mysql-connector-python
    # from flask import flask, render_template, request, redirect, session
    # import mysql.connector

app = Flask(__name__)

# For Form

app.config['SECREY_KEY']='ZAZA1234567890807022393'

# For DB

db_host = "localhost"
db_user = "root"
db_pass = ""
db_name = "flower"

@app.route("/home")
def home():
    # return"<h1>Home</h1>"
    name = "lisa"
    age = 27
    my_dict={"name": "Lisa", "age": 27 }
    return render_template("home.html", name=name, age=age, my_dict=my_dict)

@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@app.route("/store", methods=["POST"])
def store():
    # from flask import flask, render_template, request
    if request.method == "POST":
        flower_name = request.form['flower_name']
        lat_num = request.form['lat_num']
        long_name = request.form['long_name']
        place = request.form['place']
        detail = request.form['detail']
        print(flower_name, lat_num, long_num, place, detail)

        # Connect Database
        my_db = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_pass,
        db = db_name
        )
        my_cursor = my_db.cursor(dictionary=True)
        sql = "INSERT INTO flowers (flower_name, lat_num, long_num, place, detail) VALUES (%s,%s,%s,%s,%s)"
        val = (flower_name, lat_num, long_num, place, detail)
        my_cursor.execute(sql,val)
        my_db.commit()
        # my_db.commit() ใช้ได้แต่ไม่ค่อยมีใครทำกัน

    return redirect('/home')

if __name__=="__main__":
    app.run(debug=True)
    # app.run()
    # debug ทำงานจริงไม่ใช้กัน

