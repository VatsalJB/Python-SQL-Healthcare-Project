import changeTable

def login(cur):
    print("Enter login credentials.\n")
    SID = input("Subscriber ID : ")
    pas = input("Password : ")

    if changeTable.checkPass(cur,SID,pas) == False:
            print("Incorrect Password!")
            inp = input("Forgot Password? (y/n) : ")

            if inp == 'y':
               if changeTable.forgotPass(cur,SID) == True:
                   return SID
               else:
                   return False
            else:
                return False

    return SID


def newMember(cur):
    SID = input("Enter new Subscriber ID : ")

    if changeTable.duplicateID(cur,SID) == True:
        print("Duplicate ID. Try Again!")
        return False
    else:
        print('Enter the details for new Subscriber : ')
        pas = input('Password : ')
        sec_Q = input('Security Question : ')
        sec_A = input('Secirity Answer : ')
        data = (SID,pas,sec_Q,sec_A)
        changeTable.insertRecord(cur,data,"Login")

    return SID
