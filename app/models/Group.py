from app.databases.app_db import db
from tokenize import String

class Group(db.Model):
  __tablename__ = 'groups'
  # __bind_key__ = 'key-to-other-db in SQLALCHEMY_BINDS
  # __table_args__ = {'schema': 'dev'}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  platform = db.Column(db.String)
  domain = db.Column(db.String)

  @property
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'platform': self.platform,
      'domain': self.domain, 
      'type': self.type,
    }