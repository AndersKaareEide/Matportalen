from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("base.html", title="Matportalen")

@app.route('/restaurant/<name>')
def audun(name):
    return render_template("base.html", title=name)


if __name__ == '__main__':
    app.run(debug=True)
