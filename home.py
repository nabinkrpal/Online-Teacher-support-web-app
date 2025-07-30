
# from flask import Flask, flash, request, render_template, redirect,url_for,Response
# from flask_mysqldb import MySQL
# import urllib.request
# import os
# from werkzeug.utils import secure_filename
# import random
# import array

# app=Flask(__name__)

# UPLOAD_FOLDER = 'static/uploads/'#folder in which images are gonna stored
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # UPLOAD_FOLDER1 = 'static/Documents/'
# app.secret_key = "secret key"
# # app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1
 
# app.config['MYSQL_HOST']="localhost"  
# app.config['MYSQL_USER']="root" 
# app.config['MYSQL_PASSWORD']="nabin"  
# app.config['MYSQL_DB']="se_project"
# mysql=MySQL(app)


# def password():
#     MAX_LEN = 12
    
#     DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
#     LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#          'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#          'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#          'z']

#     UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#          'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
#          'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#          'Z']

#     SYMBOLS = ['@', '#', '$', '%']
    
#     COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

#     rand_digit = random.choice(DIGITS)
#     rand_upper = random.choice(UPCASE_CHARACTERS)
#     rand_lower = random.choice(LOCASE_CHARACTERS)
#     rand_symbol = random.choice(SYMBOLS)
#     temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    
#     for x in range(MAX_LEN - 4):
#         temp_pass = temp_pass + random.choice(COMBINED_LIST)

#     temp_pass_list = array.array('u', temp_pass)
#     random.shuffle(temp_pass_list)

#     password = ""
#     for x in temp_pass_list:
#         password = password + x
      
#     return password

# def username(full_name):
#     full_name = full_name.lower().split()
#     if len(full_name) > 1:
#         first_letter = full_name[0][0]
#         three_letters_surname = full_name[-1][:3].rjust(3, 'x')
#         number = '{:03d}'.format(random.randrange (1,999))
#         username = '{}{}{}'.format(first_letter, three_letters_surname, number)
#         return username
#     else:
#         print('Error. Please enter first name and surname')
#         # try again...



# @app.route('/')
# def homepage():
#     return render_template('home.html')

# @app.route('/treg',methods=['GET','POST'])
# def treg():
#     if request.method=='POST':
#         tname = request.form.get("tname")
#         tmail = request.form.get("tmail")
#         tno = request.form.get("tno")
#         tadharno = request.form.get("tadharno")
#         tdob = request.form.get("tdob")
#         tgender = request.form.get("tgender")
#         tabout = request.form.get("tabout")
#         topics=request.form.get('topics')
#         timg = request.files['timg']
#         uname=username(tname)+"T"
#         qimg = request.files['qimg']
#         passwd=password()
         
#         if timg and allowed_file(timg.filename):
#             timg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(timg.filename)))
#             t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,timg,qimg)
#         else:
#             img="<FileStorage: '"+uname[0].upper()+".jpg' ('image/jpeg')>"
#             t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,img,qimg)

#         if qimg and allowed_file(qimg.filename):
#             qimg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(qimg.filename)))
#             t=(uname,passwd,tname,tmail,tno,tdob,tgender,tabout,tadharno,topics,timg,qimg)
#         else:
#             return "Please Enter Your Qualification image"
        
#         cursor=mysql.connection.cursor()
#         cursor.execute('''insert into teacher (usernm,passwd,name,email,no,dob,gender,about,adharno,topics,pimg,qimg) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',t)
#         cursor.execute('''insert into login values(%s,%s)''',(uname,passwd))
#         mysql.connection.commit()
#         cursor.close()
#         title="Login Details"
#         Output="You register successfully Your Username: "+uname+" password: "+passwd 
#         return render_template('output.html',t=title,o=Output)
#         # return " You register successfully Your Username: "+uname+" password: "+passwd +"<a href='http://127.0.0.1:8000/login'>Login</a>"
#         #     # redirect('/login')
#         # except:
#         #     return"You have entered false values"        
        
      
#     #     # t=teacher(sno=sno,tname=tname, tmail=tmail, tno=tno, tdob=tdob, tg=tg, ta=ta, Adno=Adno, passwd=passwd)
#     #     # dbt.session.add(t)
#     #     # dbt.session.commit()
            
