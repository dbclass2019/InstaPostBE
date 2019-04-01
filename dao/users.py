from config import dbconfig
import psycopg2

class UsersDAO:

    userArray = [{"userId": 1, "userName": 'Homero123', "password": 'dotdashdot'},
                 {"userId": 2, "userName": 'Salchicha2', "password": 'bootwoot9'}]

    def _init_(self):

        connectionURL="dbname=%s user=%s password=%s" % (dbconfig['dbname'],
                                                         dbconfig['user'],
                                                         dbconfig['passwd'])

        self.conn = psycopg2._connect(connectionURL)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select userId, username from Users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByID(self, uid):
        cursor = self.conn.cursor()
        query = "select userId, username, personId, firstName, lastName, phoneNumber, email, birthday from Users natural inner join Person where userid = %s;"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        return result

    def getUserByUName(self, uname):
        cursor = self.conn.cursor()
        query = "select * from (select userId, username, personId, firstName, lastName, phoneNumber, email, birthday" \
                "from Users natural inner join Person where Person.userid = Users.userid) as foo where foo.userName = %s;"
        cursor.execute(query, (uname,))
        result = cursor.fetchone()
        return result

    def getMostActiveUser(self):
        return self.userArray[0]

    def insert(self, username, password):
        cursor = self.conn.cursor()
        query = "insert into Users(username, password) values (%s, %s) returning userId;"
        cursor.execute(query, (username, password,))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def update(self, userId, username, password):
        cursor = self.conn.cursor()
        query = "update Users set username = %s, password = %s where userId = %s;"
        cursor.execute(query, (username, password, userId,))
        self.conn.commit()
        return userId

    def delete(self, uid):
        cursor = self.conn.cursor()
        query = "delete from Users where userId = %s;"
        cursor.execute(query, (uid,))
        self.conn.commit()
        return uid

