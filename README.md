# Django Image resizer

[overview here]

## Developer Guide
### TECH USER

- pipenv, as a env and depandancies manager
- django 5, latest django version
- bootstrap 5, for app theme and styling
- PILLOW, python library that handels image (used it to resieze the images)

### installation 


# first install and start the env
```
pipenv install && pipenv shell
```

# run the migrations 
```
./manage.py migrate
```

# load test user to the db
```
./manage.py loaddata fixtures/user_data.json
```

# start the server
```
./manage.py runserver
```

# go to the browser
```
http://localhost:8000
```

# user credentials

email: 
```
test@test.com
```
password: 
```
testpassword
```
