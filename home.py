
from flask import Flask, flash, request, render_template, redirect,url_for,Response
from flask_mysqldb import MySQL
import urllib.request
import os
from werkzeug.utils import secure_filename
import random
import array

app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'#folder in which images are gonna stored
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# UPLOAD_FOLDER1 = 'static/Documents/'
app.secret_key = "secret key"
# app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1
 
app.config['MYSQL_HOST']="localhost"  
app.config['MYSQL_USER']="root" 
app.config['MYSQL_PASSWORD']="nabin"  
app.config['MYSQL_DB']="se_project"
mysql=MySQL(app)


def password():
    MAX_LEN = 12
    
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
         'Z']

    SYMBOLS = ['@', '#', '$', '%']
    
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
      
    return password

def username(full_name):
    full_name = full_name.lower().split()
    if len(full_name) > 1:
        first_letter = full_name[0][0]
        three_letters_surname = full_name[-1][:3].rjust(3, 'x')
        number = '{:03d}'.format(random.randrange (1,999))
        username = '{}{}{}'.format(first_letter, three_letters_surname, number)
        return username
    else:
        print('Error. Please enter first name and surname')
        # try again...



@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/treg',methods=['GET','POST'])
def treg():
    if request.method=='POST':
        tname = request.form.get("tname")
        tmail = request.form.get("tmail")
        tno = request.form.get("tno")
        tadharno = request.form.get("tadharno")
        tdob = request.form.get("tdob")
        tgender = request.form.get("tgender")
        tabout = request.form.get("tabout")
        topics=request.form.get('topics')
        timg = request.files['timg']
        uname=username(tname)+"T"
        qimg = request.files['qimg']
        passwd=password()
         
        if timg and allowed_file(timg.filename):
            timg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(timg.filename)))
            t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,timg,qimg)
        else:
            img="<FileStorage: '"+uname[0].upper()+".jpg' ('image/jpeg')>"
            t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,img,qimg)

        if qimg and allowed_file(qimg.filename):
            qimg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(qimg.filename)))
            t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,timg,qimg)
        else:
            return "Please Enter Your Qualification image"
        
        cursor=mysql.connection.cursor()
        cursor.execute('''insert into teacher (usernm,passwd,name,email,no,dob,gender,about,adharno,topics,pimg,qimg) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',t)
        cursor.execute('''insert into login values(%s,%s)''',(uname,passwd))
        mysql.connection.commit()
        cursor.close()
        title="Login Details"
        Output="You register successfully Your Username: "+uname+" password: "+passwd 
        return render_template('output.html',t=title,o=Output)
        # return " You register successfully Your Username: "+uname+" password: "+passwd +"<a href='http://127.0.0.1:8000/login'>Login</a>"
        #     # redirect('/login')
        # except:
        #     return"You have entered false values"        
        
      
    #     # t=teacher(sno=sno,tname=tname, tmail=tmail, tno=tno, tdob=tdob, tg=tg, ta=ta, Adno=Adno, passwd=passwd)
    #     # dbt.session.add(t)
    #     # dbt.session.commit()
            
    # return "Teacher registration"
    return render_template("treg.html")
@app.route('/sreg',methods=['GET','POST'])
def sreg():
    if request.method=='POST':
        # try:    
            sname = request.form.get("sname")
            smail = request.form.get("smail")
            sno = request.form.get("sno")
            sadharno = request.form.get("sadharno")
            if len(str(sno))==10 and len(str(sadharno))==12:
                sdob = request.form.get("sdob")
                sgender = request.form.get("sgender")
                simg = request.files['simg']
                uname=username(sname)+"S"
                passwd=password() 
                if simg and allowed_file(simg.filename):
                    simg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(simg.filename)))
                    t=(uname,passwd,sname,smail,sno,sdob,sgender,sadharno,simg)
                else:
                    img="<FileStorage: '"+sname[0].upper()+".jpg' ('image/jpeg')>"
                    t=(uname,passwd,sname,smail,sno,sdob,sgender,sadharno,img)
            
                cursor=mysql.connection.cursor()
                cursor.execute('''insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',t)
                cursor.execute('''insert into login values(%s,%s)''',(uname,passwd))
                mysql.connection.commit()
                cursor.close()
                title="Login Details"
                Output="You register successfully Your Username: "+uname+" password: "+passwd 
                return render_template('output.html',t=title,o=Output)
            else:
                if len(str(sno))!=10:
                    return "Wrong number entered"+"<a href='http://127.0.0.1:8000/sreg'>Go Back</a>" 
                elif len(str(sadharno))!=12:
                    return "Wrong Adhar number entered"+"<a href='http://127.0.0.1:8000/sreg'>Go Back</a>"
    return render_template("sreg.html")


@app.route('/login',methods=['GET','POST'])
def login():
    # return "Login"
    if request.method=='POST':
        user_id = request.form.get("userid")
        passwd = request.form.get("password") 
        cursor=mysql.connection.cursor()
        rv=cursor.execute("select * from login")
        if rv>0:
            ud=cursor.fetchall()
            if (user_id,passwd) in ud:
                if user_id[-1]=='S':
                    s="select pimg from student where usernm=%s and passwd=%s"
                    v=(user_id,passwd)
                    cursor.execute(s,v)
                    d=cursor.fetchall()
                    s1="select name from student where usernm=%s and passwd=%s"
                    cursor.execute(s1,v)
                    d1=cursor.fetchall()
                    # print(len("<FileStorage: '"))
                    # print(len("' ('image/jpeg')>"))

                    # print(d[0][0][15:-17:1])
                    name=d1[0][0]
                    img=d[0][0][15:-17:1]
                    p=os.path.join(app.config['UPLOAD_FOLDER'],img)
                    return render_template("sprofile.html",uimg=p,n=name)

                elif user_id[-1]=='T':
                    s="select pimg,name,qimg,email from teacher where usernm=%s and passwd=%s"
                    v=(user_id,passwd)
                    cursor.execute(s,v)
                    d=cursor.fetchall()
                    # print(len("<FileStorage: '"))
                    # print(len("' ('image/jpeg')>"))

                    # print(d[0][0][15:-17:1])
                    name=d[0][1]
                    email=d[0][3]
                    if d[0][2][-7:-3:1]=='jepg':
                        qimg=d[0][2][15:-16:1]
                    qimg=d[0][2][15:-16:1]
                    if d[0][0][-7:-3:1]=='jepg':
                        img=d[0][0][15:-16:1]
                    img=d[0][0][15:-17:1]
                    if d[0][0]=="<FileStorage: '' ('application/octet-stream')>":
                        img=user_id[0].upper()+".jpg"
                    print(name)
                    print(qimg)
                    print(img)
                    p=os.path.join(app.config['UPLOAD_FOLDER'],img)
                    pa=os.path.join(app.config['UPLOAD_FOLDER'],qimg)
                    return render_template("tprofile.html",uimg=p,quimg=pa,n=name,mail=email)

                else:
                    return redirect(url_for('sreg'))
            else:
                t='Wrong entries!'
                o="Wrong user_id and password"
                return render_template("output.html",o=o,t=t)

        mysql.connection.commit()
    return render_template('login.html')

@app.route('/searchT',methods=['GET','POST'])
def searchT():
    if request.method=='POST':
        topic = request.form.get("topic")
        cursor=mysql.connection.cursor()
        rv=cursor.execute("select name,topics,email from teacher")
        ud=cursor.fetchall()
        l=[]
        if rv>0:
            for i in ud:
                if topic in i[1].split(','):
                    l+=[[i[0],i[2]]]
        
            print(l)        
        mysql.connection.commit()
        if l==[]:
            return render_template('sprofile.html')
        else:
            return render_template('sprofile.html',l=l)




if __name__=="__main__":
    app.run(debug=True, port=8000) 