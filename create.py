from application import db
from application.models import Tools, Users

db.drop_all()
db.create_all()
