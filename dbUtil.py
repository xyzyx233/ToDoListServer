import sqlite3
import uuid

class dao:
    __conn=sqlite3.connect('todo_list.db')

    def __uuidtotablename(self,u):
        check_tb_cmd = '''SELECT loginname from userslist where nickname like\'''' + u + '''\';'''
        cursor = self.__conn.execute(check_tb_cmd)
        self.__conn.commit()
        for c in cursor:
            n = c[0]
        return n
    def __checkoradduser(self,username):
        # self.conn=sqlite3.connect('todo_list.db')
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS \''''+username+'''\'
                (\'ID\' INTEGER PRIMARY KEY AUTOINCREMENT,
                \'instrudction\' TEXT,
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
                CREATE TABLE IF NOT EXISTS \'userslist\'
                (\'ID\' INT AUTO_INCREMENT PRIMARY KEY,
                \'loginname\' TEXT,
                \'passwd\' TEXT,
                \'nickname\' TEXT);
            '''
            self.__conn.execute(adduser_tb_cmd)
            self.__conn.commit()
            check_tb_cmd='''SELECT count() from userslist where loginname like\''''+newuser['loginname']+'''\';'''
            cursor=self.__conn.execute(check_tb_cmd)
            self.__conn.commit()
            for c in cursor:
                if c[0]!=0:
                    return 'error username'
            insert_tb_cmd='''INSERT INTO userslist (loginname,passwd,nickname)VALUES (\''''+newuser['loginname']+'''\',\''''+newuser['passwd']+'''\',\''''+str(uuid.uuid1())+'''\');'''
            self.__conn.execute(insert_tb_cmd)
            self.__conn.commit()
            if not self.__checkoradduser(newuser['loginname']):
                return 'create table failed'
        except:
            return 'sql error'
        return 'OK'

    def logincheck(self,l,p):
        try:
            check_tb_cmd = '''SELECT * from userslist where loginname like\'''' + l + '''\'and passwd like\''''+p+'''\';'''
            cursor=self.__conn.execute(check_tb_cmd)
            self.__conn.commit()
            for c in cursor:
                if c[1]!=l:
                    return 'login failed'
                if c[2]!=p:
                    return 'login failed'
                return {'staus':'OK','uuid':c[3]}
            return 'login failed'
        except:
            return 'sql error'

    def insertactivity(self,a,u):
        try:
            n=self.__uuidtotablename(u)
            insertactivity_tb_cmd='''INSERT INTO '''+n+'''(instrudction,starttime,dealinetime,emergecny,cate )
            VALUES (\''''+a['instrudction']+'''\',\''''+a['starttime']+'''\',\''''+a['dealinetime']+'''\','''+ a['emergecny'] + ''',\''''+a['cate']+'''\');'''
            self.__conn.execute(insertactivity_tb_cmd)
            self.__conn.commit()
            return 'OK'
        except:
            return 'sql error'

    def getactivities(self,u):
        list=[]
        try:
            n = self.__uuidtotablename(u)
            allinfo_tb_cmd='''SELECT ID,instrudction,starttime,dealinetime,emergecny,cate from '''+n
            c=self.__conn.execute(allinfo_tb_cmd)
            self.__conn.commit()
            for a in c:
                x={'ID':a[0],'instrudction':a[1],'starttime':a[2],'dealinetime':a[3],'emergecny':a[4],'cate':a[5]}
                list.append(x)
            return list
        except:
            return 'sql error'

    def updateactivities(self,list,u):
        #UPDATE COMPANY set SALARY = 25000.00 where ID=1
        try:
            n = self.__uuidtotablename(u)
            for l in list:
                update_tb_cmd='''UPDATE '''+n+''' set instrudction = \''''+l['instrudction']+'''\'
                ,starttime = \''''+l['starttime']+'''\'
                ,dealinetime = \''''+l['dealinetime']+'''\'
                ,emergecny = '''+str(l['emergecny'])+'''
                ,cate = \''''+l['cate']+'''\' where ID = '''+str(l['ID'])
                self.__conn.execute(update_tb_cmd)
            self.__conn.commit()
            return 'OK'
        except:
            return 'sql error'

    def deleteactivities(self,list,u):
        try:
            n = self.__uuidtotablename(u)
            for l in list:
                detele_tb_cmd='''DELETE FROM '''+n+''' where ID = '''+str(l['ID'])
                self.__conn.execute(detele_tb_cmd)
            self.__conn.commit()
            return 'OK'
        except:
            return 'sql error'

if __name__=='__main__':
    d=dao()
    # d.checkoradduser("testuser")
    # test2={'loginname':'test3','passwd':'test'}
    # print(d.adduser(test2))
    s=d.logincheck('test3','test')
    # print(s['uuid'])
    # aa={'instrudction':'test1331','starttime':'test11','dealinetime':'test111','emergecny':'121','cate':'test1111'}
    # print(d.insertactivity(aa,s['uuid']))
    # print(uuid.uuid1())
    lll=[{'ID': 2, 'instrudction': 'testadfa', 'starttime': 'test1dddd', 'dealinetime': 'test111', 'emergecny': 121, 'cate': 'test1111'}]
    print(d.deleteactivities(lll,s['uuid']))
