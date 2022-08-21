from flask import Flask, render_template
from flask_migrate import Migrate

from app.routes.user import bp as user_bp
from app.routes.group import bp as group_bp
from app.databases.app_db import db
from app.databases.app_db import Config

app = Flask(__name__, template_folder='./app/views')
app.config.from_object('config')
app.config.from_object(Config)
print(app.config)
db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(group_bp, url_prefix='/groups')

if __name__ == '__main__':
  app.run()