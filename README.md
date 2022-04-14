# Django tutorials

## Set up

```sh
# create virtual environment
python -m venv env

# activate it
source env/bin/activate

# install django
pip install django
```

## Run `foo` project

```sh
# change into the project directory
cd foo

# run migrations (this will create the database the first time it is run)
python manage.py migrate

# run development server
python manage.py runserver
```
