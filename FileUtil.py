#-*- coding:utf-8 -*-

class FileUtil:

    def readHtml(self):
        f=open('./index.html','r');
        return f.read()


if __name__ =='__main__':
    ff=FileUtil()
    print(ff.readHtml())