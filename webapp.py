from flask import Flask
from flask import render_template
from model import *
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
from flask import session as login_session
from flask import Flask, url_for, flash, redirect, request
ID = None

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


engine = create_engine('sqlite:///webdata.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS







@app.route('/', methods = ['GET','SET'])
def main_page_html():
	return render_template('main_page.html')





@app.route('/welcome')
def welcome_html():
	return render_template('welcome.html')




@app.route('/sign_up')
def sign_up_html():
	return render_template('sign_up.html')



@app.route('/logged_in/people', methods=['GET','POST'])
def people_html():
	people = session.query(User).all()



	return render_template('people.html', people = people)




@app.route('/logged_in/people/find_people')
def find_people_html():
	return render_template('find_people.html')






@app.route('/logged_in')
def logged_in_html():
	return render_template('logged_in.html')




@app.route('/logged_in/groups')
def groups_html():
	groups = session.query(Group).all()


	return render_template('groups.html', groups=groups)





@app.route('/logged_in/groups/new_group')
def new_group_html():
	return render_template('new_group.html')



@app.route('/about_us')
def about_us_html():
	return render_template('about_us.html')




@app.route('/the_team')
def the_team_html():
	return render_template('the_team.html')



if __name__=='__main__':
	app.run(debug=True)
	
