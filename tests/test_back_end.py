import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import JobApplications, JobPosts
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app
    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        job1 = JobPosts(
            job_role='Aws Specialist', 
            positions='1', 
            years_of_experience='3', 
            salary='35000', 
            address='7 London Road', 
            postcode='se165p' 
        )
        job2 = JobPosts(
            job_role='Devops Eningeer', 
            positions='1', 
            years_of_experience='4', 
            salary='55000', 
            address='7 London Road', 
            postcode='se165p' 
        )
        db.session.add(job1)
        db.session.add(job2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_view(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):
    def test_add_new_job_post(self):
        with self.client:
            response = self.client.post(
                '/JobPostForm',
                data=dict(
                    job_role='Test', 
                    positions='1', 
                    years_of_experience='3', 
                    salary='35000', 
                    address='7 London Road', 
                    postcode='se165p'
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test', response.data)

class TestAplication(TestBase):
    def test_add_job_application(self):
        with self.client:
            response = self.client.post(
                '/job_application/1/',
                data=dict(
                    first_name="test name",
                    last_name="Test last name",
                    email='test email', 
                ),
                follow_redirects=True
            )
            count = JobApplications.query.count()
            self.assertEquals(count, 1)

class TestRoutes(TestBase):
    def test_update(self):
        with self.client:
            response = self.client.post(
                '/UpdateJobPost/1/?',
                data=dict(
                    salary="50000"
                ),
                follow_redirects=True
            )
            self.assertIn(b'50000', response.data)
 
    def test_delete(self):
        with self.client:
            response = self.client.post(
                '/Delete/1/JobPost/',
                follow_redirects=True
            )
            count = JobPosts.query.count()
            self.assertEquals(count, 1)
