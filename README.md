# Recruitement App
> DevOps Core Fundamental Project 
#### Objective: The personal objectives listed below relate directly to the skills listed in the **[ SFIA 7 framework ](https://www.sfia-online.org/en/framework/sfia-7)**
 To create a fully functional CRUD application with utilisation of supporting tools, methodologies and technologies. To work efficiently by responding to change when need be. To work with an Agile mindset and by following the four main values of a DevOps Engineer. To Develop my Core skills and improve value in my skillset.
 
--- 

### Materials:
1. [ Recruitment Website ](https://34.89.105.159:5000)

---

### Contents
1. [Executive Summary & Critical Review](#Executive-Summary-&-Critical-Review)
    1. Aim  
    1. My Method
    1. Summary

2. [Architecture](#Architecture) 
    1. Database Structure - CRD & SQL Tables
    1. CI Pipeline

3. [Project Tracking](#Project-Tracking)

4. [Testing](#Testing)

5. [Risk Assessment](#Risk-Assessment)]

6. [Conclusion](#conclusion)
    1. Identified Issues
    1. Future Improvements
7. [Reference](#Reference)
8. [license](#Licence)

---

## Executive Summary & Critical Review
### Aim
The Aim of this Project was to successfully Create an Application Which gives the user the ability to Create, Read, Update and delete within a Flask Website. 

Bespoke requirements for myself was to include a project tracking tool, create a databases that shares relations within its tables, provide documentation of all phases, build test suits and integrate my code into some type of version control system built by a CI server and deployed through a virtual machine using a cloud server.

The creation of a CRUD Application using a micro framework like Flask was great as it provides a huge library of components that could be customised to the specification of this Recruitment App. Some of which include Flask-Forms which helped with the create functionality of the application and SQLAalchemy which helped me connect my python code to the Recruitment Database. 

## My Method
### Recruitment APP
The Recruitment application is a functional display of recruitment in the virtual world. A " "Client" user is able to create a job Post by filling out a form and upon submission that form will be posted on the home page of the website. The update and delete function can also be found on the home page below each post which will alter or remove a job post from the database. Similarly, a 'job seeker' user can click on any job posted on the home page of the website to complete a form and apply for that specific job. 

![](Documents/images/HomePage.png) ![](Documents/images/JobPost.png)![](Documents/images/ApplicationsPage.png)

the application itself is built and run through Jenkins, which with a specific config works as a system disservice.

### Summary 

To summarize a successful, a Front-end and back-end CRUD application was created with a 88% test coverage. project tracking, testing and CI tools was used with the mindset of a DevOps engineer in order to work efficiently and focus on continues deployment. Along with this, risks were identified, and a risk assessment was created to take precaution whilst completing this project. Some issues and improvements have been stated in the conclusion section.

[Back to the Top](#Recruitment-App)

---

## Architecture 

### DataBase Structure

Illustrated below is four tables of which I planned to include in my project within one Database. Although only two was implemented the relationship between each table can be seen using the relevant connections and foreign/primary keys. 

![](Documents/images/CRD.png)

like stated above, only two tables was implemented "JobAplications" and "JobPosts".  A job post can have 0 to many Applications for it however a application can be from only one job roll posted. The application table depends on a job to be posted and makes use of the Primary Key "job_id" in order for the user to identify which job they are applying for. Modelled below is the specification Created in Google SQL.

![](Documents/images/SQL.png)

Each type of Column is set specifically for each variable in the table. the Job_id seen in the JobPosts Table is the foreign key in the JobApllications table and is also auto incremented. All variables in the table must contain data to be submitted otherwise an error will be displayed. For example, in the JobPosts table the salary cant contain more than 11 integers or the address cant contain more than 100 characters. below is what an error would look like on the website if an entry is not completed. Otherwise click [here](application/routes.py) to see the source code.

![](Documents/AppError.png)

### CI Pipeline
 

![](Documents/images/CiPipeline.png)

to elaborate on some of the technologies used in the CI pipeline is as follows:
* GCP - to create the virtual environment and also set up the foundation of our Databases using MySQL.
* VS Code/Python - is an interpreter which allows better visualisation when building the flask application using python, in comparison to coding using google ssh. 
* Trello board to keep track of the project progress.
* GitHub: allows the source code to be stored and also webhooks are created which trigger the Ci server to build/run the application.
* PyTest to test the application and produce a coverage report. 

[Back to the Top](#Recruitment-App)

---
## Project Tracking

This board was used to highlight the user stories/tasks and keep the development of the project on track. the MOSCOW principle was applied by colour coding what must be done (red), should be done (green), could be done (blue) and would be done (yellow). Following a DevOps mindset and agile methodology the User Stories can be seen to the far left. from this the sprint and backlog was created and sorted in terms of priority using the MOSCOW principle. All task with a red label must have been complete for the CRUD Application to be successful. Below is the progress of the Trello board half way through the project.

![](Documents/images/TrelloInProgress.png)

As you can see most of the should haves, have not been complete nor tested. throughout the project more task was inputted, and the completed version can be seen below. 

![](Documents/images/TrelloCompleted.png)

in conclusion all should haves had been met, however unfortunately some task was still in progress like testing. This could have perhaps helped identify more bugs in the application however more time should be given for this task in the future. 

[Back to the Top](#Recruitment-App)

---
## Testing

![](Documents/images/PytestCov.png)

Illustrated above is pytests coverage results for the application. the main priority is that all the major CRUD function and the URL links work so that at least data can be collected. If a function is executed, then the output should be known. All forms created was 100% tested, the models file which contains the structure of the databases was 92% tested and finally the routs.py file which is where all functions was defined was 71% tested. A total of 88% coverage was achieved. 

![](Documents/images/CreateTest.png)

The create functions above was tested by the following:
* a user can create a job post and directed back to the home page when submitted. on the home page they should be able to visualise the post which had been created.
* a user can create an application for a job which is then stored in a database. 

![](Documents/images/UpdateDeleteTest.png)

the update and delete functions above were tested by the following
* using the test base setup, the delete function when executed will remove an entry in the database. python will then count how much entries there are currently and if the result is correct the test will have passed.
* the update function will change a variable in the default jobs created within the test base setup. If that variable is now found pytest will have passed.

[Back to the Top](#Recruitment-App)

---

## Risk Assessment
The Risk assessment below contains some of the possible risks when creating an application during this cohort. The likelihood of the risk are scored using a colour code and given a number. red be very high risk, orange being high risk and yellow being moderately low risk. An overall score for each risk can be found in the last column.

![](Documents/images/RiskAssesmentIntial.png)

### Risk Assessment revisited

![](Documents/images/RiskAssessment.png)

the risk assessment was updated throughout out the project because of the exposure of new risk that could possibly occur. a column was then added "Severity of the risk to take into consideration how severe it the risk could impact your work. this parameter was then included n the overall risk score. to view the whole risk assessment click [here](#Documents/RiskAssessment.xlsx) 

[Back to the Top](#Recruitment-App)

---

## Conclusion

In conclusion, I followed the requirement that set on my Kanban Board and work with the MVP concept which resulted in a creating a successful CRUD. Users are able to create a job and an Application, update a Job Post Delete a job Post and Visualise/Read all Posts made on the homepage. risks were identified along with clear documentation of the architecture in this application. Using Visual Code and python to build my application was very efficient as python is very easy to understand at a beginner’s level and Vs code allowed me to build my application more efficiently compared to the GCP SSH. I now have a clear understanding how to use Flask, code in python and automate the process using a CI server for system disservice.

### Identified Issues
Due to a successful CRUD application being created there were not many issues established. however with the testing coverage being only 88%, perhaps some issues were not seen. Regardless some of the main issues faced whilst creating this crud application are as follows:

* Gunicorn unable to work with Jenkins. This was a result of Jenkins being unable to run the gunicorn command to run my app. one possible solution to this could be to create a new VM then set up Jenkins again. 

### Future Improvements
in conclusion to the identified issues, the improvements to be made to the application would be as follows:
* Run my app through a WSGI, to give the server a set of rules to abide by in order for the server to be compatible with any framework that use it. this will allow my app to run on a production deployment server. over all if the traffic coming into my website faces some errors using the application, a internal server error will be displayed rather than the problem that’s going on in the back end of my application. this could be done by installing a program like Gunicorn or Django.
* Create a Login function so that the functionality of my website is enhanced. with this function I can create more relationships between my tables, include a more bespoke service for the users and also improve my learning using flask. this could have been done by installing Flask login and importing login manager. Also including another tab on my home page, setting up a new form along with a root for that function and creating another table in the SQL.
* completed 100% Converge in my testing suit using pytest so that the website can be said to be truly reliable and depilated of bugs. I would do this by testing all areas of the website and not just the major areas. 
* Automated my Testing so that my project is more efficient. this can be done by inputting testing commands into the Jenkins config.
* Applied Integration Testing to the application. this will test how all the different functionalitys of my website work together. this will improve the accuracy of my tests and overall increase the reliability of the website. I would have done this by importing unnittest and all the dependencies.


---