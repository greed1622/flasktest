from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/studentprofile', methods=['POST','GET'])
def studentprofile():
    if request.method == "POST":
        fname = request.form['fname']
        mname = request.form['mname']
        lname = request.form['lname']
        suffix = request.form['suffix']
        age = request.form['age']
        dob = request.form['dob']
        return render_template('studentprofile.html', fname=fname, mname=mname, lname=lname, age=age, suffix=suffix, dob=dob)
    else:
        return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/w3schools')
def w3schools():
    return render_template('w3schools.html')

if __name__=="__main__":
    app.run(debug=True)