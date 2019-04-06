# ToDo
Todo application using DJANGO and MYSQL db.
 Features :-
 1) User Authentication
 2) Create todo
 3) Delete todo
 4) Edit existing todo
 5) Set Title, Description, Status( not started -> working -> done) and due date in your todo
 6) Date of creation is also stored.
 7) User sees only his todos.
 8) No access to Unauthenticated user.
 9) Filter todo on the basis of status.

 ## Installation
 ------------
 To the terminal:
```
git clone https://github.com/shubham7298/ToDo.git
cd ToDo
```
To install without a virtual environment.
```
pip install -r requirements.txt
```
For virtual environment install $pipenv
```
pip install --user pipenv
pipenv install -r requirements.txt
pipenv shell
```

## Run
 ------------
 To run django application.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
 ```

 Enjoy the Fun !!