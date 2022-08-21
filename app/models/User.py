from app.databases.app_db import db
from tokenize import String

class User(db.Model):
  __tablename__ = 'users'
  # __bind_key__ = 'key-to-other-db in SQLALCHEMY_BINDS
  # __table_args__ = {'schema': 'dev'}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  username = db.Column(db.String)
  email = db.Column(db.String)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'username': self.username,
      'email': self.email
    }