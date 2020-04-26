from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fabrizio'}
    return render_template('index.html', title='Home', user=user)


@app.route('/contact-me')
def contactme():
    user = {'username': 'Fabrizio'}
    return render_template('contact-me.html')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

