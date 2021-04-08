from flask import Flask, render_template, url_for, redirect, request
from station import weather as w



app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/bergen")
def bergen():
    w.bergen()
    return render_template('bergen.html', weather=w.bergentemps, title='Bergen', style="/bergen.css")

@app.route("/oslo")
def oslo():
    w.oslo()
    return render_template('oslo.html', weather=w.oslotemps, title='Oslo')

@app.route("/karmøy")
def karmøy():
    w.karmøy()
    return render_template('karmøy.html', weather=w.karmøytemps, title='Karmøy')



@app.route('/day')
def Day():
    req = request.args.get('day')
    day = int(req[:2])
    
    print(day)
    loc = req
    print(loc)
    
    if 'Bergen' in loc:
        w.bergen(day)
        return render_template('day.html', weather=w.bergentemps, title="Bergen daily", style="/bergen.css")
    elif 'Karmøy' in loc:
        w.karmøy(day)   
        return render_template('day.html', weather=w.karmøytemps, title="Karmøy daily", style="/karmøy.css")
    elif 'Oslo' in loc:
        w.oslo(day)
        return render_template('day.html', weather=w.oslotemps, title="Oslo daily", style="/oslo.css")

if __name__ == '__main__':
    app.run(debug=True)
    