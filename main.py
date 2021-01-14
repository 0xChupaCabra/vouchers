from flask import Flask, render_template, request, redirect, url_for, session 
from hashids import Hashids
hash_id = Hashids(salt='secretcode', min_length=10)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/genvouch', methods =['POST']) 
def genvouch(): 
    msg = '' 
    if request.method == 'POST' and 'user' in request.form and 'count' in request.form:
        user = int(request.form['user'])
        count = int(request.form['count'])
        try:
            a = hash_id.encode(user, count)
            msg = a
        except:
            msg = 'Error'
    else:
        msg = 'Error'
    return msg


@app.route('/getvouch', methods =['POST']) 
def getvouch(): 
    msg = '' 
    if request.method == 'POST' and 'code' in request.form:
        code = str(request.form['code'])
        #count = int(request.form['count'])
        try:
            c = hash_id.decode(code)
            userid = str(c[0])
            nodescount = str(c[1])
            msg = 'USER: ' +userid+ ' NODES: '+nodescount
            print(msg)

        except:
            msg = 'Error'
    else:
        msg = 'Error'
    return msg

app.run(host='0.0.0.0', port=5000, debug=True)
