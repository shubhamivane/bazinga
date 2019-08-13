# Bazinga
Shopify webhook for order create event when a order is created on the [shop](https://bazingashubhamtest.myshopify.com/) then this system is notified by Shopify.
![Image of Home Page](https://drive.google.com/file/d/1HOqfg2u1_ybo1V-Dwrs0C8e7cIeflv85/view?usp=sharing)
![Image of Order Page](https://drive.google.com/file/d/1GKIqVuPkVfMufqmHhSX4X9aw7Is_SyAU/view?usp=sharing)

## Programming Language, Framework and Database used
 Python 3.6.8
 Flask 1.1.1
 Postgres
 (If you want to use any other database. So, change DATABASE_URI in config.py.)

## Project Setup
* Create a virtual environment. 
```
  Python
  python3 -m venv env
```
* Activate virtual environment.
```
  Python
  source /bin/activate
```
* Install packages.
```
  Python
  pip3 install -r requirement.txt
```
* Create migrations folder.
```
  Python
  python3 manage.py db init
```
* Make migrations.
```
  Python
  python3 manage.py db migrate
```
* Apply migrations.
```
  Python
  python3 manage.py db upgrade
```
* Run server
```
  Python
  python3 manage.py runserver
```
