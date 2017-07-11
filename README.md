# CSV API

Quickly expose a CSV file as a RESTful API - intended to prototype data products given that most organisations can get their hands on CSV exports quickly.

Main setup is done through ```column_mapping.py```, whose headers need to match those in the header row in ```data.csv```.

No provision made for non-ASCII encoding or fancy quoted CSV formats.

Totally unsupported - use at your own risk.

Usage:

```
virtualenv venv
pip install -r requirements.txt
. venv/bin/activate
FLASK_APP=app.py flask run
```

Then visit [http://localhost:5000/](http://localhost:5000/), [http://localhost:5000/Leeds](http://localhost:5000/Leeds), [http://localhost:5000/Leeds/2017-05-31](http://localhost:5000/Leeds/2017-05-31) etc. (assuming you're using the sample ```data.csv```).

Edit ```column_mapping.py``` to make this work for you. Mapping names _must_ match column headings in ```data.csv```.
