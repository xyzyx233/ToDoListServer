from flask import Flask
from flask import request
import json
from FileUtil import FileUtil
from dbUtil import dao
app = Flask(__name__)

@app.route('/')
def hello_world():
    f=FileUtil()
    return f.readHtml()

@app.route('/login',methods=['POST'])
def login():
    j=request.data
    string=str(j,encoding='utf-8')
    dic=json.loads(string)
    d=dao()
    re=d.logincheck(dic['loginname'],dic['passwd'])
    return json.dumps(re)

@app.route('/addaction',methods=['POST'])
def addactin():
    j=request.data
    string=str(j,encoding='utf-8')
    dic=json.loads(string)
    d=dao()
    result=d.insertactivity(dic['activity'],dic['uuid'])
    if not result=='OK':
        d={'status':'error','info':result}
        rj=json.dumps(d)
        return rj
    d={'status':'OK'}
    return json.dumps(d)

@app.route('/getallactivity',methods=['POST'])
def getall():
    j = request.data
    string = str(j, encoding='utf-8')
    dic = json.loads(string)
    d = dao()
    result = d.getactivities(dic['uuid'])
    if result == 'sql error':
        d = {'status': 'error', 'info': result}
        rj = json.dumps(d)
        return rj
    d = {'status': 'OK','result':result}
    return json.dumps(d)

@app.route('/deleteacition',methods=['POST'])
def deleteaction():
    j = request.data
    string = str(j, encoding='utf-8')
    dic = json.loads(string)
    d = dao()
    result = d.getactivities(dic['list'],dic['uuid'])
    if not result == 'OK':
        d = {'status': 'error', 'info': result}
        rj = json.dumps(d)
        return rj
    d = {'status': 'OK'}
    return json.dumps(d)


@app.route('/updateacition',methods=['POST'])
def deleteaction():
    j = request.data
    string = str(j, encoding='utf-8')
    dic = json.loads(string)
    d = dao()
    result = d.getactivities(dic['list'],dic['uuid'])
    if not result == 'OK':
        d = {'status': 'error', 'info': result}
        rj = json.dumps(d)
        return rj
    d = {'status': 'OK'}
    return json.dumps(d)


@app.route('/registion',methods=['POST'])
def deleteaction():
    j = request.data
    string = str(j, encoding='utf-8')
    dic = json.loads(string)
    d = dao()
    result = d.getactivities(dic['newuser'])
    if not result == 'OK':
        d = {'status': 'error', 'info': result}
        rj = json.dumps(d)
        return rj
    d = {'status': 'OK','result':result}
    return json.dumps(d)

if __name__ == '__main__':
    app.run(debug=True)