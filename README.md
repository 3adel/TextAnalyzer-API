# TextAnalyzer-API

1. Install python 
1. Install pip
1. Install Goose. On Ubuntu: **pip install goose-extractor**
1. Install Flask on Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
1. cd to the folder where the flask python file apiServer.py is
1. $ export FLASK_DEBUG=1
1. $ export FLASK_APP=apiServer.py
1. $ flask run or on Ubuntu gunicorn proxy:app
1. Make a request. Here's an example: http://127.0.0.1:5000/api?url=http://www.bbc.com/news/world-us-canada-41134799



Some useful links
http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application



The app is currently on /var/www/proxy/proxy, to run it, gunicorn proxy:app
