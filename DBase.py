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
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error inserting user" + str(e))
            return False
        return True


    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False


    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print('No users with simular email')
                return False
            return res
        except sqlite3.Error as e:
            print('Sql error' + str(e))
        return False


    def getUserList(self):
            try:
                self.__cur.execute(f"SELECT id, name, email, time FROM users ORDER BY time DESC LIMIT 5")
                res = self.__cur.fetchall()
                if res: return res
            except sqlite3.Error as e:
                print("Ошибка получения статьи из БД " + str(e))

            return []