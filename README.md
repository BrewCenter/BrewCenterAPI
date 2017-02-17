# BrewCenterAPI

## Installation
Install the requirements using pip.
```
pip install -r requirements.txt
```
Then, copy `brewcenter_api/example.settings.py` to `brewcenter_api/settings.py` and modify to your needs.

Create your database:
```
python manage.py migrate
```

Update your data by mining known sources:
```
python manage.py updatedata
```

Run the app:
```
python manage.py runserver
```