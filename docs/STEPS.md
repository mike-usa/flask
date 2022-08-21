1. https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f

Setup Directory
```bash
brew install python
md flask flask/project flask/project/app

cd flask/project
python3 -m venv .venv
. .venv/bin/activate
pip install flask flask_migrate python-dotenv psycopg2
pip freeze > requirements.txt     # use: pip install -r requirements.txt
touch app.py config.py

cd app
# create directories (in flask/project/app/)
mkdir models views controllers databases routes views/layouts
chmod -R 755 *
# create files (in flask/project/app/)
touch models/__init__.py views/__init__.py controllers/__init__.py
touch databases/__init__.py routes/__init__.py views/layouts/__init__.py
touch models/User.py models/Group.py models/Account.py models/Role.py
touch controllers/UserController.py controllers/GroupController.py
touch views/layouts/base.html
chmod -R 755 *.py
```
