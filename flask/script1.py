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


@app.route('/list_prof/<list>')
def list_prof(list):
    professions = ['Пилот', 'Инженер', 'Астроном', 'Биолог', 'Химик', 'Геолог', 'Врач', 'Строитель']

    return render_template('list_prof.html', professions=professions, list=list)


@app.route('/auto_answer', methods=['POST'])
def auto_answer():
    data = {
        'title': 'Ответ на анкету',
        'surname': request.form['surname'],
        'name': request.form['name'],
        'education': request.form['education'],
        'profession': request.form['profession'],
        'sex': request.form['sex'],
        'motivation': request.form['motivation'],
        'ready': request.form.get('ready', 'Нет')
    }
    return render_template('auto_answer.html', **data)


@app.route('/answer')
def answer():
    data = {
        'title': 'Ответ на анкету',
        'surname': 'Иванов',
        'name': 'Иван',
        'education': 'Высшее',
        'profession': 'Инженер-строитель',
        'sex': 'Мужской',
        'motivation': 'Хочу покорить космос',
        'ready': 'Да'
    }
    return render_template('auto_answer.html', **data)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
