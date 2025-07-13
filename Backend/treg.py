import mysql.connector as msc
mycon=msc.connect(host="localhost",user="root",passwd="nabin",database="dummy")
cur=mycon.cursor()
paswd="Nasodium11@23*20@58"
# try:
tid=1
name=input("Enter your name: ")
dob=input("Enter your DOB(YYYY/MM/DD): ")
pno=int(input("Enter your Mobile No.: "))
email=input("Enter your E-mail: ")
un=input("Enter your Profile name: ")
topics=input("Enter the topics you want to teach: ")
qual=input("Enter your qualification: ")
idproof=input("Enter your idproof name: ")
descb=input("Tell about yourself ")
s1="insert into teacher (tid,name,dob,pno,email,un,topics,qual,idproof,descb) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(tid,name,dob,pno,email,un,topics,qual,idproof,descb)
cur.execute(s1,val)
mycon.commit()
print("Data entered successfully")
# except:
#     print("Entered False value!")
