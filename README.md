# Django_Frameworks
## Local Path
`cd ~/Desktop/Django`
## Django web application concept
Django uses the concept of projects and apps to keep code clean and readable. A single Django project contains one or more apps within it that all work together to power a web application. This is why the command for a new Django project is startproject.
### Fixing Projects Destination
`cd ~/Desktop`

`mkdir folder-name-where-your-project-files-will-live`

`cd folder-name-where-your-project-files-will-live` 
### Firing Django
`:~/Desktop/folder-name-where-your-project-files-will-live$ pipenv install django==3.0.1`

`:~/Desktop/folder-name-where-your-project-files-will-live$ pipenv shell`
### Stating Project
`:~/Desktop/folder-name-where-your-project-files-will-live$ django-admin startproject porject-name_project .`

For example, a real-world Django e-commerce site might have one app for userauthentication, another app for payments, and a third app to power item listing details: each focuses on an isolated piece of functionality. That’s three distinct apps that all live within one top-level project.
### Starting an App and its files
`:~/Desktop/folder-name-where-your-project-files-will-live$python3 manage.py startapp appName `

An appName wise folder will be created and in it these files are found-
- admin.py is a configuration file for the built-in Django Admin app
- apps.py is a configuration file for the app itself
- migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync
- models.py is where we define our database models which Django automatically translates into database tables
- tests.py is for our app-specific tests
- views.py is where we handle the request/response logic for our web app

### Tree view
```python
{
	'folder-name-where-your-project-files-will-live' = 'helloworld',
	'appName' = 'pages',
	'porject-name_project' = 'helloworld_project',
}
```

```bash
:~/Desktop/helloworld$ tree
```
```bash
├── db.sqlite3
├── helloworld_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pages
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── Pipfile
└── Pipfile.lock
```
### Things to do after creating an app
open file in ` :~Desktop/helloworld/helloworld_project$ subl setting.py`
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',# Add this line
]
```
new line definition is in `:~Desktop/helloworld/pages$subl apps.py `
```python
from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'
```
### Notes
- Even though  new app pages exists within the Django project, Django doesn’t “know” about it until we explicitly add it in settings.py file and scroll down to INSTALLED_APPS where it is seen six built-in Django apps already there and new pages app need to be added at the bottom.
- Local apps should always be added at the bottom because Django executes the INSTALLED_APPS setting from top to bottom. Therefore the internal admin app is loaded first, then auth, and so on and because We want the core Django apps to be available since it’s quite likely our own apps will rely on their functionality.
- why pages.apps.PagesConfig ? The reason is that Django creates an apps.py file with each new app and it’s possible to add additional information there, especially with the Signals framework which is an advanced technique.

## URLs, Views, Models, Templates
Within an app at least three (often four) separate files are required to power one single page.
The complete flow looks something like this:
### Django request/response cycle
`URL -> View -> Model (typically) -> Template`

## Templates
### Philosophy
Every web framework needs a convenient way to generate HTML files.  
In Django the approach is to use templates ( Templates:individual HTML files that can be linked together and also include basic logic. )
## Heroku (Production publish)
Heroku works with the help of locat git repository. So Each project should have its own git initialization for now. 
```bash
	:~/Desktop/helloworld$git init
	:~/Desktop/helloworld$git add . && git commit -m "gitted all the files"
```
Then the following four changes are needed to our Pages project so it’s ready to deploy online with Heroku:
- update Pipfile.lock
    - to update the Pipfile.lock two process must be followed
        - Withinexisting Pipfile specify the version of Python being used, which is 3.7 . So,add these two lines at the bottom of the file name Pipfile.
	```bash
		:~/Desktop/helloworld$ nano Pipfile
	```
	- Add these two lines in the bottom
	
	```
		[requires]
		python_version = "3.7"
	```
	- then run this command:
	```bash
		:~/Desktop/helloworld$ pipenv lock
	```
- make a new Procfile file
- install Gunicorn as our web server
- make a one-line change to settings.py file

## Introducing the Django Admin
### Philosophy 
Generating admin sites for your staff or clients to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models. 

Django was written in a newsroom environment, with a very clear separation between “content publishers” and the “public” site. Site managers use the system to add news stories, events, sports scores, etc., and that content is displayed on the public site. Django solves the problem of creating a unified interface for site administrators to edit content.

The admin isn’t intended to be used by site visitors. It’s for site managers.
