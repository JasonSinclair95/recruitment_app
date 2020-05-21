from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ApplicationsForm(FlaskForm):
    first_name = StringField('first Name',
            validators = [
                DataRequired(),
                Length(min=3, max=60)
            ]
    )
                
    last_name = StringField('Last name',
            validators = [
                DataRequired(),
                Length(min=4, max=60)
            ]
    )  
                
    email = StringField('Email Address',
            validators = [
                DataRequired(),
                Length(min=4, max=60)
            ]
    )
    submit = SubmitField('submit application')

    
class JobPostForm(FlaskForm):
    job_role = StringField('Job title/role',
            validators = [
                DataRequired(),
                Length(min=4, max=60)
            ]
    )

    positions = StringField('positions',
            validators = [
                DataRequired(),
                Length(min=1, max=4)
            ]
    )

    years_of_experience = StringField('how many years of experience',
            validators = [
                DataRequired(),
                Length(min=1, max=5)
            ]
    )

    salary = StringField('annual salary of position',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]	
    )

    address = StringField('address of location',
            validators = [
                DataRequired(),
                Length(min=7, max=100)
            ]
    )

    postcode = StringField('postcode of location',
            validators = [
                DataRequired(),
                Length(min=6, max=10)
            ]
    )

    submit = SubmitField('Post Job')

class UpdateJobPostForm(FlaskForm):
    job_role = StringField('Job title/role',
            validators = [
                DataRequired(),
                Length(min=4, max=60)
            ]
    )

    positions = StringField('positions',
            validators = [
                DataRequired(),
                Length(min=1, max=4)
            ]
    )

    years_of_experience = StringField('how many years of experience',
            validators = [
                DataRequired(),
                Length(min=1, max=5)
            ]
    )

    salary = StringField('annual salary of position',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]	
    )

    address = StringField('address of location',
            validators = [
                DataRequired(),
                Length(min=7, max=100)
            ]
    )

    postcode = StringField('postcode of location',
            validators = [
                DataRequired(),
                Length(min=6, max=10)
            ]
    )
    submit = SubmitField('Update job post')

