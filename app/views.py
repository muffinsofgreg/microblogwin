from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Greg'}
    posts = [  #fake array of posts
        { #posts[0]
            'author': {'nickname': 'Jonny'},
            'body': 'Loving the GFL Office'
        },
        { #posts[1]
            'author': {'nickname': 'Jonny'},
            'body': 'To my homies around town!'
        }
    ]
    return render_template("index.html", title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
