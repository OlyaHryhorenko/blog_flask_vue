from flask import (Flask, Response, abort, jsonify, redirect, render_template,
                   request, send_file, session, url_for, Markup, make_response, g)
import datetime
import hashlib
import json
import logging
import os
import random
import time
import pytz
import glob
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import string
import requests
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/olga/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    passw = db.Column('pass', db.Unicode)

    def __init__(self, name=None, passw=None):
        self.name = name
        self.passw = passw

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.Unicode)
    text = db.Column('text', db.Unicode)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __init__(self, title=None, text=None, user_id=None):
        self.title = title
        self.text = text
        self.user_id = user_id

    def toDict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


@app.route('/')
def index():
    # admin = User(name='admin3', passw='11112')
    # art = Article(title='admin3', text='11112', user_id=1)
    # db.session.add(admin)
    # db.session.add(art)
    # db.session.commit()
    return render_template('index.html')


@app.route('/api/create-user', methods=['POST'])
def create_user():
    return 'success'


@app.route('/api/create-article', methods=['POST'])
def create_article():
    return 'success'



@app.route('/api/get-users', methods=['GET'])
def get_users():
    users = User.query.all()
    usersArr = []
    for user in users:
        usersArr.append(user.toDict())
    return jsonify(usersArr)



@app.route('/api/get-articles', methods=['GET'])
def get_articles():
    articles = Article.query.all()
    articlesArr = []
    for article in articles:
        articlesArr.append(article.toDict())
    return jsonify(articlesArr)


if __name__ == "__main__":
    app.run(debug=True)
else:
    logging.basicConfig(debug=True, threaded=True,host='0.0.0.0', port=5000)
