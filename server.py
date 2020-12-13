from flask import Flask, redirect, render_template, url_for
import os
import time
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def hello_world():
    return render_template('home.html')


@app.route('/dev')
def dev():
    return render_template('dev.html')


@app.route('/drink/<string:drink>')
def drink(drink):
    return render_template('drink.html', drink=drink)


@app.route('/cola/<int:seconds>')
def cola(seconds):
    # run motor  for 5 seconds
    port = os.getenv('USB_PORT1')
    motorOn(port, seconds)
    # return 'Cola for ' + str(seconds) + ' ready'
    return redirect(url_for('hello_world'))


@app.route('/fanta/<int:seconds>')
def fanta(seconds):
    # run motor 2 for 5 seconds
    port = os.getenv('USB_PORT2')
    motorOn(port, seconds)
    # return 'Fanta ready for ' + str(seconds)
    return redirect(url_for('hello_world'))


@app.route('/sprite/<int:seconds>')
def sprite(seconds):
    # run motor 3 for 5 seconds
    port = os.getenv('USB_PORT3')
    motorOn(port, seconds)
    # return 'Fanta ready for ' + str(seconds)
    return redirect(url_for('hello_world'))


def motorOn(motorID, seconds):
    hub = os.getenv('USB_HUB')
    os.system('uhubctl/uhubctl -l ' + hub + ' -p ' + str(motorID) + ' -a 1')
    time.sleep(seconds)
    os.system('uhubctl/uhubctl -l ' + hub + ' -p ' + str(motorID) + ' -a 1')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
