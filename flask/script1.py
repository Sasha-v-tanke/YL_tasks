from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Установка директории для загрузки фотографий
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    # Отображение страницы с формой
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    # Загрузка и сохранение фотографии
    file = request.files['image']
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('show_image', filename=filename))


@app.route('/<filename>')
def show_image(filename):
    # Отображение загруженной фотографии на странице
    return render_template('show_image.html', filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
