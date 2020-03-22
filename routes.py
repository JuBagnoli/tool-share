from application import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from application.forms import ToolForm, RegistrationForm
from application.models import Tools, Users

@app.route('/')
@app.route('/home')
def home():
	postData = Tools.query.all()
	return render_template('home.html', title='our project', toolData=toolData)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
	return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hash_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
		first_name=form.first_name.data,
		last_name=form.last_name.data,
		email=form.email.data,
		password=hash_pw
		)

	db.session.add(user)
	db.session.commit()
	return redirect(url_for('post'))
	return render_template('register.html', title='Register', form=form)

@app.route('/about')
	def about():
	return render_template('about.html', title='Why we do what we do')

@app.route('/tools', methods=['GET', 'POST'])
def tools():
	form = ToolForm()
	if form.validate_on_submit():
		toolData = Tools(
		first_name = form.first_name.data,
            	last_name = form.last_name.data,
            	title = form.title.data,
            	content = form.content.data
        	)
        db.session.add(toolData)
        db.session.commit()
        return redirect(url_for('home'))
	
	else:
        print(form.errors)

	toolData = Tools.query.all()
	return render_template('tool.html', title='Tools', form=form)
