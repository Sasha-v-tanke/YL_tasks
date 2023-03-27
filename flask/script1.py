from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    title = request.args.get("title", "Колонизация Марса")
    return render_template("base.html", title=title)


@app.route('/training/<profession>')
def training(profession):
    return render_template('training.html', profession=profession.lower())


if __name__ == "__main__":
    app.run()
