import sqlite3

def createConnection(db_file):      ##Call createConnection(path) from main
    """Create a databse connection to SQLite database."""
    try:
        return sqlite3.connect(db_file)
    except Error as e:
        print("Unable to connect to sql")
        return False


def createTable(cur,command):
    try:
        cur.execute(command)
        return True
    except Error as e:
        print("Unable to create table")
        return False
