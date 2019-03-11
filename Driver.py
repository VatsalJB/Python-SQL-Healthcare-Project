import Create
import Login
import changeTable
import Member

def main():

    conn = Create.createConnection("C:\\Users\LAB\Desktop\Project1\healthcare.db")
    if conn == False:
        return

    cur = conn.cursor()
    if cur == False:
        return

    cur.execute("PRAGMA foreign_keys = ON")  ##To turn on foreign keys

    flag = Create.createTable(cur,"""create table if not exists Login(
            Subscriber_ID varchar Primary Key,
            Password varchar,
            Sec_Q varchar,
            Sec_A varchar)
            """)
    if flag == False:
        return

    flag = Create.createTable(cur,"""create table if not exists Member(
            Member_ID varchar Primary Key,
            Member_CD varchar,
            Name varchar,
            DOB date,
            ZIP_CD int,
            SID varchar,
            PID varchar,
            Foreign Key (SID) references Login(Subscriber_ID),
            Foreign Key (PID) references Provider(Provider_ID)
            )
            """)

    if flag == False:
        return


    flag = Create.createTable(cur,"""create table if not exists Provider(
            Provider_ID varchar Primary Key,
            Provider_Name varchar,
            ZIP_CD int
            )
            """)
    if flag == False:
        return


# ############# Add records to Provider ################
#     data1 = ('P345',"ABC", 1007)
#     data2 = ('P897',"DEF", 1008)
#     data3 = ('P762', "GHI", 1008)
#     data4 = ('P845', "ZXC", 1009)
#
#     changeTable.insertRecord(cur,data1,"Provider")
#     changeTable.insertRecord(cur, data2, "Provider")
#     changeTable.insertRecord(cur, data3, "Provider")
#     changeTable.insertRecord(cur, data4, "Provider")
########################################################

    command = "select * from Member"
    cur.execute(command)
    data = cur.fetchall()

    for i in data:
        print(i)
#######################Input From User##########################


    inp = int(input("1.Login\n2.Sign Up\n"))

    if inp==1:
        SID = Login.login(cur)
    else:
        SID = Login.newMember(cur)

    if SID == False:
        return

    print("\nSelect an option : \n")
    option = int(input("1.Member Enroll\n2.Member Update\n3.Member Delete\n4.Member Enquiry\n"))

    if option==1:
        Member.enroll(cur,SID)
    elif option==2:
        Member.update(cur,SID)
    elif option==3:
        Member.delete(cur,SID)
    else:
        Member.enquire(cur,SID)

    #changeTable.readTable(cur,"Login")

    conn.commit()

    print()
    command = "select * from Member"
    cur.execute(command)
    data = cur.fetchall()

    for i in data:
        print(i)

if __name__ == '__main__':
    main()


