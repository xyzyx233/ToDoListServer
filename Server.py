from flask import Flask
from flask import request
from FileUtil import FileUtil
app = Flask(__name__)

@app.route('/')
def hello_world():
    f=FileUtil()
    return f.readHtml()
@app.route('/login',methods=['POST'])
def login():
    j=request.data
    return j

if __name__ == '__main__':
    app.run(debug=True)