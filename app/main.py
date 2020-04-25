#!../venv/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login
app = Flask(__name__)

app.config['SECRET_KEY'] = '196e40bf26441892bd1b5ffc1093acfec6d55b73'

posts = [
    {
        'autor': 'Aleksandr Tolstoy',
        'title': 'First blog post',
        'content': 'First post content',
        'date': 'April 22, 2020'

    },

    {
        'autor': 'Aleksey Redka',
        'title': 'Second blog post',
        'content': 'Second post content',
        'date': 'April 23, 2020'

    }
]


@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
