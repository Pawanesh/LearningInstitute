# Setup python3 virtual env.
python3 -m venv /Users/pawgupta0/Pawanesh/runenv 

# Activate python3 virtiual env.
source /Users/pawgupta0/Pawanesh/runenv/activate

#Install django
pip install Django==4.0.6

#Install flask
pip install Flask

#Install flask_restful
pip install flask_restful

#Install requests
pip install requests


#Create empty django project
django-admin startproject LIOnline

#Start service
python manage.py runserver

#Create app Registration
python manage.py startapp Registration

#Create app Home
python  manage.py startapp Home


#Export LI_HOME env
export LI_HOME=/Users/pawgupta0/Pawanesh/development/LearningInstitute

#Export LI_RUNTIME
export LI_RUNTIME=/Users/pawgupta0/Pawanesh/runenv

#Export LI_ENV dev, uat, prod
export LI_ENV=dev

#Running sqlite
sqlite3 /Users/pawgupta0/Pawanesh/development/LearningInstitute/Database/sqlite/db/LearningInstitute.sqlite.db 
.tables

.schema Class

ctrl + d -> quit

#Run Online GUI service
./script/runner.sh ./app/OnlineService/LIOnline/manage.py runserver 7000


#Run flask query service
./script/runner.sh ./app/QueryService/QueryService.py