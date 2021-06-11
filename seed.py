from app import app
from models import Users, db

# create all tables
db.drop_all()
db.create_all()

u1 = Users(name="Jon", year=1978, email="cun3@gmail.com", color="Green")
u2 = Users(name="Yaneth", year=1984, email="jan6@gmail.com", color="White")

db.session.add(u1)
db.session.add(u2)

db.session.commit()
