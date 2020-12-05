from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/cola/<int:seconds>')
def cola(seconds):
    # run motor 2 for 5 seconds
    return 'Cola for ' + str(seconds) + ' ready'


@app.route('/fanta/<int:seconds>')
def fanta(seconds):
    # run motor 2 for 5 seconds
    return 'Fanta ready for ' + str(seconds)
