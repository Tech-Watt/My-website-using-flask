from flask import Flask,redirect,request,render_template,url_for,send_from_directory
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import os 
from twilio.rest import Client

# twillo settings
account_sid = "AC39d7673c726845598e97fe0a86117427"
auth_token = "5c0cdc2927fd3c602fc25408aac62794"
client = Client(account_sid, auth_token)

# flask configurations
app  =  Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logins'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'OASIS'
app.config['UPLOADER'] ='static/images'


@app.route('/',methods = ['POST','GET'])
def hom():
    image = os.path.join(app.config['UPLOADER'],'TECH1.png')
    image1 = os.path.join(app.config['UPLOADER'],'firsts.png')
    video = os.path.join(app.config['UPLOADER'],'watts.mp4')
    u1 = os.path.join(app.config['UPLOADER'],'u1.jpg')
    u2 = os.path.join(app.config['UPLOADER'],'u2.jpg')
    u3 = os.path.join(app.config['UPLOADER'],'u3.jpg')
    u4 = os.path.join(app.config['UPLOADER'],'u4.jpg')

    u5 = os.path.join(app.config['UPLOADER'],'u5.jpg')
    u6 = os.path.join(app.config['UPLOADER'],'u6.jpg')
    u7 = os.path.join(app.config['UPLOADER'],'u7.jpg')
    u8 = os.path.join(app.config['UPLOADER'],'u8.jpg')
    return render_template('home.html',images = image,image1 = image1,
                           video=video,u1=u1,u2=u2,u3=u3,u4=u4,u5=u5,
                           u6=u6,u7=u7,u8=u8)


@app.route('/courses',methods = ['POST','GET'])
def courses():   
    image = os.path.join(app.config['UPLOADER'],'TECH1.png')

    c1 = os.path.join(app.config['UPLOADER'],'c1.jpg')
    c2 = os.path.join(app.config['UPLOADER'],'c2.jpg')
    c3 = os.path.join(app.config['UPLOADER'],'c3.jpg')
    c4 = os.path.join(app.config['UPLOADER'],'c4.jpg')
    c5 = os.path.join(app.config['UPLOADER'],'c5.jpg')
    c6 = os.path.join(app.config['UPLOADER'],'c6.jpg')
    c7 = os.path.join(app.config['UPLOADER'],'c7.jpg')
    c8 = os.path.join(app.config['UPLOADER'],'c8.jpg')
    u1 = os.path.join(app.config['UPLOADER'],'u1.jpg')
    u5 = os.path.join(app.config['UPLOADER'],'u5.jpg')
    u2 = os.path.join(app.config['UPLOADER'],'u2.jpg')
    u3 = os.path.join(app.config['UPLOADER'],'u3.jpg')
    u4 = os.path.join(app.config['UPLOADER'],'u4.jpg')
    u6 = os.path.join(app.config['UPLOADER'],'u6.jpg')
    u7 = os.path.join(app.config['UPLOADER'],'u7.jpg')
    u8 = os.path.join(app.config['UPLOADER'],'u8.jpg')
    return render_template('courses.html',logo=image,c1=c1,c2=c2,c3=c3,
                           c4=c4,c5=c5,c6=c6,c7=c7,c8=c8,u1=u1,u5=u5,u2=u2,u3=u3
                           ,u4 = u4,u6=u6,u7=u7,u8=u8)



@app.route('/signin',methods = ['POST','GET'])
def signin():
    images = os.path.join(app.config['UPLOADER'],'tech1.png')
    if request.method == 'POST':
        email = request.form['email']
        message = client.messages.create(
        body = email,
        from_="+19282778990",
        to="+233257330594"
        )
        
        return redirect('/signin')
       
    return render_template('signin.html',images = images)


if __name__ == "main":
    app.run(debug=True)