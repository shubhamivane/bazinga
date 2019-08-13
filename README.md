# Bazinga
Shopify webhook for order create event when a order is created on the [shop](https://bazingashubhamtest.myshopify.com/) then this system is notified.
\newline
![Image of Home Page](https://github.com/shubhamivane/bazinga/blob/master/screenshots/home.png)
![Image of Order Page](https://github.com/shubhamivane/bazinga/blob/master/screenshots/order.png)

## Programming Language, Framework and Database used
 Python 3.6.8
 Flask 1.1.1
 Postgres
 (If you want to use any other database. So, change DATABASE_URI in config.py.)

## Project Setup
* Create a virtual environment. 
```
  python3 -m venv env
```
* Activate virtual environment.
```
  source /bin/activate
```
* Install packages.
```
  pip3 install -r requirement.txt
```
* Create migrations folder.
```
  python3 manage.py db init
```
* Make migrations.
```
  python3 manage.py db migrate
```
* Apply migrations.
```
  python3 manage.py db upgrade
```
* Run server
```
  python3 manage.py runserver
```
