from flask import Flask, render_template

# Create Flask instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
    first_name = 'Kuba'
    stuff = "This is <strong> Bold</strong> Text"
    favorite_pizza = ['Pepperoni', 'Margherita', 41]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# Custom Error Pages

# Invalid URL 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Invalid URL 500 error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
