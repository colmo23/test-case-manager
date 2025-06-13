# pcap-maker
 

## Install
Setup 
```
python3 -m venv venv
source venv/bin/activate
```

```
pip install Django djangorestframework

python manage.py startapp testcases


python manage.py makemigrations
python manage.py migrate
python manage.py runserver



Add:
curl -X POST   http://127.0.0.1:8000/api/testcases/   -H "Content-Type: application/json"   -d '{
        "title": "Validate User Registration2",
        "description": "Test the user registration flow with various valid and invalid inputs222.",
        "priority": "High",
        "status": "Draft"
      }'

View:
curl http://127.0.0.1:8000/api/testcases/
```



## Unittests

```
pip3 install pytest
pytest .
```

## Code reformatting

```
pip3 install autopep8
autopep8 --in-place --aggressive --aggressive pcap_maker/*py
```

```
pip3 install black
black pcap_maker
```
## Code style
```
pip3 install flake8
flake8 pcap_maker
```


## CI tests
```
pip3 install tox
tox
```

