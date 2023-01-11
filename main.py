from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.jinja2")

    if request.method == 'POST':
        return render_template("app.jinja2", diceNumber=int(request.form['diceNumber']),
                               sideNumber=int(request.form['sideNumber']))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
