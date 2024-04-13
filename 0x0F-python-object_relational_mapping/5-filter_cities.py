#!/usr/bin/python3
"""my module on MySQLdb"""
import MySQLdb
import sys
if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    args = sys.argv
    user = args[1]
    password = args[2]
    database = args[3]
    user_arg = args[4]

    db = MySQLdb.connect(host='localhost', user=user,
                         password=password, port=3306, database=database)

    cur = db.cursor()
    try:
        query = """SELECT * FROM cities
            WHERE name LIKE %s"""
        cur.execute(query, (user_arg,))
        result = cur.fetchall()
        for res in result:
            print(res)
    except MySQLdb.Error:
        pass

    cur.close()
    db.close()
