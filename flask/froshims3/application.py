import csv
from flask import Flask,redirect,render_template,request

# Configure app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")

    file=open("registrants.csv","a")
    writer = csv.writer(file)
    writer.writerow( (request.form.get("name"),request.form.get("dorm")) )
    file.close()
    return render_template("success.html")