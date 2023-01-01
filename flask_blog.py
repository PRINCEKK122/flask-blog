from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
