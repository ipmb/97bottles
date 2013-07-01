# Legacy code for 97bottles.com

This was an undocumented code dump. It is now in a state where it appears to be functional locally.
All included third-party dependencies were put into the `libs` directory until they can be
audited and updated.

The goal is to get the project in a state where it can be hosted at Heroku.

## Installation

To get setup, from within the `ninetyseven` directory (ideally within a virtualenv):

1. `cp settings/local.py.example settings/local.py`
2. Edit `settings/local.py` as needed
3. `pip install Pillow python-mysql`
4. `./manage.py syncdb --settings=settings.local`
7. `./manage.py runserver --settings=settings.local`


## To do

* ~~Get project running locally~~
* ~~Document local install~~
* ~~Test app on Postgres~~
* Upgrade Django to version with security updates
* Setup Heroku stuff (`Procfile`, S3, etc.)
* Migrate MySQL data to Postgres and reset passwords
