import mysql.connector

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()


    def ConnectDB(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="yusuf6451895"
        )
        self.cursor = self.db.cursor()
    
    def CreateDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS sinf")
        self.cursor.execute("USE sinf")
    
    def CreateTB(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS talabalar(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name TEXT,
                            second TEXT,
                            age INT)""")
        
    def InsertTB(self, ism, familiya, yosh):
        self.cursor.execute(f'INSERT INTO talabalar(name, second, age) VALUES("{ism}","{familiya}",{yosh})')
        self.db.commit()
    
    def FirstQuery(self):
        self.cursor.execute(f"SELECT * FROM talabalar")
        return self.cursor.fetchall()