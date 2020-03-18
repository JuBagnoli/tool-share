

Brief

    Solution

Architecture

    Entity Relationship Diagrams
    Multi Tier Architechture Diagram

Testing

    Report

Deployment

    Technologies Used

Front End Design

Improvements for the Future

Authors

Acknowledgements

**tool-share**  
_My app is a community resource which allows users to share neighbours tools._  

**Assessment Objective**  
_To individually create a CRUD application which uses core tools, methodologies and technologies covered by the GMCA DevOps course. These include Agile, Continuous Integration, Cloud Fundamentals and software development languages/operating systems including Linux, Python & Flask._

**Assessment Tech Stack Scope**  
_a Minimum Viable Product which covers_   
**1. KANBAN BOARD** using [this Trello Board](https://trello.com/b/oqz3rjmG/assessment) containing user stories, use cases, tasks including task backlog and Moscow analysis.  
**2. DATABASE**: GCP Mysql relational database 'tool-share' with three tables; Users, Tools & Users_toolbox.  
**3. CRUD APPLICATION BACK-END** in Python programming language, saved as a Git Repository.  
**4. FRONT-END & INTEGRATED APPLICATION PROGRAMMING INTERFACE(API)** using Flask HTML.  
**5. UNIT TESTING ENVIRONMENT(TDD)** using Pytest. Proof of high test coverage using test reports.  
**6. VERSION CONTROL SYSTEM(VCS)** using code fully integrated into the GitHub Version Control System using the Feature-Branch model.  
**7. CONTINUOUS INTEGRATION(CI) SERVER** using Jenkins.  
**8. ERG DIAGRAM** using draw.io.  
**9. Risk Assessment**.  

**Use Case**  
_The sharing economy is much vaunted with privately owned assets using web apps to timeshare resources (eg: AirBnB,Carshare, Storage). This application will allow users to benefit their local community and themselves by pooling their gardening, DIY, cooking equipment)_  

**Deadline**  
Latest Github commit on 9am Monday 23rd March 2020.    The Brief

To create an OOP-based application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training. The application must manipulate two tables with full CRUD functionality.

Solution

I decided to create a personal yoga application that would allow the user to create poses and routines, as well as add and remove poses from each routine.

The many to many relationship between poses and routines is working, where poses can be added and removed from routines.

Architecture

Entity Relationship Diagrams
Initial plan

Initial ERD

The initial plan for the ERD consisted of a lot more tables and entities than were produced in the final application. The tables are coloured based on how I had hoped to prioritise the features of the application, and therefore the order in which I would tackle them. Given the time constraints, I only managed to deliver two tables plus a join, as depicted below
Delivered solution

Final ERD

As shown in this ERD, I ended up changing the focus of the initial tables. After building the first entity (poses), I concluded it made more sense to continue making a routine table first, encompassing a many-to-many relationship between the two. My reasoning was that it would make for a more interesting user experience to create routines from the poses, rather than arbitrarily add health benefits to each pose.

Multi Tier Architecture Diagram

Please click on the diagram for a high resolution version: MTA

This is a very high-level architecture diagram to demonstrate the architecture of the application. It does not include getters and setters, test classes, or constants classes.

Testing

JUnit, Mockito and Selenium tests have been used for automated testing, and SonarLint/SonarQube for static reporting and refactoring.

Report

Link to Final Surefire Report

Test coverage for the backend is at 84%, there are as of yet no working Selenium tests but hope to get these running soon. The SonarQube static report shows 9 code smells remaining, 0 bugs, 0 duplications and 0 vulnerabilities.

Deployment

The build, test and deployment process was automated using Jenkins, with a webhook to GitHub which was triggered with every push event

This application can be deployed both locally and externally through a virtual machine. The constants.js file has commented out options to switch from an external to local IP address.

Deployment Pipeline
Technologies Used

    H2 Database Engine - Database
    Java - Logic
    Wildfly - Deployment
    Jenkins - CI Server
    Maven - Dependency Management
    Jacoco, EclEmma, Surefire - Test Reporting
    SonarQube - Static Testing
    Git - VCS
    Trello - Project Tracking
    GCP - Live Environment

Front End Design
Wireframes

Poses Poses Wireframe Routines Routines Wireframe
Final Appearance

Improvements for the Future

Currently, IDs are required to update poses and routines, and to add or remove poses from routines. In my next sprint, I would like to create buttons in the front end which allow this functionality without the need for IDs, which would allow the object IDs to be hidden from the user.

In later sprints, I would also like create a health-benefit entity which would have a many to many relationship with poses, so that users can create routines based on their focus for their practice. After this, I would add the capability to create different user accounts. At this point, I would remove the functionality for the user to add and remove poses themselves in the front end. These would instead be hard coded into the database, which the user could manipulate only for adding and removing them from their own routines.

Authors

Aysha Marty

Acknowledgements

    QA consulting and our fantastic instructors
    The rest of our wonderful cohort on the programme


