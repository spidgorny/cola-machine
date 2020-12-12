from flask import Flask, redirect, render_template, url_for
import os
import time

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/dev')
def dev():
    return render_template('dev.html')


@app.route('/drink/<int:id>')
def drink(id):
    return render_template('drink.html')


@app.route('/cola/<int:seconds>')
def cola(seconds):
    # run motor  for 5 seconds
    motorOn(1, seconds)
    # return 'Cola for ' + str(seconds) + ' ready'
    return redirect(url_for('hello_world'))


@app.route('/fanta/<int:seconds>')
def fanta(seconds):
    # run motor 2 for 5 seconds
    motorOn(2, seconds)
    # return 'Fanta ready for ' + str(seconds)
    return redirect(url_for('hello_world'))


@app.route('/sprite/<int:seconds>')
def sprite(seconds):
    # run motor 3 for 5 seconds
    motorOn(3, seconds)
    # return 'Fanta ready for ' + str(seconds)
    return redirect(url_for('hello_world'))


def motorOn(motorID, seconds):
    os.system('uhubctl/uhubctl -l 1-1.2 -p ' + str(motorID) + ' -a 1')
    time.sleep(seconds)
    os.system('uhubctl/uhubctl -l 1-1.2 -p ' + str(motorID) + ' -a 1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
