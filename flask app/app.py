from flask import Flask, render_template, request, redirect, url_for, session
from model import init_db, add_user, check_user

app = Flask(__name__)
app.secret_key = "secret123"   # fixed spelling

# initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # Your registration logic here
    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if check_user(username, password):
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return f"Welcome, {session['user']}!"


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
