import sqlite3

class dao:
    __conn=sqlite3.connect('todo_list.db')
    def __checkoradduser(self,username):
        # self.conn=sqlite3.connect('todo_list.db')
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS \''''+username+'''\'
                (\'ID\' INTEGER PRIMARY KEY AUTOINCREMENT,
                \'starttime\' TEXT,
                \'dealinetime\' TEXT,
                \'emergecny\' INT,
                \'cate\' TEXT);
                '''
            # 主要就是上面的语句
            self.__conn.execute(create_tb_cmd)
        except:
            print('Create table failed')
            return False
        self.__conn.commit()
        # conn.close()
        return True

    def adduser(self,newuser):
        try:
            adduser_tb_cmd='''
                CREATE TABLE IF NOT EXISTS userslist
                (ID INT AUTO_INCREMENT PRIMARY KEY,
                loginname TEXT,
                passwd TEXT,
                nickname TEXT);
            '''
            self.__conn.execute(adduser_tb_cmd)
            self.__conn.commit()
            check_tb_cmd='''SELECT count() from userslist where loginname like\''''+newuser['loginname']+'''\';'''
            cursor=self.__conn.execute(check_tb_cmd)
            self.__conn.commit()
            for c in cursor:
                if c[0]!=0:
                    return 'error username'
            insert_tb_cmd='''INSERT INTO userslist (
            loginname,
            passwd,
            nickname)VALUES (\''''\
                          +newuser['loginname']+'''\',\''''\
                          +newuser['passwd']+'''\',\''''\
                          +newuser['nickname']+'''\');'''
            self.__conn.execute(insert_tb_cmd)
            self.__conn.commit()
            if not self.__checkoradduser(newuser['loginname']):
                return 'create table failed'
        except:
            return 'sql error'
        return 'OK'

    def logincheck(self,l,p):
        check_tb_cmd = '''SELECT * from userslist where loginname like\'''' + l + '''\'and passwd like\''''+p+'''\';'''
        cursor=self.__conn.execute(check_tb_cmd)
        for c in cursor:
            if c[1]!=l:
                return 'login failed'
            if c[2]!=p:
                return 'login failed'
            return 'OK'
        return 'login failed'



if __name__=='__main__':
    d=dao()
    # d.checkoradduser("testuser")
    test2={'loginname':'test3','passwd':'test','nickname':''}
    print(d.adduser(test2))
    # print(d.logincheck('test1','test'))