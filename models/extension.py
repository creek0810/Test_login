from flask_security import UserMixin, RoleMixin
from flask_bcrypt import Bcrypt
from flask_security import Security, MongoEngineUserDatastore
from flask_mongoengine import MongoEngine
from models import db



app = None
def setup(cur_app):
    global app
    app = cur_app

security_db = MongoEngine(app)
bcrypt = Bcrypt(app)

# 不同種權限身份
class Role(security_db.Document, RoleMixin):
    name = security_db.StringField(max_length=80, unique=True)
    description = security_db.StringField(max_length=255)
    
# 使用者資訊
class User(security_db.Document, UserMixin):
    email = security_db.StringField(max_length=255)
    password = security_db.StringField(max_length=255)
    active = security_db.BooleanField(default=True)
    confirmed_at = security_db.DateTimeField()
    roles = security_db.ListField(security_db.ReferenceField(Role), default=[])

user_datastore = MongoEngineUserDatastore(security_db,Role,User)
security = Security(app,user_datastore)

def create_user():
    print(user_datastore)
    student_role = user_datastore.find_or_create_role('student')
    print(student_role)
    if user_datastore.get_user('Liao') == None:     
        print('345')
        user_datastore.create_user(
            email='Liao', password = hashPassword('871029'), roles=[student_role]
        )
#密碼加密
def hashPassword(password):
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    return pw_hash


def validate_user(now_user:dict) :  
    print("validating user")
    user_in_db = db.USER_COLLECTION.find_one({'email':now_user['email']})
    print(user_in_db)                                          
    if user_in_db is None:
        return "無此使用者"
    elif bcrypt.check_password_hash(user_in_db['password'], now_user['password']) is False:
        return "密碼錯誤"
    print('You are enter')
    print(now_user['email'])
    now_user = user_datastore.get_user(now_user['email'])
    print(now_user)
    return now_user
