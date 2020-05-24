# Recruitement App
> DevOps Core Fundamental Project 
#### Objective: The personal objectives listed below relate directly to the skills listed in the **[ SFIA 7 framework ](https://www.sfia-online.org/en/framework/sfia-7)**
 To create a fully functional CRUD application with utilisation of supporting tools,methodologies and technologies. To work  efficiently by responding to change when need be. To work with DevOps mindesetand by following the four main values and Devolping my Core skills and improve value of my skillset.
 
--- 

### Materials:
1. [ Recruitment Website ](https://34.89.105.159:5000)
2. [ presentation ](https://docs.google.com/presentation/d/1t09if4lU1a9x9wSj-CRnNaoeSMQIHuru3_VedxZLW-g/edit#slide=id.p)

---

### Contents
1. [Execuitve Summary & Critical Review](#execuitve-summary-&-critical-review)
    1. Aim  
    1. My Method
    1. Summary

2. [Architecture](#Architecture) 
    1. Database Structure - CRD & SQL Tables
    1. CI Pipleline

3. [Project Tracking](#Project-Tracking)

4. [Testing](#Testing)

5. [Front-End Design Walk Through](#Front-End-Desing-Walk-Through)

6. [Conclusion](#conclusion)
    1. Identified Issues
    1. Future Improvments
7. [Reference](#Reference)
8. [license](#Licence)

---

## Execuitve Summary & Critical Review
### Aim
The Aim of this Project was to succefully Create an Application Which gives the the user the ability to Create, Read, Update and delete within a Flask Website. 

Bespoke requirements for myself was include a Project Tracking tool, create a databses that shares Relations whitin its tables, provide documentation of all phases, build test suits and intergrate my code into some type of verison control sytsem built by a CI server and depolyed through a virtual machine using a cloud server .

the creation of a crud Application using a micro framework like Flask was great as is provides a huge libary of compents that could be customisation to the speciffication of this Recuitment App. some of which included Flask-Forms which helped with the create functionality of the application and SQLAalchemy which helped me connect my python code to the Recuitment Database. 

## My Aprroach
### Recuitment APP
the Recruitemnt application is a functional display of recuitment in the virual world. a " "Client" User is able to create a job Post by fillng out a Form and upon submisson that form will be posted on the home page of the Website. Similaly a 'job seeker' user can click on any job posted on the home page of the webiste to complete a form and apply for that specifif job. the source code for both forms can be seen below

### picture of forms


notice how the the job_id was not a varible in these. like spokenn of above in th SQL table this key is Auto Incrimentented. the sorurce code which specifys actley which job the applicant is applying for can be found by clicking the[link](github homehtml)

the update and delted function can also be found of the home page which will alter or remove JobPost from the database.


### Summary 


[Back to the Top](#Recruitement-App)

---
## Architecture 

### DataBase Structure

Isluatrated below is four tables of which i planned to include in my project within one Database. Although only Two was implemented the relationship between each table can be seen using the relevent connections and foreign/primary Keys. 

####CRD

like stated aboove, overall only two tables was implemented "JobAplications" and "JobPosts".  A jobPost can have 0 to many Apllications for it, and a application can be from only one job roll posted. the application table depends on a Job to be Posted and makes use of the Primary Key "job_id" iorder for the user to identuify which job they are applying for. Modelled below is the CRD and the specification Created in Google SQL.


####CRD for Two and Screenshot of SQL DataBAse

###CIP Piplie





[Back to the Top](#Recruitement-App)

---
## Project Tracking



[Back to the Top](#Recruitement-App)

---
## Testing



[Back to the Top](#Recruitement-App)

---

## Front-End Desing Walk Through



[Back to the Top](#Recruitement-App)

---

## Conclusion


### Identified Issues
Due to a succseful CRUD application thier were not many issues established. however due tot he tesing coverage being only 88%, perhaps some issuse were not seen. Regarldess some of the main issues faced whilst creating this crud application are as follows:
* Gunicorn unable to work with jenkins. this was a result of jenkins being unable to run the gunicorn command to run my app. one possible sollution to this could be to create a new VM then set up jenkins again. 



### Future Improvmments
in conclsusion to the identified issuses, the improvment to be made to the application would be as follows:
* Run my app thoruhg a WSGI, to give the sevrer a set of rules to abide by inorder for the server to be compatioable with any framework that use it. this will allow my app to run on a production deployment server. over all if the traffic coming into my website faces some erros using the aplication, a internal servor error will be dsiplayed rather than the problem thats going on in the back end of my application. this could be done by instaling a program like Gunicorn or Django.
* Create a Login funtion so that the functionalatity of my webiste is enhanced. with this function i would have be able to create more relatonships between my databses, include a more bespoke service for the users and also improve my learning using flask. this could have been done by instaling Flask_login and iporting login manager. Also including another tab on my home page, setting up a new form along with a root for that function and creating another table in the SQL.
* completed 100% Coverge in my testing suit using pytest so that the website can be said to be turly reaible and deplieted of bugs. i would do this by testing all areas of the website and not just the major areas. 
* Automated my Testing so that my project is more efficent. this can be done by inputing tesing commands into the jenkins config.
* Applied Integration Testing to the application. this will test how all the diffrent funcrtionality of my website work together. this will improve the accracy of my tests and overl increase the realibilty of the webisite. i would have done this by importing unnittest and all the dependencies.


[Back to the Top](#Recruitement-App)

---

## Reference

* [Ivory.idyll.org. 2020.](#http://ivory.idyll.org/articles/wsgi-intro/what-is-wsgi.html)
* [Flask-sqlalchemy.palletsprojects.com. 2020.](#https://flask-sqlalchemy.palletsprojects.com/en/2.x/)


[Back to the Top](#Recruitement-App)

---

## License

MIT License

Copyright (c) 2020 JasonSinclair95

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back to the Top](#Recruitement-App)

