# import logging; logging.basicConfig(level=logging.INFO)

# import asyncio, os, json, time
# from datetime import datetime
# from aiohttp import web
from flask import Flask, request, render_template, redirect, url_for, session, flash, make_response,json, jsonify
import os, logging, model, time
from flask_restful import Resource, Api, reqparse
from model import db, users, records, pains, regions, cells, reports
import uuid
# from flask_login import LoginManager, login_required


app = model.create_app()
api = Api(app)
app.secret_key = os.urandom(24)

#parsing data
parser = reqparse.RequestParser()
parser.add_argument('test1', type='str')
parser.add_argument('test2', type='str')
json_data={'test1':'', 'test2':''}

def pain_cache(json_data):
    data = json_data
    return data

class Test(Resource):
    def get(self):
        test = {'test1': session['pid'],
                'test2': session['rid']}
        return test,201
    def post(self):
        # args = parser.parse_args()
        # test1 = args['test1']
        # test2 = args['test2']
        json_data = request.get_json(force=True)
        test = {'test1': json_data['test1'],'test2': json_data['test2']}
        # json_data = test
        # print(args['test1'])
        return test, 201

api.add_resource(Test, '/api/test')

class Signup(Resource):
    def get(self):
        # Users.query.all()
        return {'a':'1'},201
    
    def post(self):
        # args = parser.parse_args()
        json_data = request.get_json(force=True)
        user_id=uuid.uuid3(uuid.NAMESPACE_DNS,json_data['username'])
        new_user = users(str(user_id),json_data['username'],json_data['passwd'],int(time.strftime('%Y',time.localtime(time.time())))-int(json_data['birth_year']), json_data['gender'])
        db.session.add(new_user)
        db.session.commit()
        flash("Sign up successfully")
        return json_data,201

api.add_resource(Signup, '/api/signup')

class Login(Resource):
    def get(self):
        # Users.query.all()
        return {'a':'1'},201
    
    def post(self):
        # args = parser.parse_args()
        json_data = request.get_json(force=True)
        user = users.query.filter_by(user_name = json_data['username']).first()
        if user.user_passwd == json_data['passwd']:
            session['username'] = json_data['username']
            # flash(session['username'])
            session['uid'] = users.query.filter_by(user_name = json_data['username']).first().User_ID
            return 202
        else:
            err = 'invalid username or password'
            return err, 200

api.add_resource(Login, '/api/login')

class Logout(Resource):
    
    def post(self):
        session.pop('username', None)
        session.pop('uid', None)
        flash('you have logged out')
        return 202

api.add_resource(Logout, '/api/logout')

class Rlist(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        uid=users.query.filter_by(user_name=session['username']).first().User_ID
        r_list=records.query.filter_by(User_ID=uid).all()
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(records.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(Rlist, '/api/rlist')

class Plist(Resource):
    def get(self):
        # json_data = request.get_json(force=True)
        uid=users.query.filter_by(user_name=session['username']).first().User_ID
        r_list=pains.query.filter_by(Users_User_ID=uid).all()
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(pains.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(Plist, '/api/plist')

class RPlist(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        uid=users.query.filter_by(user_name=session['username']).first().User_ID
        r_list=reports.query.filter_by(User_ID=uid).all()
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(reports.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(RPlist, '/api/rplist')

class getUID(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        if 'uid' in session:
            uid=session['uid']
        else:
            uid = None
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(uid), 200

api.add_resource(getUID, '/api/get_uid')

class getRID(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        # if 'rid' in session:
        #     rid=session['rid']
        #     if 'pid' in session:
        #         createdPain = pains.query.filter_by(Pain_ID = "f0a46d88-9b03-11e8-b352-dca904720f2060c-98e14142f81a").first()
        #         data = {'rid':rid, 'createdPain':createdPain}
        #     else:
        #         data=rid
        # else:
        #     rid = uuid.uuid1()
        #     session['rid'] = str(rid)
        #     data = session['rid']
        # json_data = request.get_json(force=True)
        if 'rid' in session:
            rid=session['rid']
        else:
            rid = uuid.uuid1()
            session['rid'] = str(rid)
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(session['rid']), 200
        # createdPain = pains.query.filter_by(Pain_ID = "1").first()
        # data = jsonify(createdPain.serialize)
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        # return json.dumps(data), 200

api.add_resource(getRID, '/api/get_rid')

class getPID(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        if 'pid' in session:
            pid=session['pid']
        else:
            pid = uuid.uuid1()
            session['pid'] = str(pid)
        
        # return jsonify(json_list=[i.serialize for i in r_list]), 200
        return json.dumps(session['pid']), 200

api.add_resource(getPID, '/api/get_pid')

class Add_new_record(Resource):
    
    def get(self):
        # json_data = request.get_json(force=True)
        return 200
    
    def post(self):
        json_data = request.get_json(force=True)
        rid = session['rid']
        uid = session['uid']
        new_record = records(str(rid),json_data['pain_count'],json_data['brief'],str(uid))
        db.session.add(new_record)
        db.session.commit()
        session.pop("rid",None)
        return 202

api.add_resource(Add_new_record, '/api/add_new_record')

class Add_new_pain(Resource):
    
    def get(self):
        return 200
    
    def post(self):
        json_data = request.get_json(force=True)
        # if 'pid' in session and 'uid' in session:
        pid = session['pid']
        #     rid = session['rid']
        uid = session['uid']
        #     flash(pid)
        # uid = users.query.filter_by(user_name = session['username']).first().User_ID
        depth=''
        for i in json_data['depth']:
            depth = str(i)+" "+depth

        regions=''
        for i in json_data['regions_index']:
            regions = str(i)+" "+regions

        new_pain = pains(str(pid),json_data['region_count'], regions, json_data['description'],json_data['character'],json_data['severity'],depth,json_data['frequency'],str(uid))
        db.session.add(new_pain)
        db.session.commit()

        # pain_cache(json_data)
        session.pop("pid",None)
        return 202
        # else:
        #     return None

api.add_resource(Add_new_pain, '/api/add_new_pain')

@app.route('/test',methods=['GET'])
def test2():
    return render_template('test.html')

@app.route('/')
def index():
    return redirect(url_for('ulist_page'))

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/ulist', methods=['GET'])
def ulist_page():
    if 'username' in session:
        # flash('Login successfully')
        session.pop('pid',None)
        session.pop('rid',None)
        return render_template('list.html')
    else:
        # flash('You have to logged in')
        return redirect(url_for('login_page'))

@app.route('/new_record', methods=['GET'])
def new_record_page():
    # if 'pid' in session:
    #     # createdPain = pains.query.filter_by(Pain_ID = session['pid']).first()
    #     return render_template('new_record.html', createdPain)
    # else:
    #     pass
    session.pop('pid',None)
    return render_template('new_record.html')
        # flash('Login successfully')
    

@app.route('/new_pain', methods=['GET'])
def new_pain_page():

    # flash('Login successfully')
    return render_template('new_pain.html')

@app.route('/analysis', methods=['POST','GET'])
def analysis():
    if 'username' in session:
        # flash('Login successfully')
        return render_template('list.html')
    else:
        # flash('You have to logged in')
        return redirect(url_for('login_page'))

@app.route('/user', methods=['GET'])
def user():
    if 'username' in session:
        return render_template('user_info.html')
    else:
        return redirect(url_for('login_page'))

@app.route('/info', methods=['POST','GET'])
def info():
    return render_template('help.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
    # func()

# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'

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