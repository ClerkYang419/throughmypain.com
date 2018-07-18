# import logging; logging.basicConfig(level=logging.INFO)

# import asyncio, os, json, time
# from datetime import datetime
# from aiohttp import web
from flask import Flask, request, render_template, redirect, url_for, session, flash, make_response
import flask, os, logging

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return redirect(url_for('ulist'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        if valid_login(request.form['username'],request.form['password']):
            return redirect(url_for('ulist'))
        else:
            flash('Invalid username/password')

    # else:
    #     flash('Invalid username/password')
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')

def valid_login(username, password):
    if username and password:
        return True
    else:
        return False

@app.route('/register', methods=['POST','GET'])
def register():
    return render_template('register.html')

@app.route('/ulist', methods=['POST','GET'])
def ulist():

    if 'username' in session:
        flash('Login successfully')
        return render_template('list.html')
    else:
        flash('You have to logged in')
        return redirect(url_for('login'))


@app.route('/analysis', methods=['POST','GET'])
def analysis():
    
    if 'username' in session:
        flash('Login successfully')
        return render_template('list.html')
    else:
        flash('You have to logged in')
        return redirect(url_for('login'))

@app.route('/user', methods=['GET'])
def user():
    if 'username' in session:
        return render_template('user_info.html')
    else:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if request.form['logout']:
            session.pop['username', None]
            return redirect(url_for('user'))

@app.route('/logout', methods=['POST','GET'])
def logout():
    if 'username' in session:
        session.pop('username',None)
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
            
            

@app.route('/info', methods=['POST','GET'])
def info():
    return render_template('help.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True

app.run()


    

# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')
    
# @asyncio.coroutine
# def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET', '/', index)
#     srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return srv

# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()