#     # return "Teacher registration"
#     return render_template("treg.html")
# @app.route('/sreg',methods=['GET','POST'])
# def sreg():
#     if request.method=='POST':
#         # try:    
#             sname = request.form.get("sname")
#             smail = request.form.get("smail")
#             sno = request.form.get("sno")
#             sadharno = request.form.get("sadharno")
#             if len(str(sno))==10 and len(str(sadharno))==12:
#                 sdob = request.form.get("sdob")
#                 sgender = request.form.get("sgender")
#                 simg = request.files['simg']
#                 uname=username(sname)+"S"
#                 passwd=password() 
#                 if simg and allowed_file(simg.filename):
#                     simg.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(simg.filename)))
#                     t=(uname,passwd,sname,smail,sno,sdob,sgender,sadharno,simg)
#                 else:
#                     img="<FileStorage: '"+sname[0].upper()+".jpg' ('image/jpeg')>"
#                     t=(uname,passwd,sname,smail,sno,sdob,sgender,sadharno,img)
            
#                 cursor=mysql.connection.cursor()
#                 cursor.execute('''insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)''',t)
#                 cursor.execute('''insert into login values(%s,%s)''',(uname,passwd))
#                 mysql.connection.commit()
#                 cursor.close()
#                 title="Login Details"
#                 Output="You register successfully Your Username: "+uname+" password: "+passwd 
#                 return render_template('output.html',t=title,o=Output)
#             else:
#                 if len(str(sno))!=10:
#                     return "Wrong number entered"+"<a href='http://127.0.0.1:8000/sreg'>Go Back</a>" 
#                 elif len(str(sadharno))!=12:
#                     return "Wrong Adhar number entered"+"<a href='http://127.0.0.1:8000/sreg'>Go Back</a>"
#     return render_template("sreg.html")


# @app.route('/login',methods=['GET','POST'])
# def login():
#     # return "Login"
#     if request.method=='POST':
#         user_id = request.form.get("userid")
#         passwd = request.form.get("password") 
#         cursor=mysql.connection.cursor()
#         rv=cursor.execute("select * from login")
#         if rv>0:
#             ud=cursor.fetchall()
#             if (user_id,passwd) in ud:
#                 if user_id[-1]=='S':
#                     s="select pimg from student where usernm=%s and passwd=%s"
#                     v=(user_id,passwd)
#                     cursor.execute(s,v)
#                     d=cursor.fetchall()
#                     s1="select name from student where usernm=%s and passwd=%s"
#                     cursor.execute(s1,v)
#                     d1=cursor.fetchall()
#                     # print(len("<FileStorage: '"))
#                     # print(len("' ('image/jpeg')>"))

#                     # print(d[0][0][15:-17:1])
#                     name=d1[0][0]
#                     img=d[0][0][15:-17:1]
#                     p=os.path.join(app.config['UPLOAD_FOLDER'],img)
#                     return render_template("sprofile.html",uimg=p,n=name)

#                 elif user_id[-1]=='T':
#                     s="select pimg,name,qimg,email from teacher where usernm=%s and passwd=%s"
#                     v=(user_id,passwd)
#                     cursor.execute(s,v)
#                     d=cursor.fetchall()
#                     # print(len("<FileStorage: '"))
#                     # print(len("' ('image/jpeg')>"))

#                     # print(d[0][0][15:-17:1])
#                     name=d[0][1]
#                     email=d[0][3]
#                     if d[0][2][-7:-3:1]=='jepg':
#                         qimg=d[0][2][15:-16:1]
#                     qimg=d[0][2][15:-16:1]
#                     if d[0][0][-7:-3:1]=='jepg':
#                         img=d[0][0][15:-16:1]
#                     img=d[0][0][15:-17:1]
#                     if d[0][0]=="<FileStorage: '' ('application/octet-stream')>":
#                         img=user_id[0].upper()+".jpg"
#                     print(name)
#                     print(qimg)
#                     print(img)
#                     p=os.path.join(app.config['UPLOAD_FOLDER'],img)
#                     pa=os.path.join(app.config['UPLOAD_FOLDER'],qimg)
#                     return render_template("tprofile.html",uimg=p,quimg=pa,n=name,mail=email)

#                 else:
#                     return redirect(url_for('sreg'))
#             else:
#                 t='Wrong entries!'
#                 o="Wrong user_id and password"
#                 return render_template("output.html",o=o,t=t)

#         mysql.connection.commit()
#     return render_template('login.html')

# @app.route('/searchT',methods=['GET','POST'])
# def searchT():
#     if request.method=='POST':
#         topic = request.form.get("topic")
#         cursor=mysql.connection.cursor()
#         rv=cursor.execute("select name,topics,email from teacher")
#         ud=cursor.fetchall()
#         l=[]
#         if rv>0:
#             for i in ud:
#                 if topic in i[1].split(','):
#                     l+=[[i[0],i[2]]]
        
