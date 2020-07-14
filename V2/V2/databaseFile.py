import mysql.connector
#sql = "Create TABLE userInfo(id INT AUTO_INCREMENT PRIMARY KEY, FirstName VARCHAR(255) NOT NULL, LastName VARCHAR(255) NOT NULL,birth_date VARCHAR(50), Gender VARCHAR(20), user_name VARCHAR(20), password VARCHAR(25));"
#mc.execute(sql)
#mydb.commit()

def insert1(fname,lname,bd,gen,username,password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123123123",
        database="diseaseprediction"
    )
    mc = mydb.cursor()
    sql = "insert into userInfo(FirstName,LastName,birth_date,Gender,user_name,password) values('"
    sql = sql + fname + "','" + lname + "','" + bd + "','" + gen + "','" + username + "',DES_ENCRYPT('" + password + "','" + username + "'));"
    mc.execute(sql)
    mydb.commit()
    return fname,"Successfull"

def logs(user):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="diseaseprediction"
    )
    mycursor = mydb.cursor()
    sql = "select DES_DECRYPT(password,user_name) from userinfo where user_name='"+user+"';"
    mycursor.execute(sql)
    for x in mycursor:
        #print(x)
        tet = x[0]
    #print(tet)
    return tet

def check_user_name(user):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="diseaseprediction"
    )
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(*) FROM `userinfo` WHERE user_name = '"+user+"';"
    mycursor.execute(sql)
    for x in mycursor:
        count = x[0]

    return count