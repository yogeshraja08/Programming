# pip install flask
# pip install flask_mysqldb

from flask import Flask,render_template,url_for,redirect,flash,request
from flask_mysqldb import MySQL

app = Flask(__name__)
# mySQL connection 
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="YoN"
app.config["MYSQL_PORT"]= 8402
app.config["MYSQL_PASSWORD"]="Yogesh@08"
app.config["MYSQL_DB"]="python_db"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

# loading home page
@app.route("/")
def home():
    con = mysql.connection.cursor()
    qry = """create table if not exists users(
                id integer primary key auto_increment,
                name varchar(20),
                age integer,
                city varchar(20)
            );"""
    con.execute(qry)
    qry = "select * from users;"
    con.execute(qry)
    res = con.fetchall()
    return render_template("home.html",datas=res)

#new user
@app.route("/addUsers",methods=["POST","GET"])
def addusers():
    con = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]
        qry = "insert into users (name,age,city) value (%s,%s,%s);"
        con.execute(qry,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    flash("user details added")
    return render_template("addusers.html")

#edit User
@app.route("/editUsers/<string:id>",methods=["GET","POST"])
def editusers(id):
    con = mysql.connection.cursor()
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        city = request.form["city"]
        qry = "update users set name=%s ,age=%s ,city=%s where id=%s"
        con.execute(qry,[name,age,city,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    qry = "select * from users where id=%s"
    con.execute(qry,[id])
    res = con.fetchone()
    flash("user details updated")
    return render_template("editUsers.html",datas=res)

#delete users
@app.route("/deleteUser/<string:id>",methods=["POST","GET"])
def deleteusers(id):
    con = mysql.connection.cursor()
    qry = "delete from users where id=%s"
    con.execute(qry,id)
    mysql.connection.commit()
    con.close()
    flash("user details deleted")
    return redirect(url_for("home"))

if (__name__ == '__main__'):
    app.secret_key = "yon"
    app.run(debug=True)