from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    color = db.Column(db.Text, nullable=False)

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "email": self.email,
            "color": self.color
        }
