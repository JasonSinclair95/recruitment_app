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
        app.config.update(RECRUITMENT_VM_DB_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLE=False,
                DEBUG=True
                )
        return app

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()
    
class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible 
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestPosts(TestBase):

    def test_add_new_job_post(self):
        """
        Test that when I add a new post, I am redirected to the homepage with the new post visible
        """
        with self.client:
            response = self.client.post(
                '/jobs_post',
                data=dict(
                    title="Test Title",
                    content="Test Content",
                    job_role='Aws Specialist', 
                    positions='1', 
                    years_of_experience='3', 
                    salary='35000', 
                    address='7 London Road', 
                    postcode='se165p'
                ),
            follow_redirects=True
            )
            self.assertIn(b'Test title', response.data)

class TestAplication(TestBase):
    def test_add_job_application(self):
        """
        Test that when I add a job applicaton, I am redirected to the homepage.
        """
        with self.client:
            response = self.client.post(
                '/jobs_post',
                data=dict(
                    title="Test Title",
                    content="Test Content",
                    job_role='Aws Specialist', 
                    positions='1', 
                    years_of_experience='3', 
                    salary='35000', 
                    address='7 London Road', 
                    postcode='se165p'
                ),
                follow_redirects=True
            )
    