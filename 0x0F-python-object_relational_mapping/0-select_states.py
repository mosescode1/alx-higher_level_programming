#!/usr/bin/python3
"""my module on MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    print(type(database))

    db = MySQLdb.connect(host='localhost', user=user,
                         password=password, port=3306, database=database)

    cur = db.cursor()
    query = """SELECT * FROM states ORDER BY id ASC"""
    cur.execute(query)
    result = cur.fetchall()
    for res in result:
        print(res)

    cur.close()
    db.close()
