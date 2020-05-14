from application import db
from datetime import datetime
from sqlalchemy import ForeignKey

class JobApplications(db.Model):
	__tablename__ = 'JobApplication'
	application_id = db.Column(db.Integer, primary_key=True)
	Job_id = db.Column(db.Integer, db.ForeignKey('JobPosts.Job_id'))
	first_name = db.Column(db.String(100), nullable=False, unique=False)
	last_name =  db.Column(db.String(100), nullable=False, unique=False)
	email =  db.Column(db.String(100), nullable=False, unique=False)
	date_applied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	def __repr__(self):
		return ''.join([
			"application", self.application_id, ' ', self.Job_id, ' ', self.Job_id, '\r\n',
			"user ", self.first_name, ' ', self.last_name
		])

class JobPosts(db.Model):
	__tablename__ = 'JobPosts'
	Job_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=False)
	positions = db.Column(db.Integer, nullable=False)
	years_of_experience = db.Column(db.Integer, nullable=False)
	salary = db.Column(db.Integer, nullable=False)
	address = db.Column(db.String(100), nullable=False, unique=False)
	postcode = db.Column(db.String(15), nullable=False, unique=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	JobApplication = db.relationship('JobApplications', backref='Job-id', lazy=True)

	def __repr__(self):
		return ''.join([
			'Job Role: ', self.Job_id, ' ', self.title, ' ', '\r\n',
			'Job Description: ', self.positions, ' ', self.Years_of_experience, ' ', self.salary, '\r\n', 
			'Address: ', self.address, ' ', self.postcode, '\r\n',
            	])
