# from flask_mongoengine import MongoEngine
# from flask_bcrypt import Bcrypt
# app = None
# security_db = None
# bcrypt = None
# def setup(cur_app):
#     global app  
#     app = cur_app
#     global security_db
#     security_db = MongoEngine(app)
#     global bcrypt
#     bcrypt = Bcrypt(app)
# setup(app)

#app 還沒初始化



# user_datastore = MongoEngineUserDatastore(security_db,Role_User.Role,Role_User.User)
# security = Security(app,user_datastore)
# bcrypt = Bcrypt()