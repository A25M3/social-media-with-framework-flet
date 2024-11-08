import sqlite3
import bcrypt

class Database:

    # connexion
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    # create tables  
    def addTableUser(self, t_name):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS user(
                                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                username TEXT,
                                                email TEXT,
                                                password TEXT,
                                                profile_picture TEXT
                                            )
                            """
                            )
        self.conn.commit()
    
    def addTablePost(self, t_name):
        self.cursor.execute("""
                                CREATE TABLE IF NOT EXISTS post(
                                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    desc TEXT,
                                                    userId INTEGER,
                                                    postImage TEXT
                                                )
                            """
        )
    

    # user management
    def create_user(self, username, email, password, profilePicture):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.cursor.execute(
            """
            INSERT INTO user (username, email, password, profile_picture)
            VALUES (?, ?, ?, ?)
            """,
            (username, email, hashed_password, profilePicture)
        )

        self.conn.commit()

    def deleteAllUsers(self):
        self.cursor.execute("DELETE FROM user")
        self.conn.commit()
    
    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM user")
        return self.cursor.fetchall()

    def login(self, username, password):
        self.cursor.execute(
                                """
                                SELECT * FROM user
                                WHERE username = ?
                                """,
                                (username,)
                            )
        
        user = self.cursor.fetchone()
        
        if user :
            stored_hashed_pwd = user[3]

            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_pwd):
                return True
            else:
                return False
        else:
            return False
    

    # post
    def addPost(self, desc, userId, postImage):
        self.cursor.execute("""
                            INSERT INTO post (desc, userId, postImage) 
                            VALUES (?,?,?)
                            """,
                            (desc, userId, postImage)
        )

        self.conn.commit()

    def getAllPosts(self):
        self.cursor.execute("""
            SELECT * FROM post
        """)

        posts = self.cursor.fetchall()

        self.conn.commit()

        return posts
    
    def deleteAllPosts(self):
        self.cursor.execute("""
            DELETE FROM post
        """)

        self.conn.commit()