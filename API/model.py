from API import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    Fullname = db.Column(db.String(120))
    Address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    State = db.Column(db.String(120))
    Country = db.Column(db.String(120))
    Phone = db.Column(db.Integer, nullable=False)
    Pincode = db.Column(db.Integer, nullable=False)

    post = db.relationship('Content', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.email}',{self.Fullname},{self.Pincode},{self.Pincode})"


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(30), nullable=False)
    Body = db.Column(db.Text, nullable=False)
    Summary = db.Column(db.String(60), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    PostTags = db.Column(db.String(60))
    Filename = db.Column(db.String(20), nullable=False)
