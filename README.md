# Projects
## Notable REST API projects by me
** (Medi_Project)JWT Token authentication multiple stakeholders like Doctor and Paitent authentication is same project**<https://github.com/19mddil/Django-and-Django-API-project-Source-codes/tree/master/api_projects/Medi_Project/jwt_authen_project/backend>   
** (Medi_Project)django rest-auth Token authentication multiple stakeholders like Doctor and Paitent authentication is same project**<https://github.com/19mddil/Django-and-Django-API-project-Source-codes/tree/master/api_projects/Medi_Project/rest_auth_project/backend>  
** (BloggerAPI) CRUD API project **<https://github.com/19mddil/Django-and-Django-API-project-Source-codes/tree/master/api_projects/blogapi>
## Notable Django project  

** (Newspaper) application with authorization,authentication,crud ** <https://github.com/19mddil/Django-and-Django-API-project-Source-codes/tree/master/demo_projects/news>



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


