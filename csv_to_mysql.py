import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="https://127.0. 0.1",
  user="root",
  password="root",
  database="databasename"
)
mycursor = mydb.cursor()

df = pd.read_csv("database.csv")
header=df.columns.to_list()
collen =len(df.index)
table_name=input() or "students"


def createtable():
    heading=[]
    rows=[]
    normalhead=[]
    for q in header:
        normalhead.append(q)
    for x in header:
        x=x+" VARCHAR(20)"
        heading.append(x)
    heading.pop()
    mainhead=",".join(heading)
    normalhead.pop()
    normalhead=",".join(normalhead)
    mycursor.execute("CREATE TABLE "+table_name+" ("+mainhead+",att VARCHAR(20))")
    for iq in range(collen):
        x=df.loc[iq,:].values.tolist()
        for i in range(len(x)):
            rows.append(str(x[i]))
        sql = "INSERT INTO "+table_name+" ("+normalhead+",att) VALUES ("+(len(header)-1)*"%s,"+"%s)"
        val = rows        
        mycursor.execute(sql, val)
        mydb.commit()
        rows.clear()

def deletetable():
    mycursor.execute("DROP TABLE "+table_name+"")
    print("TABLE DELETED")

def describetable():
    mycursor.execute("DESC "+table_name+"")
    myresult = mycursor.fetchall()
    print(myresult)

def viewtable():
    mycursor.execute("SELECT * FROM "+table_name+"")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

try:
    deletetable()
except:
    pass
createtable()
describetable()
viewtable()

