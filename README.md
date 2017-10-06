# BrewCenterAPI
An open source API for sharing and crowd-sourcing brewing ingredient data. Grains, Sugars, Adjusts, Beer Styles, Hops, and Yeast data will all be made available for free. We'll provide easy-to-use interfaces for you to make suggestions to existing data or add new data to our API. Together we can make the best brewing database on the web!

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
