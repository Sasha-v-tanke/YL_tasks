from flask import Flask, render_template, request
from setuptools._entry_points import render

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    title = request.args.get("title", "Колонизация Марса")
    return render_template("base.html", title=title)


@app.route('/training/<profession>')
def training(profession):
    return render_template('training.html', profession=profession.lower())


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['Пилот', 'Инженер', 'Астроном', 'Биолог', 'Химик', 'Геолог', 'Врач', 'Строитель']

    return render_template('list_prof.html', professions=professions, list=list)


if __name__ == "__main__":
    app.run()
