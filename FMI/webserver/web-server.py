from flask import Flask, render_template, url_for, redirect, request
from station import weather as w



app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/bergen")
def bergen():

    return render_template('bergen.html', weather=w.bergentemps)

@app.route("/oslo")
def oslo():
    w.oslo()
    return render_template('oslo.html', weather=w.oslotemps)

@app.route("/karmøy")
def karmøy():

    return render_template('karmøy.html', weather=w.karmøytemps)



@app.route('/day')
def Day():
    req = request.args.get('day')
    day = int(req[:2])
    print(day)
    loc = req
    print(loc)
    
    if 'Bergen' in loc:
        return render_template('day.html', weather=w.bergentemps)
    elif 'Karmøy' in loc:   
        return render_template('day.html', weather=w.karmøytemps)
    elif 'Oslo' in loc:
        w.oslo(day)
        return render_template('day.html', weather=w.oslotemps, days=day)

if __name__ == '__main__':
    app.run(debug=True)
    