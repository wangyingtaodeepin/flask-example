# flask-example

# handle database migration
(venv) $ python hello.py db init</br>
(venv) $ python hello.py db migrate -m "initial migration"</br>
(venv) $ python hello.py db upgrade</br>
(venv) $ python hello.py db downgrade</br>

# recovery virtualenv enviroment
(venv) $ pip install -r requirements.txt

# backup virtualenv enviroment
(venv) $ pip freeze > requirements.txt