#             print(l)        
#         mysql.connection.commit()
#         if l==[]:
#             return render_template('sprofile.html')
#         else:
#             return render_template('sprofile.html',l=l)

# @app.route('/feedback', methods=['POST'])
# def feedback():
#     name = request.form.get("name")
#     source = request.form.get("source")
#     message = request.form.get("message")

#     if name and source and message:
#         cursor = mysql.connection.cursor()
#         cursor.execute("INSERT INTO feedback (name, source, message) VALUES (%s, %s, %s)", (name, source, message))
#         mysql.connection.commit()
#         cursor.close()

#         title = "Feedback Received"
#         output = f"Thank you {name}! We appreciate your feedback."
#         return render_template("output.html", t=title, o=output)
#     else:
#         title = "Submission Failed"
#         output = "Please fill in all the fields correctly."
#         return render_template("output.html", t=title, o=output)





# if __name__=="__main__":
#     # app.run(debug=True, port=8000) 
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, flash, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import os
import random
import array
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.secret_key = "secret key"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "nabin"
app.config['MYSQL_DB'] = "teacher_connect"
mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def password():
    MAX_LEN = 12
    DIGITS = [str(i) for i in range(10)]
    LOCASE_CHARACTERS = list('abcdefghijkmnopqrstuvwxyz')
    UPCASE_CHARACTERS = list('ABCDEFGHJKLMNPQRSTUVWXYZ')
    SYMBOLS = ['@', '#', '$', '%']
    COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

    temp_pass = random.choice(DIGITS) + random.choice(UPCASE_CHARACTERS) + random.choice(LOCASE_CHARACTERS) + random.choice(SYMBOLS)

    for _ in range(MAX_LEN - 4):
        temp_pass += random.choice(COMBINED_LIST)

    temp_pass_list = list(temp_pass)
    random.shuffle(temp_pass_list)
    return ''.join(temp_pass_list)

