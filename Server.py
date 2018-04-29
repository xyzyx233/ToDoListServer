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

if __name__ == '__main__':
    app.run(debug=True)