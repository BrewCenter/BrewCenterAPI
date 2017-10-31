# BrewCenterAPI

### What the heck is a BrewCenter API?
The BrewCenter API is an open source and free-to-use API for sharing brewing related data. Using this API, brewgrammers (brewing programmers) can share scientific specifications for fermentables, hops, yeast, and other pertanent information for the creating of brewing related apps!
The aim of this project is not to make a product for the average homebrewer, but rather to make a product for the experienced brewgrammer. This API will allow people to fetch all of its data. This data can then be used in other brewing applications to prepopulate fields and choices with values that the community agrees are correct. 

### Where's the data come from?
This data set will largely be crowdsourced, with some initial seed data inserted when it launches. Users of the API will be able to suggest improvements to the dataset via a web form on our future website or by POSTing directly to the API.

### How does it work?
The BrewCenter API is a django rest framework application. We store all of our data in a SQL-based database, and make it available via RESTful endpoints which return JSON data.

## Contributing
Any amount of contribution is welcomed and encouraged. For now, it's just me reviewing PRs. I'd love to get
more people on board, form a review team, and do some really cool stuff. We do have a slack channel for development
support. If you would like to join, please send me an email (see my profile).

I try to review PRs at least within 2 days, if not by the end of the same night.

## Installation
First, download the latest stable release of Python 3.

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
