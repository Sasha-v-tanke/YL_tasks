from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def planet_invite(planet_name):
    return render_template('index.html', name=planet_name)


if __name__ == '__main__':
    app.run(debug=True)
