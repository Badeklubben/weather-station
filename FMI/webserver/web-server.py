from flask import Flask, render_template, url_for, redirect, request
from station import weather as w
from station import structuring as s


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/bergen")
def bergen():
    w.bergen()
    return render_template('bergen.html', weather=w.bergentemps)

@app.route("/oslo")
def oslo():
    w.oslo()
    # avg_temp(w.oslotemps)
    return render_template('oslo.html', weather=w.oslotemps)

@app.route("/karmøy")
def karmøy():
    w.karmøy()
    # s.avg_temp(w.karmøytemps)
    return render_template('karmøy.html', weather=w.karmøytemps)



@app.route('/day')
def Day():
    req = request.args.get('day')
    day = int(req[0])
    loc = req
    print(loc)
    if 'Bergen' in loc:
        return render_template('day.html', weather=w.bergentemps, days=int(day))
    elif 'Karmøy' in loc:
        return render_template('day.html', weather=w.karmøytemps, days=int(day))
    elif 'Oslo' in loc:
        return render_template('day.html', weather=w.Oslo, days=int(day))

if __name__ == '__main__':
    app.run(debug=True)
    