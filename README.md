## Project setup

```bash
# installing pipenv as system package
pip install pipenv
# installing project dependencies, use --python 3.6 if it's installed
pipenv install --python3
# activating virtualenv via pipenv
pipenv shell
# run migration
./manage.py migrate
# create a superuser to play with your models via admin
./manage.py createsuperuser
# run django server
./manage.py runserver
```
