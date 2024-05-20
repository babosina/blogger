from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
    first_name = "Vitaly"
    stuff = "Some <strong>Bold</strong> text here"
    pizzas = ["Margarita", "Cheese", "Peperoni", 42]
    return render_template("index.html", first_name=first_name,
                           stuff=stuff,
                           pizzas=pizzas)


# def index():
#     return "<h1>Hello World!</h1>"


# localhost:500/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)  # pass status code
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)  # pass status code
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
