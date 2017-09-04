# TextAnalyzer-API

1. Install python
2. Install pip
3. Install Goose. On Ubuntu: pip install goose-extractor
4. Install Flask. https://www.fullstackpython.com/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html
5. Create a Flask server
6. cd to the folder where the flask python file apiServer.py is
7. $ export FLASK_DEBUG=1
8. $ export FLASK_APP=apiServer.py
9. $ flask run or on Ubuntu gunicorn proxy:app
10. Make a request. Here's an example: http://127.0.0.1:5000/api?url=http://www.bbc.com/news/world-us-canada-41134799



Some useful links
http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
