# Recruitement App
> DevOps Core Fundamental Project 
#### Objective: The personal objectives listed below relate directly to the skills listed in the **[ SFIA 7 framework ](https://www.sfia-online.org/en/framework/sfia-7)**
 To create a fully functional CRUD application with utilisation of supporting tools,methodologies and technologies. To work  efficiently by responding to change when need be. To work with DevOps mindesetand by following the four main values and Devolping my Core skills and improve value of my skillset.
 
--- 

### Contents
1. [ Materials ](#Materials)
    1. [ Recruitment Website ](https://34.89.105.159:5000)
    1. [ presentation ](https://docs.google.com/presentation/d/1t09if4lU1a9x9wSj-CRnNaoeSMQIHuru3_VedxZLW-g/edit#slide=id.p)

2. [Execuitve Summary & Critical Review](#execuitve-summary-&-critical-review)
    1. Aim  
    1. Requirments
    1. My Method

3. [Architecture](#Architecture) 
    1. Database Structure - CRD & SQL Tables
    1. CI Pipleline

4. [Project Tracking](#Project-Tracking)

5. [Testing](#Testing)

6. [Front-End Design Walk Through](#Front-End-Desing-Walk-Through)

7. [Conclusion](#conclusion)
    1. Identified Issues
    1. Future Improvments
8. [Reference](#Reference)
9. [license](#Licence)
---
## Materials



[Back to the Top](#Recruitement-App)

---
## Execuitve Summary & Critical Review
The Aim of this Project was to succefully Create an Application Which gives the the user the ability to Create, Read, Update and delete within a Flask Website. 

Bespoke requirements for myself was include a Project Tracking tool, create a databses that shares Relations whitin its tables, provide documentation of all phases, build test suits and intergrate my code into some type of verison control sytsem built by a CI server and depolyed through a virtual machine using a cloud server .

the creation of a crud Application using a micro framework like Flask was great as is provides a huge libary of compents that could be customisation to the speciffication of this Recuitment App. some of which included Flask-Forms which helped with the create functionality of the application and SQLAalchemy which helped me connect my python code to the Recuitment Database. 

## My Aprroach


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



[Back to the Top](#Recruitement-App)

---

## Reference



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

