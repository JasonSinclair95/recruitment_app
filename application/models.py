from application import db

class JobApplications(db.Model):
	application_id = db.Column(db.Integer, primary_key=True)
	def __repr__(self):
		return ''.join([
			self.application_id
		])

class JobPosts(db.Model):
	Job_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=False)
	positions = db.Column(db.Integer, nullable=False)
	Years_of_experience = db.Column(db.Integer, nullable=False)
	salary = db.Column(db.Integer, nullable=False)
	address = db.Column(db.String(100), nullable=False, unique=False)
	postcode = db.Column(db.String(15), nullable=False, unique=False)

	def __repr__(self):
		return ''.join([
			'Job Role: ', self.Job_id, ' ', self.title, ' ', '\r\n',
			'Job Description: ', self.positions, ' ', self.Years_of_experience, ' ', self.salary, '\r\n', 
			'Address: ', self.address, ' ', self.postcode
            	])
