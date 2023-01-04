from flask import render_template, url_for, flash, redirect
from .forms import RegistrationForm, LoginForm
from flaskblog import app
from flaskblog.models import User, Post

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
        return redirect(
            url_for("hello")
        )  # url_for uses the name of the method not the string argument in the app.route() decorator
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("hello"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

