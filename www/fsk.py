from flask import Flask, request, render_template, redirect, url_for, session, flash, make_response,json, jsonify
import os, logging, model, time
from flask_restful import Resource, Api, reqparse
from model import db, users, records, record_cache, pains, regions, cells, reports
import uuid

app = model.create_app()
api = Api(app)
app.secret_key = os.urandom(24)

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
        json_data = request.get_json(force=True)
        test = {'test1': json_data['test1'],'test2': json_data['test2']}
        return test, 201

api.add_resource(Test, '/api/test')

class Signup(Resource):
    def get(self):
        return {'a':'1'},201
    
    def post(self):
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
        return {'a':'1'},201
    
    def post(self):
        json_data = request.get_json(force=True)
        user = users.query.filter_by(user_name = json_data['username']).first()
        if user.user_passwd == json_data['passwd']:
            session['username'] = json_data['username']
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
        uid=users.query.filter_by(user_name=session['username']).first().User_ID
        r_list=records.query.filter_by(User_ID=uid).all()
        return json.dumps(records.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(Rlist, '/api/rlist')

class Plist(Resource):
    def get(self):
        uid=session['uid']
        r_list=pains.query.filter_by(Users_User_ID=uid).all()
        return json.dumps(pains.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(Plist, '/api/plist')

class RPlist(Resource):
    
    def get(self):
        uid=users.query.filter_by(user_name=session['username']).first().User_ID
        r_list=reports.query.filter_by(User_ID=uid).all()
        return json.dumps(reports.serialize_list(r_list)), 200
    
    def post(self):
        return 200

api.add_resource(RPlist, '/api/rplist')

class getUID(Resource):
    
    def get(self):
        if 'uid' in session:
            uid=session['uid']
        else:
            uid = None
        return json.dumps(uid), 200

api.add_resource(getUID, '/api/get_uid')

class getRID(Resource):
    
    def get(self):
        if 'rid' in session:
            rid=session['rid']
        else:
            rid = uuid.uuid1()
            session['rid'] = str(rid)
        return json.dumps(session['rid']), 200

api.add_resource(getRID, '/api/get_rid')

class getPID(Resource):
    
    def get(self):
        if 'pid' in session:
            pid=session['pid']
        else:
            pid = uuid.uuid1()
            session['pid'] = str(pid)
        return json.dumps(session['pid']), 200

api.add_resource(getPID, '/api/get_pid')

class Add_new_record(Resource):
    
    def get(self):
        return 200
    
    def post(self):
        json_data = request.get_json(force=True)
        rid = session['rid']
        uid = session['uid']
        pains_list = json_data['pains_list']
        new_record = records(str(rid),json_data['pain_count'],json_data['brief'], pains_list,str(uid))
        db.session.add(new_record)
        db.session.commit()
        session.pop("rid",None)
        return 202

api.add_resource(Add_new_record, '/api/add_new_record')

class Add_con_record(Resource):
    
    def get(self):
        return 200
    
    def post(self):
        json_data = request.get_json(force=True)
        if 'rid' in session:
            rid = session['rid']
            uid = session['uid']
            pains_list = json_data['pains_list']
            con_record = records.query.filter_by(Record_ID=rid).first()
            if con_record:
                con_record.record_brief = json_data['brief']
                con_record.pains_list = json_data['pains_list']
                con_record.pain_number = json_data['pain_count']
                db.session.commit()
            else:
                con_record = records(str(rid),json_data['pain_count'],json_data['brief'], pains_list,str(uid))
                db.session.add(con_record)
                db.session.commit()
            return 202
        else:
            return 200
        

api.add_resource(Add_con_record, '/api/add_con_record')

class Get_new_pain(Resource):

    def get(self):
        if 'pid' in session:
            pid = session['pid']
            new_pain = pains.query.filter_by(Pain_ID=pid).first()
            session.pop('pid', None)
            return json.dumps(pains.serialize(new_pain)), 202
        else:
            return 200

api.add_resource(Get_new_pain, '/api/get_new_pain')

class Add_new_pain(Resource):
    
    def get(self):
        return 200
    
    def post(self):
        json_data = request.get_json(force=True)
        pid = session['pid']
        uid = session['uid']
        depth=''
        for i in json_data['depth']:
            depth = str(i)+" "+depth

        regions=''
        for i in json_data['regions_index']:
            regions = str(i)+" "+regions

        new_pain = pains(str(pid),json_data['region_count'], regions, json_data['description'],json_data['character'],json_data['severity'],depth,json_data['frequency'],str(uid))

        user = users.query.filter_by(user_name = session['username']).first()
        user.pains_number += 1
        db.session.add(new_pain)
        db.session.commit()
        return 202

api.add_resource(Add_new_pain, '/api/add_new_pain')

class get_pain(Resource):
    def get(self):
        if 'pid' in session:
            pid = session['pid']
            pain=pains.query.filter_by(Pain_ID=pid).first()
            session.pop('pid',None)
            return json.dumps(pains.serialize(pain)), 202
        else:
            return 200
api.add_resource(get_pain, '/api/get_pain')

class get_record(Resource):
    def get(self):
        if 'rid' in session:
            rid = session['rid']
            record=records.query.filter_by(Record_ID=rid).first()
            session.pop('rid',None)
            return json.dumps(records.serialize(record)), 202
        else:
            return 200
api.add_resource(get_record, '/api/get_record')

class get_record2(Resource):
    def get(self):
        if 'rid' in session:
            rid = session['rid']
            record=records.query.filter_by(Record_ID=rid).first()
            return json.dumps(records.serialize(record)), 202
        else:
            return 200
api.add_resource(get_record2, '/api/get_record2')

class get_user(Resource):
    def get(self):
        if 'username' in session:
            user=users.query.filter_by(user_name=session['username']).first()
            return json.dumps(users.serialize(user)), 202
        else:
            return 200
api.add_resource(get_user, '/api/get_user')

class get_pains_count(Resource):
    def get(self):
        if 'username' in session:
            user=users.query.filter_by(user_name=session['username']).first()
            count = db.session.query(pains).count()
            return count, 202
        else:
            return 200

api.add_resource(get_pains_count, '/api/get_pains_count')

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

@app.route('/pain/<pain_id>', methods=['GET'])
def pain_page(pain_id):
    if 'username' in session:
        # flash('Login successfully')
        session['pid']=pain_id
        return render_template('pain.html')
    else:
        # flash('You have to logged in')
        return redirect(url_for('login_page'))

@app.route('/record/<record_id>', methods=['GET'])
def record_page(record_id):
    if 'username' in session:
        # flash('Login successfully')
        session['rid']=record_id
        return render_template('record.html')
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
    if 'username' in session:
        return render_template('new_record.html')
    else:
        return redirect(url_for('login_page'))

@app.route('/continue_record', methods=['GET'])
def continue_record_page():
    # if 'pid' in session:
    #     # createdPain = pains.query.filter_by(Pain_ID = session['pid']).first()
    #     return render_template('new_record.html', createdPain)
    # else:
    #     pass
    if 'username' in session:
        if 'rid' in session:
            return render_template('continue_record.html')
        else:
            return redirect(url_for('ulist_page'))
        # return render_template('continue_record.html')
    else:
        return redirect(url_for('login_page'))
    

@app.route('/new_pain', methods=['GET'])
def new_pain_page():

    # flash('Login successfully')
    if 'username' in session:
        return render_template('new_pain.html')
    else:
        return redirect(url_for('login_page'))
    

@app.route('/analysis', methods=['POST','GET'])
def analysis():
    if 'username' in session:
        # flash('Login successfully')
        return render_template('analysis.html')
    else:
        # flash('You have to logged in')
        return redirect(url_for('login_page'))

@app.route('/user', methods=['GET'])
def user():
    if 'username' in session:
        return render_template('user_info.html')
    else:
        return redirect(url_for('login_page'))

@app.route('/about', methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
