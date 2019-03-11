import changeTable

def enroll(cur,SID):
    print("\nEnter details : \n")
    MID = input("Member ID : ")
    MCD = input("Member Code : ")
    Name = input("Name : ")
    DOB = input("DOB (dd-mm-yy) : ")
    ZIP = int(input("ZIP : "))

    command = "select Provider_ID from Provider where ZIP_CD = {}".format(ZIP)
    cur.execute(command)
    data = cur.fetchall()

    if len(data)!=0:
        print("Select from the list of providers available in your area :\n")
        num = 1
        for i in data :
            print("{}. {}".format(num, i))
            num+=1

        print()
        inp = int(input())

        #print(data)
        PID = data[inp-1][0]

        data = (MID,MCD,Name,DOB,ZIP,SID,PID)
        #print(data)
        changeTable.insertRecord(cur,data,"Member")

        print("Member enrolled successfully!")
    else:
        print("No provider in your area!")


def update(cur,SID):
    MID = input("\nEnter member ID : ")
    command = "select * from Member where Member_ID = '{}'".format(MID)
    cur.execute(command)
    data = cur.fetchall()

    print("The detailslows : are as fol \n")

    for i in data:
        print(i)

    field = input("Enter the field to be updated : ")
    value = input("Enter the new value : ")

    if field!='ZIP_CD':
        command = "update Member set {} = '{}' where Member_ID = '{}'".format(field,value,MID)
        cur.execute(command)
    else:
        #command = "update Member set ZIP_CD = {} where Member_ID = '{}'".format(value, MID)

        command = "select Provider_ID from Provider where ZIP_CD = {}".format(value)
        cur.execute(command)
        data = cur.fetchall()

        if len(data) != 0:
            print("Select from the list of providers available in your area :\n")
            num = 1
            for i in data:
                print("{}. {}".format(num, i))
                num += 1

            print()
            inp = int(input())

            # print(data)
            PID = data[inp - 1][0]

            command = "update Member set ZIP_CD = {} where Member_ID = '{}'".format(value, MID)
            cur.execute(command)
            command = "update Member set PID = '{}' where Member_ID = '{}'".format(PID, MID)
            cur.execute(command)
        else:
            print("Invalid ZIP")

    print("Details updated successfully")


def delete(cur,SID):
    MID = input("\nEnter the member ID to be deleted : ")

    command = "delete from Member where Member_ID = '{}'".format(MID)
    cur.execute(command)

    print("Delete successful")

def enquire(cur,SID):
    MID = input("Enter member ID : ")

    command = "select * from Member where Member_ID = '{}'".format(MID)
    cur.execute(command)
    memb = cur.fetchall()
#    print(memb)
    if len(memb)!=0:
        depID = memb[0][1]
        PID = memb[0][6]

        command = "select * from Member where Member_CD = '{}' and Member_ID != '{}'".format(depID,MID)
        cur.execute(command)
        dependents = cur.fetchall()

        print("Member details : \n{}".format(memb))
        print("\nDependents : \n")

        for i in dependents:
            print(i)

        command = "select * from Provider where Provider_ID = '{}'".format(PID)
        cur.execute(command)
        provider = cur.fetchall()

        print("\nProvider details :\n")

        for i in provider:
            print(i)
    else:
        print("Invalid Member_ID")