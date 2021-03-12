import sqlite3
import time
import math


class DBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def addUser(self, name, email, hpsw):
        try:
            self.__cur.execute(f"SELECT COUNT() as 'count' FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Email already exist")
                return False
            tm = math.floor(time.time())
            self.__cur.execute('INSERT INTO users VALUES(NULL, ?, ?, ?, ?)', (name, email, hpsw, tm))
            self.__db.comit()
        except sqlite3.Error as e:
            print("Error inserting user" + str(e))
            return False
        return True


    def getUser(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone
