# BrewCenterAPI

## Please Hold All Development
For the time being, please hold off on any and all BrewCenter development. I'm in the midst of doing a redesign before progress goes too far. In particular, I'm working on refactoring the overall architecture to offer better support for a service-oriented architecture of a suite of tools. Other improvements will include stronger authentication and authorization mechanisms, and introducing GraphQL as the main method of using data. 

### What the heck is a BrewCenter API?
The BrewCenter API is an open source and free-to-use API for sharing brewing related data. Using this API, brewgrammers (brewing programmers) can share scientific specifications for fermentables, hops, yeast, and other pertinent information for the creating of brewing related apps!
The aim of this project is not to make a product for the average homebrewer, but rather to make a product for the experienced brewgrammer. This API will allow people to fetch all of its data. This data can then be used in other brewing applications to populate fields and choices with values that the community agrees are correct.

### Where's the data come from?
This data set will largely be crowdsourced, with some initial seed data inserted when it launches. Users of the API will be able to suggest improvements to the dataset via a web form on our future website or by POSTing directly to the API.

### How does it work?
The BrewCenter API is a django rest framework application. We store all of our data in a SQL-based database, and make it available via RESTful endpoints which return JSON data.

## Contributing

### Communication
Building brewing software is hard and complicated. It's a confusing domain to work in when you get down to the science of how ingredients affect the outcome. To make this web service as good as possible, we need to actively communicate. I strongly encourage anyone interested in working on this project to join the slack team. Email me, [Michael Washburn Jr](https://github.com/MichaelWashburnJr) for an invite. My email can be found [on my github profile](https://github.com/MichaelWashburnJr).

### Getting Started

If you're interested in working on the BrewCenterAPI, you can start by digging through the issues and searching for ones with the "Beginner" label. Furthermore, there's always several beginner tasks that are constantly in need of being done which aren't in the issues. Here are some examples of great tasks you can do to get started: pull the repo and run the tests, run the code through a linter like [pylint](https://www.pylint.org/) and fix the errors, write additional unit tests, write API level tests (HTTP requests hitting the endpoints), add comments to confusing code after you think you understand it, look for duplicate code and extract it into a common function/class. 

### PRs
I try to review PRs at least within 2 days. I will try my best to thoroughly review PRs and leave good feedback. I always test the PRs before merging. If you want your PR to be merged in fast, please make sure to do the following:

1. Run the unit tests
2. Write unit tests for functionality you introduced
3. Run your code through a linter like `pylint`
4. Thoroughly test your PR
5. Make sure your PR is up-to-date with master.

I will help you along the way by offering feedback. I will not, however, take half-completed PRs and finish them myself. The PR is yours and yours alone. If it goes without being worked for 20 days or so, it will be closed without merging.

## Installation
First, download the latest stable release of Python 3.

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

## Testing
To run the tests, `cd` to the same directory as the `manage.py` file, then run `python manage.py test brew_data.tests`.
