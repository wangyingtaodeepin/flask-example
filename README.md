# flask-example

# handle database migration
(venv) $ python hello.py db migrate -m "initial migration"
(venv) $ python hello.py db upgrade
(venv) $ python hello.py db downgrade

# recovery virtualenv enviroment
(venv) $ pip install -r requirements.txt

# backup virtualenv enviroment
(venv) $ pip freeze > requirements.txt
