from application import db

class (db.Model):
	application_id = db.Column(db.Integer, primary_key=True)
	Job_id = db.Column(db.Integer, foreign_key=True)
  	date_applied = db.Column(, nullable=False)
    
    def __repr__(self):
        return ''.join([
            'User: ', self.first_name, ' ', self.last_name, '\r\n',
            'Title: ', self.title, '\r\n', self.content
        ])

