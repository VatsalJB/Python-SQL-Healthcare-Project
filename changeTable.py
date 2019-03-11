def insertRecord(cur,data,table):
    insertCommand = "insert into {} values {}".format(table,data)
    cur.execute(insertCommand)

def checkPass(cur,SID,pas):
    command = "select Password from Login where Subscriber_ID = '{}'".format(SID)
    cur.execute(command)
    correctPass = cur.fetchall();

    if pas == correctPass[0][0]:            #Fetched as a list of tuples
        return True
    else:
        return False

def forgotPass(cur,SID):
    command = "select Sec_Q,Sec_A from Login where Subscriber_ID = '{}'".format(SID)
    cur.execute(command)

    data = cur.fetchall()
    #print(data[0][0])
    print("Security Question : \n{}".format(data[0][0]))
    secA = input('Answer : ')

    if data[0][1] == secA:
        newPass=input('Enter new password : ')
        command = "update Login set Password = {} where Subscriber_ID = '{}'".format(newPass,SID)
        cur.execute(command)
        print('Password Updated')

        return True
    else:
        print("Incorrect Answer! Try Again")
        return False


def duplicateID(cur,SID):
    command = "select Subscriber_ID from Login where Subscriber_ID = '{}'".format(SID)
    cur.execute(command)
    tempID = cur.fetchall()

    if len(tempID)==0:
        return False
    else:
        return True

def readTable(cur,table):
    command = "select * from {}".format(table)
    cur.execute(command)
    data = cur.fetchall()

    for i in data:
        print(i)

