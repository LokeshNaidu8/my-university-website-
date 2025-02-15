from flask import Flask, redirect, render_template, request, session
from database2 import adddata, fetchuserpwd, fetchdata, deleteUser

# create object of the flask class
app = Flask(__name__)


@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/admins")
def admin():
    return render_template("admin.html")


@app.route("/abouts")
def about():
    return render_template("about.html")


@app.route("/blogs")
def blog():
    return render_template("blog.html")


@app.route("/contacts")
def contact():
    return render_template("contact.html")


@app.route("/courses")
def course():
    return render_template("course.html")


@app.route("/studentablelink")
def homefun():
    if(session.get('name')):
        f = fetchdata()
        return render_template("studentable.html", data=f)
    else:
        return redirect("/validlogin")


@app.route("/savelink", methods=["POST"])
def save():
    name = request.form["name"]
    email = request.form["email"]
    subject = request.form["subject"]
    message = request.form["message"]
    t = (name, email, subject, message)
    adddata(t)
    return redirect("contacts")


@app.route("/deleteuser/<int:id>")
def DELETE_USER(id):
    if(request.method == "GET"):
        deleteUser(id)
    f = fetchdata()
    return render_template("studentable.html", data=f)


# validate user login.html
@app.route("/validlogin", methods=["GET", "POST"])
def validloginfun():
    session.clear()
    error = None
    if (request.method == "POST"):
        session['name'] = request.form.get("name")
        session['pwd'] = request.form.get("password")
        f = fetchuserpwd()
        for i in f:
            if session['name'] == i[0] and session['pwd'] == i[1]:
                text = "Successfully Login."
                return redirect("/studentablelink")
            else:
                error = "Invalid credentials. Check Username and Password or register."
    return render_template("admin.html")


if __name__ == "__main__":
    app.secret_key = "super secret key"
    app.run(debug=True)
