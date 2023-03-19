from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mission_name():
    return "Миссия Колонизация Марса"


@app.route("/index")
def mission_slogan():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def mission_promotion():
    return '''Человечество вырастает из детства.<br>
              Человечеству мала одна планета.<br>
              Мы сделаем обитаемыми безжизненные пока планеты.<br>
              И начнем с Марса!<br>
              Присоединяйся!'''


@app.route("/image_mars")
def mission_image():
    return """<!DOCTYPE html>
                <html>
                    <head>
                        <title>Привет, Марс!</title>
                    </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/img.png" alt="Mars">
                        <p>Мы скоро прилетим!</p>
                    </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080)
