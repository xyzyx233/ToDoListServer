import sqlite3

class dao:
    __conn=sqlite3.connect('todo_list.db')
    def checkoradduser(self,username):
        conn=sqlite3.connect('todo_list.db')
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS '''+username+'''
                (NAME TEXT,
                AGE INT,
                SALARY REAL);
                '''
            # 主要就是上面的语句
            conn.execute(create_tb_cmd)
        except:
            print("Create table failed")
            return False
        conn.commit()
        conn.close()

    def adduser(self):
        try:
            adduser_tb_cmd='''
                CREATE TABLE IF NOT EXISTIS userslist
                (ID INTEGER PRIMARY KEY AUTO_INCREMENT,
                loginname TEXT,
                passwd TEXT,
                nickname TEXT
                );
            '''
            self.__conn.execute(adduser_tb_cmd)
        except:
            print("")
            return False
        self.__conn.commit()


if __name__=='__main__':
    d=dao()
    d.adduser('testuser')