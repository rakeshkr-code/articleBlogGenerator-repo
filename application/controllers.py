from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.models import Article
from application.utilities import *


@app.route('/', methods=['GET', 'POST'])
def articles():
    articles = Article.query.all()
    v = render_template("articles.html", articles=articles)
    return v


@app.route('/article_by/<user_name>', methods=['GET', 'POST'])
def article_by_author(user_name):
    articles = Article.query.filter(Article.authors.any(username=user_name))
    v = render_template("article_by_author.html", articles=articles, user_name=user_name)
    return v
