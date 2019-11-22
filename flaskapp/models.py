from flaskapp import db
class Address(db.model):
    id= db.Column(ab.Integer, primary_key=True)
    housenumber=db.Column(db.String(5),index=True, unique=True)
    stname = db.Column(db.String(64), index=True, unique=True)
    city = db.Column(db.String(30), index=True, unique=True)
    unit = db.Column(db.String(10), index=True, unique=True)
    phonenumber=db.Column(db.String(20), index=True, unique=True)


    def __repr__(self):
        return '<User {}>'.format(self.username)
