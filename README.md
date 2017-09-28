# BrewCenterAPI

## Installation
Install the requirements using pip.
```
pip install -r requirements.txt
```
Then, copy `brewcenter_api/example.settings.py` to `brewcenter_api/settings.py` and modify to your needs.

To create your database, execute the followng command:
```
python manage.py migrate
```

To update your data by mining known sources, execute the followng command:
```
python manage.py updatedata
```

To run the app, execute the followng command:
```
python manage.py runserver
```
