from shop import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    picture = db.Column(db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.picture}')"


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100))
    price = db.Column(db.Numeric(6, 2), nullable=False)
    description = db.Column(db.String(4000))
    picture = db.Column(db.String(30), default='default.jpg')
    year = db.Column(db.Integer)
    genre = db.Column(db.String(30))

    def __repr__(self):
        return f"Record('{self.name}', '{self.artist}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Cart('{self.id}', '{self.item_id}')"
