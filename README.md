# Install flask server on an Ubuntu intance

1. Install python 
1. Install pip
1. Install Goose. On Ubuntu: **pip install goose-extractor**
1. Install Flask on Ubuntu: https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
1. **sudo python /var/www/flaskapp/flaskapp/__init__.py**
1. Make a request. Here's an example: http://127.0.0.1:5000/api?url=http://www.bbc.com/news/world-us-canada-41134799



# Install flask server locally (Mac)
1. Install python
1. Install pip
1. Install Goose
1. Install Flask
1. Create a Flask server
1. cd to the folder where the flask python file apiServer.py is
1. $ export FLASK_DEBUG=1
1. $ export FLASK_APP=apiServer.py
1. $ flask run
1. Make a request. Here's an example: http://127.0.0.1:5000/api?url=http://www.bbc.com/news/world-us-canada-41134799


# Setup serverapi to run on boot
https://github.com/3adel/TextAnalyzer-API/blob/master/apiserver/How%20To%20Serve%20Flask%20Applications%20with%20uWSGI%20and%20Nginx%20on%20Ubuntu%2016.04%20%7C%20DigitalOcean.pdf

# Some useful links
* http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
* Virual environments on mac: http://docs.python-guide.org/en/latest/dev/virtualenvs/

