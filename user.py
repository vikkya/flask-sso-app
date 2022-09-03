from flask_login import UserMixin

from db import get_db

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name,
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute("select * from user where id = ?", (user_id,)).fetchone()
        if not user:
            return None
        user = User(id_=user[0], name=user[1], email=user[2], profile_pic=user[3])
        return user
    
    @staticmethod
    def create(id_, name, email, profile_pic):
        db = get_db()
        db.execute("insert into user (id, name, email,profile_pic) values (?,?,?,?)", (id_, name, email, profile_pic))
        db.commit()