from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')  
@app.route('/index')        						#This is the main URL
def index():
    return render_template("index.html",title="home",name="index")		#The argument should be in templates folder

@app.route('/interests')   
def interests():
    return render_template("interests.html",title="interests",name="interests")

#Add the code for courses
@app.route('/courses')   
def courses():
    return render_template("courses.html",title="courses",name="courses")
#Add the code for other
@app.route('/other')   
def other():
    return render_template("other.html",title="other",name="other")
#Hmmm, do we need another one?


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
