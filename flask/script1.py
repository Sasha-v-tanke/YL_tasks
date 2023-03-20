from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit_form():
    # Получение данных из формы
    surname = request.form['surname']
    name = request.form['name']
    email = request.form['email']
    jobs = []
    for i in range(1, 17):
        jobs.append(request.form.get("job" + str(i)))
    education = request.form['qualification']
    gender = request.form['gender']
    motivation = request.form['motivation']
    stay_on_mars = request.form.get('stay_on_mars')

    file = request.files['file']

    return 'Анкета успешно отправлена!'


if __name__ == '__main__':
    app.run(debug=True)
