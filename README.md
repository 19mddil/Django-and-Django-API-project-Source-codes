# Running projects locally
First clone the repo 
```bash
username@device-name:~/Desktop$ git clone https://github.com/19mddil/Django_Framework.git
```
Then navigate any projects you prefer and see if there is manage.py in director list view,
```bash
username@device-name:~/Desktop/Django_Framework-master/Django_Framework-master/demo_projects/news$ ls
articles  db.sqlite3  manage.py  newspaper_project  pages  Pipfile  Pipfile.lock  Procfile  requirements.txt  users
```
For some projects you can run only
```bash
python3 manage.py migrate
python3 manage.py runserver
```
But if that dont work,run following commands
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install pipenv
cp ~/Desktop/Django_Framework-master/Django_Framework-master/requirements.txt .
pipenv install -r requirements.txt
```
Now run
```bash
python3 manage.py migrate
python3 manage.py runerver
```


Happy coding:).