def username(full_name):
    full_name = full_name.lower().split()
    if len(full_name) > 1:
        first_letter = full_name[0][0]
        three_letters_surname = full_name[-1][:3].rjust(3, 'x')
        number = '{:03d}'.format(random.randrange(1, 999))
        return f'{first_letter}{three_letters_surname}{number}'
    else:
        return None

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/treg', methods=['GET', 'POST'])
def treg():
    if request.method == 'POST':
        tname = request.form.get("tname")
        tmail = request.form.get("tmail")
        tno = request.form.get("tno")
        tadharno = request.form.get("tadharno")
        tdob = request.form.get("tdob")
        tgender = request.form.get("tgender")
        tabout = request.form.get("tabout")
        topics = request.form.get("topics")
        timg = request.files.get('timg')
        qimg = request.files.get('qimg')

        uname = username(tname)
        if not uname:
            return "Error. Please enter First and Last name."
        uname += "T"
        passwd = password()

        timg_filename = secure_filename(timg.filename) if timg and allowed_file(timg.filename) else uname[0].upper() + ".jpg"
        timg_path = os.path.join(app.config['UPLOAD_FOLDER'], timg_filename)
        if timg and allowed_file(timg.filename):
            timg.save(timg_path)

        if not (qimg and allowed_file(qimg.filename)):
            return "Please Enter Your Qualification image"
        qimg_filename = secure_filename(qimg.filename)
        qimg_path = os.path.join(app.config['UPLOAD_FOLDER'], qimg_filename)
        qimg.save(qimg_path)

        data = (uname, passwd, tname, tmail, tno, tdob, tgender, tabout, tadharno, topics, timg_path, qimg_path)

        cursor = mysql.connection.cursor()
        cursor.execute('''INSERT INTO teacher 
            (usernm, passwd, name, email, no, dob, gender, about, adharno, topics, pimg, qimg) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', data)
        cursor.execute('INSERT INTO login VALUES (%s, %s)', (uname, passwd))
        mysql.connection.commit()
        cursor.close()

        return render_template('output.html', t="Login Details", o=f"You registered successfully. Username: {uname}, Password: {passwd}")
    
    return render_template("treg.html")

@app.route('/sreg', methods=['GET', 'POST'])
def sreg():
    if request.method == 'POST':
        sname = request.form.get("sname")
        smail = request.form.get("smail")
        sno = request.form.get("sno")
        sadharno = request.form.get("sadharno")

        if len(str(sno)) != 10:
            return "Wrong number entered. <a href='/sreg'>Go Back</a>"
        if len(str(sadharno)) != 12:
            return "Wrong Aadhar number entered. <a href='/sreg'>Go Back</a>"

        sdob = request.form.get("sdob")
        sgender = request.form.get("sgender")
        simg = request.files.get('simg')

        uname = username(sname)
        if not uname:
            return "Error. Please enter First and Last name."
        uname += "S"
        passwd = password()

        simg_filename = secure_filename(simg.filename) if simg and allowed_file(simg.filename) else sname[0].upper() + ".jpg"
        simg_path = os.path.join(app.config['UPLOAD_FOLDER'], simg_filename)
        if simg and allowed_file(simg.filename):
            simg.save(simg_path)

        data = (uname, passwd, sname, smail, sno, sdob, sgender, sadharno, simg_path)

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', data)
        cursor.execute('INSERT INTO login VALUES (%s,%s)', (uname, passwd))
        mysql.connection.commit()
        cursor.close()

        return render_template('output.html', t="Login Details", o=f"You registered successfully. Username: {uname}, Password: {passwd}")
    
    return render_template("sreg.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get("userid")
        passwd = request.form.get("password")
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM login")
        ud = cursor.fetchall()

        if (user_id, passwd) in ud:
            if user_id.endswith('S'):
                cursor.execute("SELECT pimg, name FROM student WHERE usernm=%s AND passwd=%s", (user_id, passwd))
                result = cursor.fetchone()
                pimg_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(result[0]))
                return render_template("sprofile.html", uimg=pimg_path, n=result[1])
            elif user_id.endswith('T'):
                cursor.execute("SELECT pimg, name, qimg, email FROM teacher WHERE usernm=%s AND passwd=%s", (user_id, passwd))
                result = cursor.fetchone()
                pimg_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(result[0]))
                qimg_path = os.path.join(app.config['UPLOAD_FOLDER'], os.path.basename(result[2]))
                return render_template("tprofile.html", uimg=pimg_path, quimg=qimg_path, n=result[1], mail=result[3])
        else:
            return render_template("output.html", t='Wrong entries!', o="Wrong user ID or password")

    return render_template('login.html')



# @app.route('/searchT', methods=['GET', 'POST'])
# def searchT():
#     if request.method == 'POST':
#         topic = request.form.get("topic", "").strip().lower()
#         cursor = mysql.connection.cursor()
#         cursor.execute("SELECT name, topics, email FROM teacher")
#         teachers = cursor.fetchall()
#         exact_matches = []
#         similar_matches = []
#         for name, topics, email in teachers:
#             topic_list = [t.strip().lower() for t in topics.split(',')]
#             # Exact match (case-insensitive, by whole topic)
#             if topic in topic_list:
#                 exact_matches.append([name, email])
#             # Similar (partial/substring) match
#             elif any(topic in t for t in topic_list):
#                 similar_matches.append([name, email])

#         # Always pass profile info if you have it (e.g., user image/name from session or previous query)
#         return render_template(
#             'sprofile.html',
#             exact=exact_matches if exact_matches else None,
#             similar=similar_matches if similar_matches else None,
#             # Add other context: e.g. profile_image=current_user_img,
#             # name=current_user_name, etc.
#         )

#     return redirect(url_for('homepage'))

@app.route('/searchT', methods=['GET', 'POST'])
def searchT():
    if request.method == 'POST':
        topic = request.form.get("topic", "").strip().lower()
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT name, topics, email FROM teacher")
        teachers = cursor.fetchall()
        exact_matches = []
        similar_matches = []
        for name, topics, email in teachers:
            topic_list = [t.strip().lower() for t in topics.split(',')]
            # Exact match
            if topic in topic_list:
                exact_matches.append([name, email])
            # Partial/substring similar match (avoiding repeat)
            elif any(topic in t and topic != '' for t in topic_list):
                similar_matches.append([name, email])

        return render_template(
            'sprofile.html',
            exact=exact_matches if exact_matches else None,
            similar=similar_matches if similar_matches else None,
            # Pass uimg and n if you want to keep showing student profile info
            #uimg=session.get('uimg'),  # or however you handle user images
            #n=session.get('n'),        # or the student's name
        )
    return redirect(url_for('homepage'))


@app.route('/feedback', methods=['POST'])
def feedback():
    name = request.form.get("name")
    source = request.form.get("source")
    message = request.form.get("message")

    if name and source and message:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO feedback (name, source, message) VALUES (%s, %s, %s)", (name, source, message))
        mysql.connection.commit()
        cursor.close()
        return render_template("output.html", t="Feedback Received", o=f"Thank you {name}! We appreciate your feedback.")
    else:
        return render_template("output.html", t="Submission Failed", o="Please fill in all the fields correctly.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)
