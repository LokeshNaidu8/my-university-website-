import pymysql as p


def getconnection():
    return p.connect(host="localhost", user="root", password="", database="university")


def adddata(t):
    con = getconnection()
    cur = con.cursor()
    query1 = "insert into contact(name,email,subject,message)values(%s,%s,%s,%s)"
    cur.execute(query1, t)
    con.commit()
    con.close()

# for validate user login


def fetchuserpwd():
    con = getconnection()
    cur = con.cursor()
    query = "select name,password from login"
    cur.execute(query)
    f = cur.fetchall()
    con.commit()
    con.close()
    return f


def deleteUser(id):
    con = getconnection()
    cur = con.cursor()
    query = f"delete from contact where id={id}"
    cur.execute(query)
    f = cur.fetchall()
    con.commit()
    con.close()
    return f


def fetchdata():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from contact")
    datalist = cur.fetchall()
    con.commit()
    con.close()
    return datalist


def specificdata(id):
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from contact where id=%s", (id,))
    datalist = cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]


def deletedata(id):
    con = getconnection()
    cur = con.cursor()
    query3 = "delete from contact where id=%s"
    cur.execute(query3, (id,))
    con.commit()
    con.close()
