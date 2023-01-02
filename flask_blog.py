from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "eaace66504036762549d64aca993ef2b"

posts = [
    {
        "author": "Prince Awuah Karikari",
        "title": "Blog 1",
        "content": "First content",
        "date_posted": "January 1, 2023",
    },
    {
        "author": "John Doe",
        "title": "Blog 2",
        "content": "Second content",
        "date_posted": "April 21, 2018",
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("hello")) # url_for uses the name of the method not the string argument in the app.route() decorator
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)
