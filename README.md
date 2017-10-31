# BrewCenterAPI

### What the heck is a BrewCenter API?
The BrewCenter API is an open source and free-to-use API for sharing brewing related data. Using this API, brewgrammers (brewing programmers) can share scientific specifications for fermentables, hops, yeast, and other pertinent information for the creating of brewing related apps!
The aim of this project is not to make a product for the average homebrewer, but rather to make a product for the experienced brewgrammer. This API will allow people to fetch all of its data. This data can then be used in other brewing applications to populate fields and choices with values that the community agrees are correct.

### Where's the data come from?
This data set will largely be crowdsourced, with some initial seed data inserted when it launches. Users of the API will be able to suggest improvements to the dataset via a web form on our future website or by POSTing directly to the API.

### How does it work?
The BrewCenter API is a django rest framework application. We store all of our data in a SQL-based database, and make it available via RESTful endpoints which return JSON data.

## Installation
Install the requirements using pip.
```
pip install -r requirements.txt
```
Then, copy `brewcenter_api/example.settings.py` to `brewcenter_api/settings.py` and modify to your needs.

To create your database, execute the following command:
```
python manage.py migrate
```

To update your data by mining known sources, execute the following command:
```
python manage.py updatedata
```

To run the app, execute the following command:
```
python manage.py runserver
```
