from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html", title="Matportalen")

@app.route('/<name>')
def restaurant(name):
    return render_template("restaurant.html", title=name)


if __name__ == '__main__':
    app.run(debug=True)

