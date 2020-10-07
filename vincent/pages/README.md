# Deploying Django to heroku

Single Project should have single git tracker.For example: suppose having this project tree,
```bash
:~/Desktop/pages$ tree

├── db.sqlite3
├── manage.py
├── pages
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── static
│   │   └── pages
│   │       └── style.css
│   ├── templates
│   │   ├── about.html
│   │   ├── base.html
│   │   └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pages_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Pipfile
├── Pipfile.lock
└── Procfile

```
Now step by step follow following commands:
```bash
:~/Desktop/pages$ pipenv shell
:~/Desktop/pages$ git status
:~/Desktop/pages$ git init
:~/Desktop/pages$ git add .
:~/Desktop/pages$ git commit -m "Preparing to launch to github"
:~/Desktop/pages$ touch README.md
:~/Desktop/pages$ git add .
:~/Desktop/pages$ git commit -m "Added a README file"
:~/Desktop/pages$ heroku login
```
Now,
- update Pipfile.lock, to do this
    - open pipfile and insert these lines in the end
    ```
    	[requires]
		python_version = "3.7"
    ```
    - run 
    ```bash
    	(pages) $ pipenv lock
    ```
- create a Procfile , which is configuration file specific to Heroku
```bash
	:~/Desktop/pages$: touch Procfile
```
Now add this line `web: gunicorn pages_project.wsgi --log-file -`
Now follow through:
```bash
(pages) $ pipenv install gunicorn==19.9.0

```

