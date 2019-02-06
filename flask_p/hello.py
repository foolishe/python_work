from flask import Flask, render_template,session,redirect,url_for,flash
from flask import request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate,MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:12345678@localhost:3306dd/tysql'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

from flask_mail import Message
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasy Admin <flasky@example.com>'

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
        sender = app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    mail.send(msg+)



db = SQLAlchemy(app)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
bootstrap = Bootstrap(app)
moment = Moment(app)
migrate = Migrate(app,db)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

class NameForm(Form):
    name = StringField('what is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
     form = NameForm()
     if form.validate_on_submit():
         old_name = session.get('name')
         if old_name is not None and old_name != form.name.data:
             flash('Looks like you have changed your name!')
         session['name'] = form.name.data
         return redirect(url_for('index'))
     return render_template('index.html',
        current_time=datetime.utcnow(),form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__ == '__main__':
    manager.run()
