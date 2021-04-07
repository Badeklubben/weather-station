from flask import Flask, render_template, url_for
from weather import weather as w
from weather import structuring as s
import os
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




if __name__ == '__main__':
    app.run(debug=True)
    