#

![Mockup](docs/readme-images/mockup.p)

![GitHub last commit](https://img.shields.io/github/last-commit/marceillo/kayak-blog-pp4?color=red)
![GitHub contributors](https://img.shields.io/github/contributors/marceillo/kayak-blog-pp4?color=orange)
![GitHub language count](https://img.shields.io/github/languages/count/marceillo/kayak-blog-pp4?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/marceillo/kayak-blog-pp4?color=green)
<hr>

## Table of Contents

- [Overview](#overview)
- [User Experience](#ux)
- [Project Goal](#project-goal)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
- [Skeleton](#skeleton)
  - [Wireframes](#wireframes)
  - [Flowchart](#flowchart)
  - [Visual Effects](#visual-effects)
- [Features](#features)
  - [Visual Effects](#visual-effects)
  - [Home Page](#home-page)
  - [About Us Page](#about-us-page)
  - [Blogs Page](#blogs-page)
  - [Comments Page](#comments-page)
  - [Recipes Page](#recipes-page)
  - [Add Recipe Modal](#add-recipe-modal)
  - [Contact Page](#contact-page)
  - [Account Login](#account-login)
  - [Register](#register)
  - [Profile](#profile)
  - [Logout](#logout)
- [Agile Methodology](#agile-methodology)
  - [Responsive Layout and Design](#responsive-layout-and-design)
  - [Database](#database)
- [Testing](#testing)
  - [Lighthouse](#lighthouse)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Manual Testing](#manual-testing)
  - [Frontend](#frontend)
  - [Backend Admin Panel](#backend-admin-panel)
  - [Fixed Bugs](#fixed-bugs) 
- [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
- [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


## Overview


[Back to Table of Contents](#table-of-contents)

# UX
This website was created using the Five Planes Of Website Design<br>

**User Stories**

User stories can be viewed here on the project [kanban board ](https://github.com/users/hughes84/projects/1)

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily navigate through website content |             
|                                       |1B| As a user, I want to know what the website is about without having to do too much reading|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the blog's theme|
|**USER REGISTRATION**                  |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|                                       |2D| As a user, I want to know that I've logged out successfully|
|**BLOGS**                              |  ||
|                                       |3A| As a logged-in user, I want to be able to see relevant blogs clearly|
|                                       |3B| As a logged-in user, I want to be able to select a blog and comment and/or like selected blog|
|                                       |3C| As a logged-in user, I want to be able to delete my own previous comments|
|**RECIPES**                            |  ||
|                                       |4A| As a user, I want to see the recipes individual overview clearly|
|                                       |4B| As a user, I want to be able to access ingredients and methods|
|                                       |4C| As a logged-in user, I want to be able to navigate through different recipes easily|
|**ADMINISTRATION**                     |  ||
|                                       |5A| As a logged-in admin member, I want to be able to access the admin page|
|                                       |5B| As a logged-in admin member, I want to be able to authenticate and authorise comments and posts|
|                                       |5C| As a logged-in admin member, I want to be able to publish new recipes|
|                                       |5D| As a logged-in admin member, I want to be able to create a new user, recipes, author and categories|
|                                       |5E| As a logged-in admin member, I want to be able to delete users, recipes, authors, categories and comments|
|**CONTACT**                            |  ||
|                                       |6A| As a user, I want to be able to contact the site with ease|
|                                       |6B| As a user, I want to get a reply that my messgae has been received|
|                                       |6C| As a user, I want to see contact information on the website|

[Back to Table of Contents](#table-of-contents)

# Project Goal:



**Project Objectives:**

* To create a website with a simple and intuitive User Experience;
* To add content that is relevant to the topic and helps create a better understanding;
* To be able to differentiate between client and staff member accounts;
* To implement fully functional features that will ease the staff members' tasks and upgrade clients' experience with the blog features;
* To make the website responsive and functional on different devices.<br><br>

[Back to Table of Contents](#table-of-contents)

# Design

#### Colours

* 
## Colour Scheme
* 
<img src="docs/readme-images/primary-green.png" width="30%">
<img src="docs/readme-images/primary-white.png" width="30%">
<img src="docs/readme-images/primary-black.png" width="30%">
<img src="docs/readme-images/primary-grey.png" width="30%">
<img src="docs/readme-images/primary-orange.png" width="30%">
<br>

* The secondary colour scheme was used for buttons, warnings, errors or for highlighting important information.<br>
<img src="docs/readme-images/secondary-blue.png" width="30%">
<img src="docs/readme-images/secondary-gray.png" width="30%">
<img src="docs/readme-images/secondary-green.png" width="30%">
<img src="docs/readme-images/secondary-lightblue.png" width="30%">

[Back to Table of Contents](#table-of-contents)

#### Typography

* The Roboto font is used as the main font for the whole project.

[Back to Table of Contents](#table-of-contents)

#### Imagery

* 

# Skeleton

## Wireframes
The wireframes for mobile were created with <br>

<details>
  <summary>Wire Frames</summary>
  <h4>Home page</h4>
  <img src="docs/readme-images/wireframe-home.png"><br>
  <h4>About page</h4>
  <img src="docs/readme-images/wireframe-about.png"><br>
  <h4>About more</h4>
  <img src="docs/readme-images/wireframe-aboutmore.png"><br>
  <h4>Blog page</h4>
  <img src="docs/readme-images/wireframe-blog.png"><br>
  <h4>Blog user comments</h4>
  <img src="docs/readme-images/wireframe-comments.png"><br>
  <h4>Recipes</h4>
  <img src="docs/readme-images/wireframe-recipe.png"><br>
  <h4>Recipe details</h4>
  <img src="docs/readme-images/wireframe-recipedetail.png"><br>
  <h4>Contact us</h4>
  <img src="docs/readme-images/wireframe-contactpage.png"><br>
  <h4>Submit message</h4>
  <img src="docs/readme-images/wireframe-contactmsg.png"><br>
  <h4>User profile</h4>
  <img src="docs/readme-images/wireframe-profile.png"><br>
  <h4>Sign in</h4>
  <img src="docs/readme-images/wireframe-signin.png"><br>
  <h4>Sign up</h4>
  <img src="docs/readme-images/wireframe-signup.png"><br>
</details>
</details><br>

[Back to Table of Contents](#table-of-contents)

## Flowchart
 
## Visual Effects

* 
## Features

### Home Page

![Home Page](docs/readme-images/screen-home.png)

* The hero image

### About Us Page

![About Us](docs/readme-images/screen-aboutus.png)


* Note:

[Back to Table of Contents](#table-of-contents)

### Blogs Page

![Blogs](docs/readme-images/screen-blogs.png)

* Note:

[Back to Table of Contents](#table-of-contents)

### Comments Page

![Comments](docs/readme-images/screen-comments.png)

* Note:

[Back to Table of Contents](#table-of-contents)

### Recipes Page

![Recipes](docs/readme-images/screen-recipes.png)

* 
[Back to Table of Contents](#table-of-contents)

### Add  Modal

![Recipes](docs/readme-images/screen-addrecipe.png)

* 

[Back to Table of Contents](#table-of-contents)

### Contact Page

![Contact](docs/readme-images/screen-contact.png)

* 
[Back to Table of Contents](#table-of-contents)

### Account login

![Login](docs/readme-images/screen-login.png)

* 
[Back to Table of Contents](#table-of-contents)

### Register

![Register](docs/readme-images/screen-register.png)

* 

[Back to Table of Contents](#table-of-contents)

### Profile

![Profile](docs/readme-images/screen-profile.png)

* The profile page allows the user to add an image as well as edit their profile picture, username or email address.

[Back to Table of Contents](#table-of-contents)

### Logout

![Logout](docs/readme-images/screen-signout.footer.png)

* 

[Back to Table of Contents](#table-of-contents)

## Database

The project uses the PostgreSQL relational database for storing the data.

## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [Github issues](https://github.com/hughes84/my-blog-pp4/issues). As the user stories were accomplished, they were moved in the Kanban Board from **Epic**,**User stories**, **To Do**, to **In-progress**, **Testing** and **Done** lists. 

## Responsive Layout and Design
The project design has been adapted to all types of devices using Bootstrap predefined breakpoints. For intermediate devices where the design didn't fit accordingly, custom breakpoints were used.

**Breakpoints:**
    - max-width:575.98px
    - max-width:991.98px
    - max-width:1300.98px

[Back to Table of Contents](#table-of-contents)

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predifined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
LightHouse - for testing performance<br>

[Back to Table of Contents](#table-of-contents)

# Testing

* Testing has taken place continuously throughout the development of the project. Each view was tested regularly. 
  When the outcome was not as expected, debugging took place at that point.

  ### Python Validation - PEP8
* Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files
were entered into the online checker and no errors were found in any of the custom codes.

![Pyhton](docs/readme-images/screen-pyhton.png)

## Lighthouse
Lighthouse was used to test Performance, Best Practices, Accessibility, and SEO on Desktop.

![Lighthouse](docs/readme-images/screen-lighthouse.png)

[Back to Table of Contents](#table-of-contents)

## HTML Validation

![HTML](docs/readme-images/screen-w3c.png)

## CSS Validation
* Custom CSS was validated using W3C Jigsaw validation service. No were displayed.

![CSS](docs/readme-images/screen-css.png)

[Back to Table of Contents](#table-of-contents)

## Manual Testing
### Frontend
* 
[Back to Table of Contents](#table-of-contents)

### Backend Admin Panel
* 

[Back to Table of Contents](#table-of-contents)

* **All known bugs have been fixed**

## Fixed bugs

| **Bug** | **Fix** |
| --- | --- |
| Bug: Performance is very low | Solution: Load Css and Javascript asynchronously |
| Bug:  While I was developing the project I tried to merge my recipe model and my recipe detail model and when I tried to migrate the changes I got an error in the terminal telling me the terminal required a default number for the new foreign key. | I entered no and closed terminal and entered default value in the model itself

[Back to Table of Contents](#table-of-contents)

## Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py runserver
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

[Back to Table of Contents](#table-of-contents)

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New
App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

[Back to Table of Contents](#table-of-contents)

## Final Deployment 

1. Create a runtime.txt `python-3.8.13`
2. Create a Procfile `web: gunicorn your_project_name.wsgi`
3. When development is complete change the debug setting to: `DEBUG = False` in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: `X_FRAME_OPTIONS = SAMEORIGIN `to
   settings.py.
5. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

[Back to Table of Contents](#table-of-contents)

## Forking This Project

* Fork this project by following the steps:

1. Open [GitHub](https://github.com/hughes84/my-blog-pp4.git)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/hughes84/my-blog-pp4.git)
2. You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order
to copy the URL
3. Once you click the button the fork will be in your repository
4. Open a new terminal
5. Change the current working directory to the location that you want the cloned directory
6. Type 'git clone' and paste the URL copied in step 3
7. Press 'Enter' and the project is cloned

[Back to Table of Contents](#table-of-contents)

## Credits

### Content

* 

## Acknowledgements

* 
[Back to Table of Contents](#table-of-contents)
