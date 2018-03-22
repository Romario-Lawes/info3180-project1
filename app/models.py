from . import db


class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    location = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    bio = db.Column(db.Text)
    photo = db.Column(db.String(80))
    created_on = db.Column(db.String(80)) 

    def __init__(self, firstname, lastname, email, location, gender, bio, photo, created_on):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.gender = gender
        self.bio = bio
        self.photo = photo
        self.created_on = created_on
        

    def __repr__(self):
        return '<User %r>' % str(self.id)
