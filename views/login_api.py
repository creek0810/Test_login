from flask import flash, redirect, Blueprint, request, session, jsonify
from flask_bcrypt import Bcrypt
from models import extension

login_api = Blueprint('login_api', __name__)
bcrypt = Bcrypt()

#密碼加密
def hashPassword(password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return pw_hash

#沒有權限導引畫面
def unauthorized_callback():
    flash("你沒有權限") 
    return redirect('/login')

# 設定未授權時轉跳畫面
# security._state.unauthorized_handler(unauthorized_callback)

@login_api.route('/login_user',methods = ['POST'])
def login_user():
    # try:
    now_user = request.values.to_dict()
    print(now_user)
    #
    now_user = extension.validate_user(now_user)
    print("validate"+now_user)
    if type(now_user) is not str:            
    #    設置session
        session['username'] = now_user['email']
        session.permanent = True
        

        login_user(now_user)
        return jsonify(now_user)
    else:
        return now_user
    # except:
    #     return "失敗"
