from flask import Flask, render_template
import os
import time

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/cola/<int:seconds>')
def cola(seconds):
    # run motor  for 5 seconds
    motorOn(4, seconds)
    return 'Cola for ' + str(seconds) + ' ready'


@app.route('/fanta/<int:seconds>')
def fanta(seconds):
    # run motor 2 for 5 seconds
    motorOn(2, seconds)
    return 'Fanta ready for ' + str(seconds)

@app.route('/sprite/<int:seconds>')
def sprite(seconds):
    # run motor 3 for 5 seconds
    motorOn(3, seconds)
    return 'Fanta ready for ' + str(seconds)

def motorOn(motorID, seconds):
    os.system('uhubctl/uhubctl -l 1-1.2 -p ' + str(motorID) + ' -a 1')
    time.sleep(seconds)
    os.system('uhubctl/uhubctl -l 1-1.2 -p ' + str(motorID) + ' -a 0')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
