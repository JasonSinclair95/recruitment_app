from application import db
from application.models import JobApplications 
from application.models import JobPosts

db.drop_all()
db.create_all()
