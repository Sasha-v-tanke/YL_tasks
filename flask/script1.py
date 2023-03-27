from flask import Flask, render_template
app = Flask(__name__)


@app.route('/results/<string:nickname>/<int:level>/<float:rating>')
def show_results(nickname, level, rating):
    return render_template('index.html', level=level, nickname=nickname, rating=rating)


if __name__ == '__main__':
    app.run(debug=True)
