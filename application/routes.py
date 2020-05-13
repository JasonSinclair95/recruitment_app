from application import app
from flask import render_template, redirect, url_for
from application.models import JobPosts
from application.forms import JobPostForm

@app.route('/')
@app.route('/home')
def home():
	postData = JobPosts.query.all() 
	return render_template('home.html', title='Home', Jobs_post=postData) 

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/JobApplication')
def register():
	return render_template('Job_Application.html', title='Job Applications')

@app.route('/JobPostForm', methods=['GET', 'POST'])
def post():
	form = JobPostForm()
	if form.valid_on_submit():
		postData = JobPosts( 
			title=form.title.data,
			positions=form.positions.data,
			years_of_experience=form.years_of_experience.data,
			salary=form.salary.data,
			address=form.address.data,
			postcode=form.postcode.data		
		)
		db.session.add(postData)
		db.session.commit()
		return redirect(url_for('home'))

	else:
		return render_template('Jobpost.html', title='JobPost', form=form)



