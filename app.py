from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/contactus')
def contactus():
    return render_template('/contactus.html')

@app.route('/about')
def about():
    return render_template('/about.html')
@app.route('/studentprofile', methods=['GET','POST'])
def studentprofile():
    if request.method=="POST":
        fname=request.form['fname']
        mname=request.form['mname']
        lname=request.form['lname']
        suffix=request.form['suffix']
        age=request.form['age']
        dob=request.form['dob']
        gender=request.form['gender']
        status=request.form['status']
        houseno=request.form['houseno']
        purok=request.form['purok']
        subdivision=request.form['subdivision']
        barangay=request.form['barangay']
        municipality=request.form['municipality']
        province=request.form['province']
        zip=request.form['zip']
        return render_template('studentprofile.html', fname=fname,mname=mname,lname=lname,suffix=suffix,age=age,dob=dob,gender=gender,status=status,houseno=houseno,purok=purok,subdivision=subdivision,barangay=barangay,municipality=municipality,province=province,zip=zip)
    else:
        return render_template('/index.html')