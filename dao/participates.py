from config.dbconfig import pg_config
import psycopg2


class ParticipatesDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            )

        self.conn = psycopg2._connect(connection_url)

    postsArray = [{"postId": 1, "photoId": '345C6', "postDate": '2/21/2019 12:00:00'},
                  {"postId": 2, "photoId": '265A2', "postDate": '2/14/2018 15:00:00'},
                  {"postId": 3, "photoId": '542B1', "postDate": '2/17/2019 21:00:00'},
                  {"postId": 4, "photoId": '21476', "postDate": '2/23/2019 11:00:00'},
                  {"postId": 5, "photoId": '635W9', "postDate": '5/01/2019 4:00:00'}]

    def getAllPosts(self):
        cursor = self.conn.cursor()
        query = "select * from post;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getUsersInSpecificChat(self, chatid):
        cursor = self.conn.cursor()
        query = "select firstname, lastname, phonenumber, email, birthday, username " \
                "from (participates as PP natural inner join users natural inner join " \
                "person natural inner join chat)" \
                "where PP.chatid=%s;"
        cursor.execute(query, (chatid,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getOwnerInSpecificChat(self, chatid):
        cursor = self.conn.cursor()
        query = "select firstname, lastname, phonenumber, email, birthday, username " \
                "from (participates as PP natural inner join users natural inner join " \
                "person natural inner join chat)" \
                "where PP.role='owner' and PP.chatid=%s;"
        cursor.execute(query, (chatid,))
        result = cursor.fetchone()
        return result