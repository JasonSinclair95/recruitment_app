from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import JobPosts
from application.forms import JobPostForm, ApplicationsForm

@app.route('/')
@app.route('/home')
def home():
	postData = JobPosts.query.all() 
	return render_template('home.html', title='Home', Jobs_post=postData) 

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/JobApplication')
def job_application():
	form = ApplicationsForm()
	if form.validate_on_submit():
		postData = JobApplications( 
			job_id=form.job_id.data,
			first_name=(form.first_name.data),
			last_name=(form.last_name.data),
			email=(form.email.data),	
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('job_application.html', title='Job Applications', form=form)

@app.route('/JobPostForm', methods=['GET', 'POST'])
def post():
	form = JobPostForm()
	if form.validate_on_submit():
		postData = JobPosts( 
			title=form.title.data,
			positions=int(form.positions.data),
			years_of_experience=int(form.years_of_experience.data),
			salary=int(form.salary.data),
			address=form.address.data,
			postcode=form.postcode.data		
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('jobs_post.html', title='JobPost', form=form)

