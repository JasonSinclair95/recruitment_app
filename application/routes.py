from application import app, db
from flask import render_template, redirect, url_for, request
from application.models import JobPosts, JobApplications
from application.forms import JobPostForm, ApplicationsForm, UpdateJobPostForm

@app.route('/')
@app.route('/home')
def home():
	postData = JobPosts.query.all() 
	return render_template('home.html', title='Home', Jobs_post=postData) 

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/JobPostForm', methods=['GET', 'POST'])
def post():
	form = JobPostForm()
	job_Data = None
	if form.validate_on_submit():
			job_Data = JobPosts( 
			job_role=form.job_role.data,
			positions=int(form.positions.data),
			years_of_experience=int(form.years_of_experience.data),
			salary=int(form.salary.data),
			address=form.address.data,
			postcode=form.postcode.data)
			db.session.add(job_Data)
			db.session.commit()
			return redirect(url_for('home'))
	else:
		print(form.errors)
	return render_template('jobs_post.html', title='JobPost', form=form, job=job_Data)

@app.route('/UpdateJobPost/<id>/', methods=['GET','POST'])
def UpdateJobPost(id):
	form = UpdateJobPostForm()
	getPost = JobPosts.query.filter_by(Job_id=id).first()

	if form.validate_on_submit():
		getPost.job_role = form.job_role.data
		getPost.positions = int(form.positions.data)
		getPost.years_of_experience = int(form.years_of_experience.data)
		getPost.salary = int(form.salary.data)
		getPost.address = form.address.data
		getPost.postcode = form.postcode.data

		db.session.commit()
		return redirect(url_for('home'))
	elif request.method == 'GET':
		form.job_role.data = getPost.job_role
		form.positions.data = int(getPost.positions)
		form.years_of_experience.data = int(getPost.years_of_experience)
		form.salary.data = int(getPost.salary)
		form.address.data = getPost.address
		form.postcode.data = getPost.postcode
	return render_template('jobs_post.html', title='JobPost', form=form, post=getPost)

@app.route('/job_application/<id>/', methods=['GET','POST'])
def job_application(id):
	form = ApplicationsForm()
	getPost = JobPosts.query.filter_by(Job_id=id).first()
	
	if form.validate_on_submit():
		postData = JobApplications( 
			Job_id=id,
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

@app.route('/Delete/<id>/JobPost/', methods=['GET','POST'])
def DeleteJobPost(id):
	job_post = JobPosts.query.filter_by(Job_id=id).first()
	application = JobApplications.query.filter_by(Job_id=id).all()
	alljob = JobApplications.query.all()
	for post in alljob:
		db.session.delete(post)
	db.session.delete(job_post)
	db.session.commit()
	return redirect(url_for('post'))


