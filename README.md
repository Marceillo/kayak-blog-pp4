
<img src="static/readme/images/mockup.png">

## Table of Contents

- [Overview](#overview)
- [Project Goal](#project-goal)
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
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
  - [Contact Page](#contact-page)
  - [Account Login](#account-login)
  - [Register](#register)
  - [Profile](#profile)
  - [Logout](#logout)
  - [Future Features](#future-features)
  - [Dependencies](#dependencies)
- [Agile Methodology](#agile-methodology)
  - [Responsive Layout and Design](#responsive-layout-and-design)
  - [Database](#database)
- [Testing](#testing)
  - [Testing User Stories](#testing-user-stories)
  - [Lighthouse](#lighthouse)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Manual Testing](#manual-testing)
  - [Frontend](#frontend)
  - [Backend Admin Panel](#backend-admin-panel)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
- [Creating the Django app](#creating-the-django-app)
  - [Deployment of This Project](#deployment-of-this-project)
  - [Final Deployment](#final-deployment)
  - [Forking This Project](#forking-this-project)
  - [Cloning This Project](#cloning-this-project)
- [Credits](#credits)
  - [Acknowledgements](#acknowledgements)


## Overview

I love water sports, and kayaking is one of the best ways for me to be in nature and escape from daily life. That's why I decided to create a kayaking blog, where my fellow paddlers and I can share our experiences on the water. Please feel free to see the [live link](https://kayak-blog-pp4-1054055911f7.herokuapp.com/my-posts/) 

## Project Goal:

The goal is to build a community around kayaking, where we can share knowledge and insights to enhance everyone's experience in the sport.

**Project Objectives:**

* Provide people the opportunity to write about their kayaking experiences.
* Connect kayakers to kayakers is the idea so that we can find more information or just blog about our experiences and safety tips.
* Share ideas and create a community around kayaking so that the paddling experience is shared. 


[Back to Table of Contents](#table-of-contents)


# User Experience UX

**User Stories**

User stories can be viewed here on the project [kanban board ](https://github.com/users/Marceillo/projects/8/views/1)

| EPIC                               | ID | User Story                                                           |
| :--------------------------------- | -- | :------------------------------------------------------------------- |
| **User Authentication and Profiles**|    |                                                                      |
|                                     | 1.1| As a user, I can register and log in so that I can access the website.|             
|                                     | 1.2| As a user, I want to view and edit my profile.                        |
| **Core Blog Functionality** |    |                                                                      | 
|                                     | 2.1| As a user, I want to search for specific kayaking topics.             |
|                                     | 2.2| As a content creator, I can write blog posts so that it is published. |
|                                     | 2.3| As a user, I want to read blog posts about kayaking experiences.      |
| **User Interaction and Engagement** |    |                                            |
|                                     | 3.1 |As a user, I want to comment on blog posts. |
|                                     | 3.2 | As a user, I want to like blog posts. |
|                                     | 3.3 |As a user, I want to favorite blog posts to find them later easily.  |
| **Core Blog Functionality** |    |                                                       |
|                                     | 4.1 | As a content creator, I want to upload for **images for my blog posts.|
|                                     | 4.2 | As a user, I want to search for specific kayaking topics.           |
|                                     | 4.3 | As a content creator, I can write blog posts so that it is published.|
| **Admin Functionality** |     |                                                                     |
|                                     | 5.1 | As an admin, I want to manage users and content through the admin panel. |
| **EPIC: Mobile Responsiveness and UI/UX**|    |                                                                 |
|                                     | 6.1 | As a user, I want to view the website on my mobile device.          |
|                                     | 6.2 | As a user, I want to view the website on my Focus on testing all implemented features.          |
|**Focus on testing all implemented features**.| 


[Back to Table of Contents](#table-of-contents)


# Design

## Colours

* I used colors to match the background which is a moving mp4, more about that below in visual experience.

 <img src="static/readme/images/backgroundmp4.png"><br>

### Colour Scheme

* Used a [Coolors web site](https://coolors.co/palettes/trendin) to search for colors that match.

[Back to Table of Contents](#table-of-contents)

#### Typography

* The Roboto font is the main font, and Lato is the secondary font used for the whole project.

[Back to Table of Contents](#table-of-contents)

#### Imagery

* I sourced images and the moving background from [pixabay](https://pixabay.com/).

# Skeleton

## Wireframes

* The wireframes for mobile and desktop and used [Balsamiq](https://balsamiq.com/)

<br>
<details>
  <summary>Wire Frames</summary>
  <h4>Home page</h4>
  <img src="static/readme/images/wireframes/home.png"><br>
  <h4>Home after signed in page</h4>
  <img src="static/readme/images/wireframes/home_signin.png"><br>
  <h4>Create Blog page link only when logged in</h4>
  <img src="static/readme/images/wireframes/create_blog.png"><br>
  <h4>My Blog page link only when logged in</h4>
  <img src="static/readme/images/wireframes/myblog.png"><br>
  <h4>Profile page link only when logged in</h4>
  <img src="static/readme/images/wireframes/profile.png"><br>
  <h4>MY Profile edit page link only when logged in</h4>
  <img src="static/readme/images/wireframes/profile_edit.png"><br>
  <h4>About page</h4>
  <img src="static/readme/images/wireframes/about.png"><br>
  <h4>About contact page</h4>
  <img src="static/readme/images/wireframes/about_contact.png"><br>
  <h4>Register page </h4>
  <img src="static/readme/images/wireframes/register.png"><br>
  <h4>Login</h4>
  <img src="static/readme/images/wireframes/login.png"><br>
  <h4>Signout</h4>
  <img src="static/readme/images/wireframes/signout.png"><br>
</details>

<br>

[Back to Table of Contents](#table-of-contents)

## Initial ERD Diagram

<details>
<summary>My Intial ERD Diagram</summary>

* For the initial ERD diagram plan, I used [lucid chart](https://www.lucidchart.com/)
<br>
<br>
<img src="static/readme/images/lucid_erd_diagram.png">
<br>
<br>
</details>

## Django ERD Diagram
<details>
<summary>Used code Django to get an ERD.dot file and convert it to ERD Diagram</summary>
Django has a built-in tool that can show you your ERD diagram.

### Reason 

* It is not always possible to start a project from scratch sometimes it may be the case that you need to work on someone else project.
* So this will give me as a developer an overview of the project from an ERD standpoint.

### Steps used
* Step 1 to using this is to install django-extensions.
* Step 2 would be to add the installed apps.
* Step 3 would be to add it to the requirements file.
* Step4 is to run the python manage.py graph_models -a --output erd.dot 
* Step5 After this it will create an erd. dot file with all the application model data.
* Step 6 Put the data in this software to change to an image file much like the one I used below.

The red dot file converted to image [Graphviz online](https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D)
<br>
<br>
<img src="static/readme/images/erd_diagram.png"><br>

## Credit below for the above-detailed ERD diagram.

[YouTube link](https://www.youtube.com/watch?v=qzrE7cfc_3Q&t=357s)

[django-extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
</details>

## Visual Experience

* The goal was to bring in a feel of water so you feel as if you are there in the water with other paddlers.
* It is a moving image in a dark green and this has positives and negatives to the design.
* If I decided to deploy it to the public I would make some small changes to the color scheme but mostly I am happy with it.
* I used some Bootstrap code for the html and implemented this in my templates.
* I got inspiration from the LMS project and used the base template modifying it to my needs and then replicating this into other smaller templates. 

#### Positives

* It compliments the the idea and the sport nicely.
* A large number of my kayak friends and family like the moving background.
* It's different and fresh from what I have done before this kept my motivation high in the really tough times of this project.

#### Negatives 

* It might not suit well with all people as some did not like the moving image.
* People with visual problems might have difficulty viewing some features.
* I tested this with my Father who is color blind and he was able to find his way around the site so I am happy with that result.

## Features

### Home Page

<details>

<summary>Home Page Summary</summary>

<br>

#### Before login 

* Before login The user will see a home page with the blog posts.
* They will be able to read blog post comments use the search feature and access the footer links.
* If they wish to have more features they will need to log in or Register if they do not have an account. 
* On the right is a message that displays that you are not logged in.
* There is a search option in the nav bar that will display before and after login.

 <br>

![Home Page](/static/readme/images/home-screen.png)

<br>

#### After login  

* Note: After login the nav bar will change a bit it will include extra links for more features explained later.
* The first link will be the Profile Page which will display the login user name.
* The second Link will be a Create Blog link.
* Also the login button will change its text to logout. 


<br>

![Home Page](/static/readme/images/after-login-page.png)

### Footer

* Has social website links to Facebook, X, and YouTube.

<br>

![Home Page](/static/readme/images/footer.png)

<br>

</details>

### About Page

<details>
<summary>About Page summary</summary>
<br>

* Note: This is a basic page with a contact form for users to get in contact.
* While developing I noticed that most kayak sites do not have this as a landing page as most just want to see the pictures and content including me.
* Since it's not a live site, we don't have an exchange to set it up, to make it more functional so that we can send a message to the email service provider.

<br>

![About](/static/readme/images/about-page.png)

<br>

#### Contact form 

* Note: This is a basic page with a contact form for users to get in contact.

<br>

![About](/static/readme/images/contactform.png)

<br>

</details> 

### Register Page

<details>

<summary>Register Page summary</summary>

<br>

* Note: Here the user can register an account for more features in order to have some CRUD functionality.
* The email address is optional for now as this is not yet live to the general public and some might not like that.
* If a user decides not to enter an email address and forget their password they will need to use the contact form so that the admin can reset this.

<br>

![Register](/static/readme/images/register-page.png)

</details>

### Login page

<details>

<summary>Login and Logout Page summary</summary>

<br>

* Note: Here you can log in using the allauth tool in Django.
* Note: I added the forgot password feature here to give the users the ability to be independent. 
* However it is not 100 percent as certain mail servers block Django messages. 

<br>

![Login](/static/readme/images/login-page.png)

#### Forgot Password

<br>

* When you click on the forgot password you will be prompted for your email address.

<br>

![Login](/static/readme/images/forgot-password.png)

<br>

* If you did not add an email address as it is optional you can use the About contact form.
* Once you enter your e-mail address you will see this screen as a user.

<br>

![Login](/static/readme/images/passwordresetmessage.png)


##### NOTE:

* The link will be sent to the IDE terminal and only to certain email service providers.
* The reason for this is that certain service providers block Django messages on the server side such as Gmail.
* This is not a live site and not in control of the SMTP server I have to accept this result.

###### Terminal link view 
<br>

![Login](/static/readme/images/passchangeterminal.png)

<br>

###### Temporary email address view test from Heruko

* The way I tested this was to use a temporary [ temporary e-mail service provider](https://temp-mail.org/).
* Created a user account with the temp email service provider and tested this.

<br>

![Login](/static/readme/images/passtempforgotpasswordlink.png)

<br>

</details>


[Back to Table of Contents](#table-of-contents)

### After login: Profile Page CRUD 

<details>

<summary>Profile Page summary</summary>

#### Profile page view 

* When you click on the Profile icon with your registered name it will show you your profile data.
* Here you will have CRUD functionality.
* You will be able to change your password.
* Delete Your profile.
* Edit your Profile Image as there is a default image, as well as personal details including kayaking skills.     

<br>

![Profile](/static/readme/images/profile-edit-page.png)

<br>

#### Profile Edit 

<br>

![Profile edit](/static/readme/images/profile-edit-form.png)

<br>

#### Profile password Change 

![Password Change](/static/readme/images/profile_passwordchange.png)

<br>

#### Profile Delete

<br>

![Profile Delete](/static/readme/images/delet_profile.png)

<br>

</details>

[Back to Table of Contents](#table-of-contents)

### Blog Post CRUD 

<details>

<summary>Blog Post Summary</summary>

#### Create a Blog page link 

* The user can create a blog Using this form.
* A default picture has been set up if the user decides not to select one.
* The user can set the post to Draft or Published state.
* In Draft the user will need to go to My Blog to see their drafts.
* If in the published state it will go straight to the blog page for everyone to see.

<br>

![Create Blog](/static/readme/images/create-blog.png)

<br>

#### My Blog view

* Here you can see the CRUD buttons and the post you created.
* Your draft Posts will be here and the Published posts.
* As a user you will be able to Read, edit(UPdate), and Delete Posts.
* should you wish to create you will need to go to the create blog link.
* Originally I had the create link in the view as well but did not want to overpopulate the view with buttons so took it out. 
 
<br>

![Create Blog](/static/readme/images/mb-blog.png)

<br>

#### Edit Post 

* The user can update the title and body and the status is also in control of the user.
* You can choose an image for your post if you don't have one a default image is shown.
* In the input field when selecting an image and you decide you want the field blank there is a script that clears the input.
* Once you have chosen an image and don't like it you can change the image.

<br>

![Edit Post](/static/readme/images/edit-post.png)

<br>

#### Delete Post 

* If you click on the deleted post you will receive a confirmation pop-up.
* The success message or error message.

<br>

![Delet Post](/static/readme/images/delet-post.png)

<br>

#### Detail view 

* This view will be when you click on a post and want to read the post.
* It will check that you are the author if so you will see extra buttons (edit_post,delet_post)
* If not it will not show buttons you also will see the favorites and comments in a later section for more info.
* Here you can read more about the post the author and the created date details are also present.

<br>

![Detail View](/static/readme/images/detail-view.png)

<br>

</details>

[Back to Table of Contents](#table-of-contents)

### Comments CRUD

<details>

<summary>Comment Page summary</summary>

* In this blog post a logged user will have the opportunity to write a comment on a blog post.
* You can create, read, update, and delete comments.
* So when things go write you get a success message or a message. error in the unlucky case.

<br>

![Comment View](/static/readme/images/comments.png)

<br>

##### Update comment 

* When you update a comment the comment icon turns red and there is a count that shows how many comments.
* When there is no comment there is no count and the icon is not fully red.

<br>

![Update Comment](/static/readme/images/comment_update%20.png)

<br>

##### Edit Comment 

* You can update the comment and receive a success message with the displayed update on the post.
* Of course when unsuccessful you will also receive an error message.

<br>

![Edit Comment](/static/readme/images/edit-comment.png)

<br>

##### Delete Comment 

* You will get a confirmation message and then a success message or error message if not.

<br>

![Delete Comment](/static/readme/images/delet-comment.png)

<br>

</details>

### Favorites 

* Here you can favorite or unfavorite a Post 
* When you do so the star goes red and you receive a success message or error message when not.

<details>

<summary>Favorite Image </summary>



#### Favorited 

<br>

![Favorited](/static/readme/images/favorited.png)

<br>

#### Unfavorited

<br>

![Unfavorites](/static/readme/images/unfavorited.png)

<br>

</details>

### Confirmation Messages 
<details>
<summary>Confirmation messages</summary>

* There are success confirmation message and error messages 
* There is Java Script and mondal code inspired by the LMS.

* Logging in and out
* In the Comments features
* In the post features
* When registering a new account
* In the Profile features  
* Favorite or unfavorite

![Style of the Message](/static/readme/images/message-style.png)

</details>

[Back to Table of Contents](#table-of-contents)

### Future Features

* Originally I planned the like feature to include in the project but due to time constraints and having met the MPV criteria, I would like to come back to this project and include it at a later stage.
* I have since moved it to a won't have status on the Kanban Board.  
* For the contact form it would be great at a later stage to set up an API with Javascript and implement a feature when a user sends their details that it goes to an email address of the admin.
* The Favorite feature is working as planned but if the site should grow I will need to change it into a separate link on the page as this method makes it easier for users to keep track of their project favorites.
* At The moment the colors are my favorite but there is always room for improvement also for the design and flow of the blog posts. Due to time, this was the biggest issue for me in this regard.
* As a kayaker we often have meetups and would like to include a feature that will assist with the logistics and dates of their meetups.
* A feature to join in on classes or book an instructor for some time.
* An online training program with video guides and information.
* In the far future people to be able to sell their equipment and buy from others on the platform.
* I did not inlcude Pagination for the amount of blog posts this would be great to come back to and update at later date.  


[Back to Table of Contents](#table-of-contents)

## Dependencies
<details>
<summary>Dependencied brief summary</summary>
This document provides a brief description of the key dependencies used in the app.

- **asgiref==3.8.1**: A library that provides utilities for ASGI (Asynchronous Server Gateway Interface) applications.

- **click==8.1.7**: A package for creating command-line interfaces (CLI) in Python.

- **cloudinary==1.40.0**: A library for integrating Cloudinary's image and video management services in the application.

- **colorama==0.4.6**: A library that allows for cross-platform colored terminal text in Python.

- **crispy-bootstrap5==2024.2**: A Django application that provides Bootstrap 5 support for crispy forms.

- **cssbeautifier==1.15.1**: A tool for formatting and beautifying CSS code.

- **dj-database-url==0.5.0**: A utility for parsing database URLs and configuring Django's database settings from environment variables.

- **dj3-cloudinary-storage==0.0.6**: A Django storage backend for Cloudinary.

- **Django==4.2.13**: The primary web framework for building web applications in Python.

- **django-allauth==0.57.2**: A comprehensive authentication package for Django that supports authentication and account management.

- **django-crispy-forms==2.2**: A Django application that helps to manage and render forms with a clean and customizable layout.

- **django-extensions==3.2.3**: A collection of custom extensions for Django.

- **EditorConfig==0.12.4**: A plugin that helps maintain consistent coding styles across different editors and IDEs by using a `.editorconfig` file.

- **gunicorn==20.1.0**: A Python WSGI HTTP server for UNIX, used to serve your Django application in a production environment.

- **html-tag-names==0.1.2**: A library that provides a list of HTML tag names.

- **html-void-elements==0.1.0**: A utility that defines void elements in HTML.

- **jsbeautifier==1.15.1**: A JavaScript beautifier that formats and beautifies JavaScript code for improved readability.

- **oauthlib==3.2.2**: A generic, spec-compliant implementation of the OAuth request-signing logic for Python, facilitating OAuth 1 and OAuth 2 support.

- **pathspec==0.12.1**: A library that provides a way to specify file patterns for matching files in a directory.

- **psycopg2==2.9.9**: A PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.

- **PyJWT==2.8.0**: A Python library for encoding and decoding JSON Web Tokens (JWT), used for secure authentication and information exchange.

- **python-dotenv==1.0.1**: A library that reads key-value pairs from a `.env` file and adds them to the environment variables.

- **python3-openid==3.2.0**: A library for OpenID authentication in Python, enabling users to log in using their OpenID credentials.

- **regex==2024.7.24**: An alternative to Python's built-in `re` module, providing additional functionality for regular expressions.

- **requests-oauthlib==2.0.0**: A library that provides OAuth support for the popular `requests` library, making it easier to work with OAuth-protected APIs.

- **sqlparse==0.5.0**: A non-validating SQL parser for Python, useful for formatting and analyzing SQL queries.

- **tqdm==4.66.5**: A library for creating progress bars in Python.

- **whitenoise==6.5.0**: A middleware for serving static files in Django applications, simplifying static file management in production environments.

</details>

## Database

The project uses the PostgreSQL database for storing the data.

## Agile Methodology
This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [Github](https://github.com/users/Marceillo/projects/8). As the user stories were accomplished, they were moved in the Kanban Board from **Epic**,**User stories**, **No Status**, **To Do**, to **In-progress**, and **Done** lists.

I added sprints to help with organizing the project and MoSCoW prioritization Labels were also included in each issue. Additionally, I included tasks for some guidance as to what needs to be done. 


## Responsive Layout and Design

The project design was adapted to different devices and Bootstrap helped with most of this. My focus was really to have a working Django APP and as I have said before time was an issue for me to really do a design with all the bells and whistles this will be my future focus for this project.

[Back to Table of Contents](#table-of-contents)

## Tools Used

[GitHub](https://github.com/) - used for hosting the source code of the program<br>
[Heroku](https://dashboard.heroku.com/) - used for deploying the project<br>
[Favicon.io](https://favicon.io/) - used for generating the website favicon<br>
[Font Awesome](https://fontawesome.com/) - for creating atractive UX with icons<br>
[Bootstrap5](https://getbootstrap.com/) - for adding predefined styled elements and creating responsiveness<br>
[Google Fonts](https://fonts.google.com/) - for typography<br>
[JsHint](https://jshint.com/) - used for validating the javascript code<br>
[PEP8 Validator](http://pep8online.com/) - used for validating the python code<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options) - used for validating the HTML<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri) - used for validating the CSS<br>
[GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/#digraaph%20G%20%7B%0A%0A%20%20subgraph%20cluster_0%20%7B%0A%20%20%20%20style%3Dfilled%3B%0A%20%20%20%20color%3Dlightgrey%3B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%2Ccolor%3Dwhite%5D%3B%0A%20%20%20%20a0%20-%3E%20a1%20-%3E%20a2%20-%3E%20a3%3B%0A%20%20%20%20label%20%3D%20%22process%20%231%22%3B%0A%20%20%7D%0A%0A%20%20subgraph%20cluster_1%20%7B%0A%20%20%20%20node%20%5Bstyle%3Dfilled%5D%3B%0A%20%20%20%20b0%20-%3E%20b1%20-%3E%20b2%20-%3E%20b3%3B%0A%20%20%20%20label%20%3D%20%22process%20%232%22%3B%0A%20%20%20%20color%3Dblue%0A%20%20%7D%0A%20%20start%20-%3E%20a0%3B%0A%20%20start%20-%3E%20b0%3B%0A%20%20a1%20-%3E%20b3%3B%0A%20%20b2%20-%3E%20a3%3B%0A%20%20a3%20-%3E%20a0%3B%0A%20%20a3%20-%3E%20end%3B%0A%20%20b3%20-%3E%20end%3B%0A%0A%20%20start%20%5Bshape%3DMdiamond%5D%3B%0A%20%20end%20%5Bshape%3DMsquare%5D%3B%0A%7D) - To take erd. dot file and convert to a graph<br>
LightHouse in the browser- for testing performance<br>
[Cloudinary](https://cloudinary.com/users/login) - to handel the image storage.<br>
[CI database](https://dbs.ci-dbs.net/)

[Back to Table of Contents](#table-of-contents)

# Testing

* Testing was ongoing during this project from one feature to the next even so I left some of the final testing for last.
 
## Testing User Stories

<details>
<summary>User stories testing</summary>

## User Stories Table

| EPIC                                 | ID   | User Story                                                                 | Check | Test Result                                                                                      |
| :----------------------------------- | ---- | :------------------------------------------------------------------------- | :---: | :----------------------------------------------------------------------------------------------- |
| **User Authentication and Profiles** |      |                                                                           |       |                                                                                                 |
|                                     | 1.1  | As a user, I can register and log in so that I can access the website.   | [x]   | The button is there to register and I can access the site after login.                         |
|                                     | 1.2  | As a user, I want to view and edit my profile.                            | [x]   | I can access my profile and have CRUD functionality.                                           |
| **Core Blog Functionality**         |      |                                                                           |       |                                                                                                 |
|                                     | 2.1  | As a user, I want to search for specific kayaking topics.                 | [x]   | I can search by title, body, excerpt, and author for kayaking topics in the blog.              |
|                                     | 2.2  | As a content creator, I can write blog posts so that they are published.  | [x]   | I can write a post as an admin and as a user, and I can see it in draft and published with CRUD functionality. |
|                                     | 2.3  | As a user, I want to read blog posts about kayaking experiences.          | [x]   | I can read blog posts in detail.                                                                |
| **User Interaction and Engagement** |      |                                                                           |       |                                                                                                 |
|                                     | 3.1  | As a user, I want to comment on blog posts.                               | [x]   | I have CRUD functionality on comments.                                                          |
|                                     | 3.2  | As a user, I want to like blog posts.                                     | [ ]   | For future implementation.                                                                       |
|                                     | 3.3  | As a user, I want to favorite blog posts to find them later easily.      | [x]   | I can favorite and unfavorite blog posts.                                                      |
| **Admin Functionality**             |      |                                                                           |       |                                                                                                 |
|                                     | 5.1  | As an admin, I want to manage users and content through the admin panel.  | [x]   | The admin has CRUD functionality and can manage the content.                                   |
| **EPIC: Mobile Responsiveness and UI/UX** |  |                                                                           |       |                                                                                                 |
|                                     | 6.1  | As a user, I want to view the website on my mobile device.               | [x]   | Yes, I can view the website on a mobile device and other formats.                              |
|                                     | 6.2  | I want to view the website on my mobile device.                           | [x]   | I have tested the features on a mobile device.                                                 |
| **Focus on Testing All Implemented Features** | |                                                                           | [x]   | All focused features have been tested on an ongoing basis.
</details>

## Python Validation - PEP8

* I had a lot of errors found but none that could not be fixed, use this tool [pep8ci](https://pep8ci.herokuapp.com/)
* Cleared all until I received the below result. 

<br>

![Pyhton](/static/readme/test-image/blogviewpepnoerror.png)

<br>

<details>
<summary>Blog PeP8 errors/warnings fixed</summary>

#### Blog View

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 18         | E265 block comment should start with '# '                               | 26         | W291 trailing whitespace                                                 |
| 27         | E302 expected 2 blank lines, found 0                                    | 28         | E501 line too long (86 > 79 characters)                                 |
| 29         | E231 missing whitespace after ','                                        | 36         | W291 trailing whitespace                                                 |
| 37         | E302 expected 2 blank lines, found 0                                    | 40         | E305 expected 2 blank lines after class or function definition, found 1 |
| 41         | E501 line too long (99 > 79 characters)                                 | 48         | E302 expected 2 blank lines, found 0                                    |
| 52         | E501 line too long (113 > 79 characters)                                | 55         | W293 blank line contains whitespace                                       |
| 58         | W291 trailing whitespace                                                 | 65         | E501 line too long (112 > 79 characters)                                |
| 75         | W293 blank line contains whitespace                                       | 78         | E501 line too long (92 > 79 characters)                                 |
| 79         | E501 line too long (111 > 79 characters)                                | 85         | E302 expected 2 blank lines, found 0                                    |
| 87         | E225 missing whitespace around operator                                   | 90         | W293 blank line contains whitespace                                       |
| 98         | E501 line too long (87 > 79 characters)                                 | 101        | W293 blank line contains whitespace                                       |
| 103        | E501 line too long (83 > 79 characters)                                 | 104        | W291 trailing whitespace                                                 |
| 106        | E305 expected 2 blank lines after class or function definition, found 1 | 114        | W291 trailing whitespace                                                 |
| 119        | E302 expected 2 blank lines, found 0                                    | 121        | E225 missing whitespace around operator                                   |
| 127        | W293 blank line contains whitespace                                       | 134        | W293 blank line contains whitespace                                       |
| 135        | E501 line too long (87 > 79 characters)                                 | 139        | E501 line too long (83 > 79 characters)                                 |
| 140        | W291 trailing whitespace                                                 | 150        | E501 line too long (80 > 79 characters)                                 |
| 152        | E501 line too long (86 > 79 characters)                                 | 155        | E302 expected 2 blank lines, found 0                                    |
| 161        | E303 too many blank lines (2)                                          | 164        | W293 blank line contains whitespace                                       |
| 166        | E303 too many blank lines (2)                                          | 167        | E501 line too long (85 > 79 characters)                                 |
| 170        | W293 blank line contains whitespace                                       | 172        | E501 line too long (83 > 79 characters)                                 |
| 173        | W291 trailing whitespace                                                 | 174        | W293 blank line contains whitespace                                       |
| 175        | E305 expected 2 blank lines after class or function definition, found 1 | 176        | E501 line too long (84 > 79 characters)                                 |
| 181        | W291 trailing whitespace                                                 | 183        | W291 trailing whitespace                                                 |
| 184        | E302 expected 2 blank lines, found 0                                    | 190        | E501 line too long (81 > 79 characters)                                 |
| 194        | E303 too many blank lines (3)                                          | 198        | W291 trailing whitespace                                                 |
| 199        | E302 expected 2 blank lines, found 0                                    | 201        | E231 missing whitespace after ','                                        |
| 208        | E305 expected 2 blank lines after class or function definition, found 1 | 209        | E501 line too long (80 > 79 characters)                                 |
| 213        | E302 expected 2 blank lines, found 0                                    | 217        | E501 line too long (96 > 79 characters)                                 |
| 232        | E211 whitespace before '('                                               | 232        | E231 missing whitespace after ','                                        |
| 232        | E501 line too long (88 > 79 characters)                                 | 234        | E305 expected 2 blank lines after class or function definition, found 1 |
| 240        | E302 expected 2 blank lines, found 0                                    | 248        | E231 missing whitespace after ','                                        |
| 248        | E501 line too long (82 > 79 characters)                                 | 251        | E501 line too long (95 > 79 characters)                                 |
| 252        | W293 blank line contains whitespace                                       | 254        | W293 blank line contains whitespace                                       |
| 257        | E305 expected 2 blank lines after class or function definition, found 1 | 261        | E302 expected 2 blank lines, found 0                                    |
| 263        | W293 blank line contains whitespace                                       | 264        | E117 over-indented                                                       |
| 275        | W293 blank line contains whitespace                                       | 276        | E303 too many blank lines (2)                                          |
| 278        | E305 expected 2 blank lines after class or function definition, found 1 | 284        | E302 expected 2 blank lines, found 0                                    |
| 294        | E501 line too long (82 > 79 characters)                                 | 300        | W293 blank line contains whitespace                                       |
| 305        | W291 trailing whitespace                                                 | 308        | E302 expected 2 blank lines, found 0                                    |
| 311        | W293 blank line contains whitespace                                       | 313        | E231 missing whitespace after ','                                        |
| 315        | W293 blank line contains whitespace                                       | 318        | W293 blank line contains whitespace                                       |
| 321        | E501 line too long (84 > 79 characters)                                 | 327        | E501 line too long (93 > 79 characters)                                 |
| 327        | E202 whitespace before ''                                               | 332        | W291 trailing whitespace                                                 |
| 336        | E302 expected 2 blank lines, found 0                                    | 339        | W293 blank line contains whitespace                                       |
| 343        | W293 blank line contains whitespace                                       | 347        | E501 line too long (80 > 79 characters)                                 |
| 350        | W293 blank line contains whitespace                                       | 352        | E303 too many blank lines (2)                                          |
| 354        | E305 expected 2 blank lines after class or function definition, found 1 | 357        | W291 trailing whitespace                                                 |
| 359        | E302 expected 2 blank lines, found 0                                    | 371        | W291 trailing whitespace                                                 |
| 381        | W291 trailing whitespace                                                 | 382        | E302 expected 2 blank lines, found 0                                    |
| 394        | W291 trailing whitespace                                                 | 395        | E122 continuation line missing indentation or outdented                 |
| 395        | E501 line too long (82 > 79 characters)                                 | 397        | W293 blank line contains whitespace                                       |
| 398        | E303 too many blank lines (2)                                          | 398        | E202 whitespace before ')'                                               |
| 407        | W291 trailing whitespace                                                 | 411        | W391 blank line at end of file                                           |

#### Blog Urls

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 4          | W293 blank line contains whitespace                                       | 7          | E303 too many blank lines (4)                                          |
| 13         | E501 line too long (97 > 79 characters)                                 | 15         | E501 line too long (88 > 79 characters)                                |
| 16         | E501 line too long (101 > 79 characters)                                | 17         | E501 line too long (103 > 79 characters)                               |
| 20         | E501 line too long (81 > 79 characters)                                 | 21         | E501 line too long (84 > 79 characters)                                |
| 22         | E501 line too long (90 > 79 characters)                                 | 23         | E265 block comment should start with '# '                              |
| 23         | E501 line too long (89 > 79 characters)                                 | 24         | E265 block comment should start with '# '                              |
| 24         | E501 line too long (95 > 79 characters)                                 | 25         | E231 missing whitespace after ','                                       |
| 25         | E501 line too long (87 > 79 characters)                                 | 28         | W391 blank line at end of file                                          |

#### Blog Models

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 51         | W293 blank line contains whitespace                                       | 55         | W291 trailing whitespace                                                 |
| 56         | W293 blank line contains whitespace                                       | 60         | W291 trailing whitespace                                                 |
| 63         | E501 line too long (85 > 79 characters)                                 | 64         | E501 line too long (87 > 79 characters)                                |
| 69         | E303 too many blank lines (2)                                          | 70         | W291 trailing whitespace                                                 |
| 71         | W293 blank line contains whitespace                                       | 73         | E303 too many blank lines (2)                                          |
| 77         | E303 too many blank lines (2)                                          | 78         | W291 trailing whitespace                                                 |
| 83         | W291 trailing whitespace                                                 | 87         | E231 missing whitespace after ','                                        |
| 89         | E231 missing whitespace after ','                                        | 89         | E501 line too long (84 > 79 characters)                                 |
| 90         | E222 multiple spaces after operator                                       | 90         | E231 missing whitespace after ','                                        |
| 90         | E501 line too long (83 > 79 characters)                                 | 114        | W291 trailing whitespace                                                 |

#### Blog Forms

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 1          | W291 trailing whitespace                                                 | 2          | W291 trailing whitespace                                                 |
| 5          | E201 whitespace after '('                                               | 5          | E202 whitespace before ')'                                              |
| 7          | E501 line too long (122 > 79 characters)                               | 9          | E301 expected 1 blank line, found 0                                     |
| 10         | W291 trailing whitespace                                                 | 11         | E201 whitespace after ''                                                |
| 11         | E231 missing whitespace after ','                                        | 11         | E231 missing whitespace after ','                                        |
| 11         | E501 line too long (127 > 79 characters)                                | 12         | E301 expected 1 blank line, found 0                                     |
| 18         | E302 expected 2 blank lines, found 1                                    | 20         | E225 missing whitespace around operator                                   |
| 23         | E122 continuation line missing indentation or outdented                 | 24         | E122 continuation line missing indentation or outdented                 |
| 25         | E122 continuation line missing indentation or outdented                 | 28         | E211 whitespace before '('                                               |
| 28         | E202 whitespace before ')'                                              | 31         | E501 line too long (105 > 79 characters)                                |
| 42         | W291 trailing whitespace                                                 | 43         | W291 trailing whitespace                                                 |
| 46         | E203 whitespace before '                                                | 49         | E265 block comment should start with '# '                               |
| 52         | E501 line too long (91 > 79 characters)                                 | 55         | W293 blank line contains whitespace                                       |
| 55         | W292 no newline at end of file                                          |            |                                                                         |

#### Blog Admin

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
|  E231      | missing whitespace after ','                                             | 11         | E231 missing whitespace after ','                                        |
| 11         | E231 missing whitespace after ','                                        | 12         | E231 missing whitespace after '                                          |
| 17         | E302 expected 2 blank lines, found 1                                    | 20         | E201 whitespace after ''                                                |
| 22         | E265 block comment should start with '# '                               | 23         | E265 block comment should start with '# '                               |
| 25         | E265 block comment should start with '# '                               | 27         | E302 expected 2 blank lines, found 1                                    |
| 29         | E501 line too long (106 > 79 characters)                               | 29         | E231 missing whitespace after ','                                        |
| 30         | E231 missing whitespace after ','                                        | 31         | E501 line too long (84 > 79 characters)                                 |
| 32         | E501 line too long (121 > 79 characters)                               | 32         | E231 missing whitespace after ','                                        |
| 32         | E231 missing whitespace after ','                                        | 33         | W293 blank line contains whitespace                                       |
| 37         | W391 blank line at end of file                                          |            |                                                                         |

</details>                                      


<details>

<summary>About PeP8 errors</summary>

#### About View

| Error Code | Description                    | Error Code | Description                        |
|------------|--------------------------------|------------|-------------------------------------|
| W291       | trailing whitespace            | E302       | expected 2 blank lines, found 0   |
| E231       | missing whitespace after ','   | W293       | blank line contains whitespace     |
| E305       | expected 2 blank lines after class or function definition, found 1 | W291 | trailing whitespace |
| E302       | expected 2 blank lines, found 0 | W293       | blank line contains whitespace     |
| E501       | line too long (85 > 79 characters) | E265   | block comment should start with '# ' |
| W293       | blank line contains whitespace | E303       | too many blank lines (2)           |
| W291       | trailing whitespace            | E302       | expected 2 blank lines, found 1   |
| W292       | no newline at end of file      |            |                                    |

#### About Models
| Error Code | Description                    | Error Code | Description                        |
|------------|--------------------------------|------------|-------------------------------------|
| E302       | expected 2 blank lines, found 1 | E303       | too many blank lines (2)           |
| W292       | no newline at end of file      |            |                                    |
|            |                                |            |                                    |
|            |                                |            |                                    |

#### About Forms
| Error Code | Description                    | Error Code | Description                        |
|------------|--------------------------------|------------|-------------------------------------|
| W293       | blank line contains whitespace | W293       | blank line contains whitespace     |
| W292       | no newline at end of file      |            |                                    |
|            |                                |            |                                    |
|            |                                |            |                                    |

</details>

<details>
<summary>Main App PeP8 errors</summary>

## Main View

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 7          | E302 expected 2 blank lines, found 0                                    | 11         | E305 expected 2 blank lines after class or function definition, found 1 |
| 15         | E302 expected 2 blank lines, found 0                                    | 17         | W292 no newline at end of file                                          |

## Main Urls

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 27         | E231 missing whitespace after ','                                        | 28         | W293 blank line contains whitespace                                       |

## Main Settings

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 19         | W291 trailing whitespace                                                 | 20         | W293 blank line contains whitespace                                       |
| 31         | E265 block comment should start with '# '                               | 31         | E501 line too long (82 > 79 characters)                                 |
| 35         | E265 block comment should start with '# '                               | 37         | E501 line too long (128 > 79 characters)                                |
| 37         | E231 missing whitespace after ','                                        | 61         | E265 block comment should start with '# '                               |
| 62         | E265 block comment should start with '# '                               | 84         | E303 too many blank lines (5)                                          |
| 123        | E265 block comment should start with '# '                               | 128        | E265 block comment should start with '# '                               |
| 137        | W293 blank line contains whitespace                                       | 146        | E501 line too long (91 > 79 characters)                                 |
| 149        | E501 line too long (81 > 79 characters)                                 | 152        | E501 line too long (82 > 79 characters)                                 |
| 155        | E501 line too long (83 > 79 characters)                                 | 167        | E265 block comment should start with '# '                               |
| 178        | W291 trailing whitespace                                                 | 182        | E122 continuation line missing indentation or outdented                 |
| 183        | E122 continuation line missing indentation or outdented                 | 188        | E303 too many blank lines (3)                                          |
| 194        | E501 line too long (80 > 79 characters)                                 | 201        | W391 blank line at end of file                                           |

</details>

<details>
<summary>ENV file PEP8 errors</summary>

#### ENV File

| Error Code | Message                                                                 | Error Code | Message                                                                 |
|------------|-------------------------------------------------------------------------|------------|-------------------------------------------------------------------------|
| 1          | E501 line too long (158 > 79 characters)                               | 6          | E501 line too long (161 > 79 characters)                               |
| 9          | E501 line too long (103 > 79 characters)                               | 11         | E501 line too long (109 > 79 characters)                               |
| 19         | E265 block comment should start with '# '                               | 19         | E501 line too long (91 > 79 characters)                                |
| 20         | E265 block comment should start with '# '                               | 20         | E501 line too long (80 > 79 characters)                                |
| 22         | E265 block comment should start with '# '                               | 23         | E265 block comment should start with '# '                               |
| 24         | W391 blank line at end of file                                          |            |                                                                         |
</details> 


## Lighthouse

* Most of my light house score was in this range as seen below. 

![Lighthouse](/static/readme/images/homelight.png)

<details>
<summary>Lighthouse image of pages</summary>

* I added some of them but not all as the results where all similar.

#### Home

* [Lighthouse Home](/static/readme/images/homelight.png)
* [Lighthouse Home mobile](/static/readme/images/homelightmobile.png)

#### About 

* [Lighthouse About](/static/readme/images/aboutlight.png)
* [Lighthouse About](/static/readme/images/aboutlightmobile.png)

#### Profile

* [Lighthouse Profile](/static/readme/images/profilelight.png)
* [Lighthouse Profile Mobile](/static/readme/images/profilelightmobile.png)

#### Profile Edit 

* [Profile Edit ](/static/readme/images/profileeditlight.png)
* [Profile Edit mobile ](/static/readme/images/profilelighteditmobile.png)

#### My Blog 

* [My Blog ](/static/readme/images/mybloglight.png)
* [My Blog mobile ](/static/readme/images/mybloglightmobile.png)

</details>

[Back to Table of Contents](#table-of-contents)

## HTML Validation

* I used the [W3C Validator](https://validator.w3.org/)
* They managed to clear the errors I found from the validator on all the links.

![HTML](/static/readme/test-image/html-test/validator-w3-success.png)

<details>
<summary>links validated success </summary>

* [Profile](/static/readme/test-image/html-test/userprofilesuccess.png)
* [Profile Edit](/static/readme/test-image/html-test/profile_edit.png)
* [Delete Profile](/static/readme/test-image/html-test/deleteprofile.png)
* [Password Change](/static/readme/test-image/html-test/profilepasswordchange.png)
* [Password Reset](/static/readme/test-image/html-test/password-reset.png)
* [Home Page](/static/readme/test-image/html-test/homepage.png)
* [MY Post](/static/readme/test-image/html-test/my-post.png)
* [Post Edit](/static/readme/test-image/html-test/postedit.png)
* [Post Delete](/static/readme/test-image/html-test/deletpostvalidation.png)
* [Post Detail](/static/readme/test-image/html-test/postdetail.png)
* [Comment Edit](/static/readme/test-image/html-test/comment_editsuccess.png)
* [Contact_Kayaker](/static/readme/test-image/html-test/about-contact.png)
* [HTML About Page](/static/readme/test-image/html-test/aboutpagesuccess.png)

</details>


## CSS Validation

* MY custom CSS was validated using [W3C Jigsaw validation](https://jigsaw.w3.org/css-validator/)service. 

<details>
<summary>CSS success image</summary>

![CSS](/static/readme/test-image/success-css.png)

</details>
[Back to Table of Contents](#table-of-contents)

## Java Script 

* I used [jsHint](https://jshint.com/) for testing the JS in my static file 
* Removed all the warnings and errors.
* Undefinded variables and unused variables remained.
* I tried to remove these as well but ended up crashing my app features and decided to leave them as they are no risk. 

![JS](/static/readme/test-image/jshint.png)

<details>
<summary>jsHInt error summary </summary>

#### JS Errors

| Line | Error Message                                                           | Line | Error Message                                                           |
|------|-------------------------------------------------------------------------|------|-------------------------------------------------------------------------|
| 1    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 2    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 3    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 4    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 6    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 7    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 8    | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 21   | 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 21   | 'for of' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 22   | 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6'). |
| 23   | 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 24   | 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 24   | 'template literal syntax' is only available in ES6 (use 'esversion: 6'). | 27   | 'template literal syntax' is only available in ES6 (use 'esversion: 6'). |
| 46   | 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6'). | 48   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 49   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 56   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 57   | 'template literal syntax' is only available in ES6 (use 'esversion: 6'). | 64   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 71   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). | 72   | 'template literal syntax' is only available in ES6 (use 'esversion: 6'). |
| 73   | 'template literal syntax' is only available in ES6 (use 'esversion: 6'). | 77   | 'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). |
| 82   | 'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6'). |      |                                                                         |

| Type | Variable |
|------|----------|
| Undefined | 7 bootstrap |
| Unused | 8 deleteButtons |
</details>

## Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.
<details>
<summary>Manual Testing results </summary>

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication loads the log in page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the About button on the nav bar loads the About page.
| &check; | Clicking While in the About page clicking on the contac us link loads the contact page.
| &check; | Clicking the Register link loads the Register page
| &check; | Clicking the Log In link loads the Log In page 
| &check; | Clicking In the Log In link clicking on the forget password link loads password reset.  
| &check; | Clicking on the Post title loads the review detail page
| &check; | In Post details view the user has no access to update post.
| &check; | In the details view the user cannot create a comment or delet.
| &check; | Clicking the Facebook link in the footer area opens Facebook link. 
| &check; | Clicking the X link in the footer area opens X link . 
| &check; | Clicking the You Tube in the footer area opens You Tube link.
| &check; | Clicking the search field and serching for Author,Body,Excerpt,Title works. 

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | User cannot access Admin Panel without being staff member
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and lists all posts
| &check; | Clicking the About button on the nav bar loads the About page.
| &check; | Clicking While in the About page clicking on the contac us link loads the contact page.
| &check; | Clicking in the Profile page loads the Profile page.
| &check; | While in the Profile page clicking on the button Password change loads the page to change password.
| &check; | While in the Profile page clicking on the button Profile Edit loads the page to edit profile.
| &check; | While in the Profile Edit page clicking on the button delete Profile Picture deletes profile picture.
| &check; | While in the Profile page clicking on the button Profile Delete loads confirm page and then when confirmed deletes profile.
| &check; | After it  deletes profile a success message is displayed or error message if not.
| &check; | In the detail post view or the home page will show buttons if user is the author of post.
| &check; | In the detail post view the logged in user can comment underneath a post.
| &check; | When user submits a comment a confirmation message is being shown on the page
| &check; | In the detail view the logged in user can update/delete the comments written by themselves.
| &check; | Clicking the update button the comment text will show in the comment box.
| &check; | Clicking the delete button loads the delete comment confirm message page.
| &check; | In the detail view the logged in user can Favorite/unfavorite posts.
| &check; | In the detail view the logged in user has full CRUD for the post written by themselves.
| &check; | Clicking the edit button in My Blog nav link view loads the edit btn and page.
| &check; | Clicking the delete button in the detail view loads the delete post confirmation page
| &check; | Clicking the My Blog nav link in the logged in user nav bar shows the logged in users posts
| &check; | While in the My Blog link the logged in user can see there drafts and published posts.
| &check; | In the logged in user menu the Admin Area is not visible
| &check; | Clicking the X link in the footer area opens X link . 
| &check; | Clicking the You Tube in the footer area opens You Tube link.
| &check; | Clicking the search field and serching for Author,Body,Excerpt,Title works. 

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | The Admin Panel is access b typing /admin
| &check; | Deleting a Profile works on the Admin Panel
| &check; | Deleting a Post works on the Admin Panel
| &check; | Deleting a Comment works on the Admin Panel
| &check; | Changing an email of any user works in the admin bar
| &check; | Changing a password of any user works in the admin bar
| &check; | Deleting a Profile will delete their posts, comments and email and logout the user before delet.

 Status | **Create A Post - User Logged In**
|:-------:|:--------|
| &check; | Title field is required
| &check; | Title field does not accept empty field
| &check; | Title field does not accept just spaces
| &check; | Featured Image is not required
| &check; | Body field is required
| &check; | Body field does not accept empty field
| &check; | Body field has to have 100 characters.
| &check; | Excerpt is not required
| &check; | Excerpt auto summorises the text.
| &check; | Status field defaults to Draft
| &check; | Posting as shows name of author
| &check; | If no image is selected a default is provided.
| &check; | **Home** page with a success message is displayed when the user submits the post

Status | **Create A New User - User Logged Out**
|:-------:|:--------|
| &check; | Username field is required
| &check; | Username field does not accept empty field
| &check; | Email field does not accept just spaces
| &check; | Email field is optional
| &check; | Password field is required does not accept empty field
| &check; | Success message is displayed when the user creates a new user
| &check; | Error message with corresponding info when wrong input is submitted


Status | **Profile Page - User Logged In**
|:-------:|:--------|
| &check; | The default profile info is seen on the profile page (Field not provided).
| &check; | The profile success message or error is displayed when the user submits the profile form.
| &check; | A new user has CRUD on there profile and posts, like and crud on comment after registering.

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Multi Device Mockup Generator](https://techsini.com/multi-mockup/).

| Desktop    | Display <1200px       | Display >1200px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | iPad Air              | Asus Zenbook Fold  | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S8+/S20 Ultra  | iPhone XR/12Pro/14 Pro Max | Pixel 7 / 7 Pro      |
|------------|-----------------------|----------------------------|----------------------|
| Render     | pass                  | pass                       | pass      | pass     |
| Images     | pass                  | pass                       | pass      | pass     |
| Links      | pass                  | pass                       | pass      | pass     |

### Browser Compatibility
* Google Chrome Version 
* Mozilla Firefox 
* Microsoft Edge 
</details>
 
[Back to Table of Contents](#table-of-contents)

- All manual testing was done with DEBUG = False in the settings.py file.


* **All known bugs have been fixed**

## Fixed bugs

| **Bug** | **Fix** |
| --- | --- |
| Bug1: Heroku log= Mis-cased procfile detected; ignoring. to Heruko | Rename it to Procfile to have it honored as it is case sensitive |
| Bug2: deployment was an error on the Heroku app =Bad Request (400). | I forgot to add the Heruko site to the allowed hosts.
| Bug3: Forbidden (403)CSRF verification failed. Request aborted. | Added Heroku to the  CSRF_TRUSTED_ORIGINS in settings 
| Bug4: The model Post is already registered in the app blog. |  Removed the duplicate admin.register(post)
| Bug5: The drop-down list in the Django admin app was showing the ID and not the author's name. | Removed this incorrect code I created raw_id_fields = ['author',] which returned it to its stock feature a drop-down list.
| Bug6: admin.E108 The value of 'list_display[1]' refers to 'first-name', which is not a callable, an attribute of 'UserProfileAdmin', or an attribute or method on 'blog.UserProfile'. | changed the code from first-name to first_name as per my code.
| Bug7: RelatedObjectDoesNotExist at /accounts/login/User has no user profile.Exception Type:  RelatedObjectDoesNotExist | Accessed the manage.py shell and imported the UserProfile, testing after with the shell. Reason the model was changed and not synced with the database.
|Bug8:TemplateSyntaxError at /user_profile/Could not parse the remainder:|I had extra curly braces,changed it to this <img src="{% static 'images/default_profile_picture.jpg' %}"
|Bug9:NoReverseMatch at /about/ Reverse for 'contact_success' not found.| It needed to include URLs path('about/', include('about.URLs))

[Back to Table of Contents](#table-of-contents)

## Unfixed Bugs 

| Bug                     | Status      | Why                                                                 |
|------------------------|-------------|---------------------------------------------------------------------|
| CSRF verification failed | Unfixed     | This is a known problem ; all resources, including tutor support, acknowledge that this is a known Django issue. |
* This bug is when you login somtimes but when you press the backspace yit shows you are logged in.

## Creating the Django app hello

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and unicorn: `pip3 install django gunicorn`
6. Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url psycopg2`
7. Create a file for requirements: in the terminal window type `pip freeze --local > requirements.txt`
8. Create a project: in the terminal window type django-admin start project your_project_name
9. Create app: in the terminal window type python3 manage.py start app your_app_name
10. Add the app to the list of installed apps in the settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal window type python3 manage.py and run the server
13. If the app has been installed correctly the window will display The install worked successfully! Congratulations!

[Back to Table of Contents](#table-of-contents)

## Deployment of This Project

* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labeled New in the top right corner and from the drop-down menu select Create New
App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click on resources and select Heroku Postgres database
7. Click Reveal Config Vars and add a new record with SECRET_KEY
8. Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
9. Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
10. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
11. Next, scroll down to the Buildpack section click Add Buildpack select Python, and click Save Changes
12. Scroll to the top of the page and choose the Deploy tab
13. Select Github as the deployment method
14. Confirm you want to connect to GitHub
15. Search for the repository name and click the connect button
16. Scroll to the bottom of the deploy page and select the preferred deployment type
17. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub

[Back to Table of Contents](#table-of-contents)

# Deployment
<details>
<summary>Deployment from terminal to Heroku</summary>

### Helpfull guide links 

[Django](https://docs.djangoproject.com/en/5.1/topics/install/)
[Django Central](https://djangocentral.com/building-a-blog-application-with-django/#pre-requirements)

* A small note: This is a simple guide of how to get the app up and running.
* Should certain section not seem clear there is a large number of recources that can clarify the below steps if not clear.

The project was deployed to [Heroku](https://www.heroku.com). To deploy a project, these are the steps:

1. Begin by creating a GitHub repository I used this template [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template). Navigate to template and select use. THis was the step I used you can create this in a differant way.

2. 'Create Repository From the Template.

3. After the repository is created, click on 'Gitpod'.

4. Install Django by entering this command in the terminal:

* ```pip3 install Django~=4.2.1``` 
* Best is to see what is the latest verstion and if compatible with the software you plan to install.

5. Generate a requirements file using the following command:

* ```pip3 freeze --local > requirements.txt``` - This will create the requirements.txt file and adds required libraries to it. This command needs to exectuted every time a new libary gets added to the project.

6. Create your project:

* ```django-admin startproject YOUR_PROJECT_NAME .``` - "YOUR_PROJECT_NAME" is the name you choose for your project.

7. Create your application using:

* ```python3 manage.py startapp APP_NAME``` - This will create your application with the name "APP-NAME"

8. Add your local server to "ALLOWED_HOSTS" in the settings.py file. For this you need to run the command

* ```python3 manage.py runserver``` - This runs the server. This will give you an error message "DisallowedHost at /", following the link of your local server. Copy this link and add it in your settings.py file.
* While in the settings.py file, also add your newly created app in the "INSTALLED_APPS" section at the bottom of the list. In the picture, the first app is called "APP".

9. To get the code ready for deployment, gunicorn needs to be installed and added to the requirements with the following commands:

* ```pip3 install gunicorn~=20.1``` - This installs gunicorn
* ```pip3 freeze --local > requirements.txt``` - This will add gunicorn to the requirements.txt file

10. Create a file in the root directory named "Procfile" and add the nessesary lines to the settings.py file:

- Procfile:
* ```web: gunicorn "proejec_name".wsgi``` - "project_name" stands for the name of your project
- settings.py:
* ```DEBUG = False``` - This is the debug line in the settings.py file. It is very important that debug is never set to "True" on a deployed webpage for security reasons. While in development, DEBUG should be set to "True"
* ```,'.herokuapp.com'``` needs to be added to the "ALLOWED_HOSTS" section in the settings.py file, so that heroku has the permission to access the project.

11. Now it is time to create the application on Heroku:

* Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

* In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

12. On Heroku, enter a unique application name, choose your region, and click 'Create app':

13. I used thePostgres database provided by Code Institute, [PostgresSQL](https://dbs.ci-dbs.net/) in the LMS course material.

* Press "Reveal Config Vars" and add "DATABASE_URL" as key and enter the postgres URL, which has been sent by email, as the value.
* Addistionally, add the "DISABLE_COLLECTSTATIC" key with a value of "1" as a second config var. This is nessesary for the later implementation of the Cloudinary API.

14. In GitPod, create an env.py file in the top-level directory with the following content:

* ```import os``` - This imports the os library
* ```os.environ("DATABASE_URL", "postgres://*********************")``` - This sets database variable to your PostgresSQL database.
* ```os.environ("SECRET_KEY", "actual_secret_key")``` - You can create your own key with a webpage like [RandomKeyGen](https://randomkeygen.com/).
* if using the Code Institute template, the env.py file should already be in the "gitignore" file, if not, it has to be added manually.

15. Add your secret key to Heroku's Config Vars and your env variables used: Look at step 13

16. In settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

17. Replace the insecure secret key in settings.py with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

18. Comment out the old database settings and add the link to DATABASE_URL since the project does not use the standart sqlite3 database. 

```DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}```

18. Save all your fields and migrate the changes with the following commands:

```python3 manage.py migrate```

19. Set up Cloudinary for static file storage: After creating a Cloudinary account, you can copy the API Environment Variable from the Cloudinary dashboard.

20. In the env.py file, add the Cloudinary url (it's very important that the url is unaltered):

```os.environ.setdefault("CLOUDINARY_URL", "cloudinary://*********************************")```

21. In the Config Vars of heroku, add the Cloudinary url (CLOUDINARY_URL as the key, the actual url as the value). 

22. In the settings.py file, the Cloudinary Libraries have to be added to the installed apps. The correct order is very important.

23. In the bottom of settings.py, add additional settings for static file management:

24. The next step is to link the file to the Heroku templates directory:

25. Now edit the templates directory to "TEMPLATES_DIR" in the teamplates array.

26. Some more files are needed before deploying:

* Create 2 folders in the top level directory: **static** and **templates**
* The **static** folder will include all CSS and JS files as well as images.
* The **templates** folder will include the "base.html" file, as well as all django related templates.

27. Make sure that all the files are saved, then enter the following lines in the console for the first commit and push to Github:

* ```python3 manage.py collectstatic ``` 
* ```git add .```
* ```git commit -m "Deployment commit"```
* ```git push```


30. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

31. Scroll down to the manual deployment section and click 'Deploy Branch'.

The live link to the site on Heroku an be found [Kayak Blog](https://kayak-blog-pp4-1054055911f7.herokuapp.com/). And the Github repository can be found [github](https://github.com/Marceillo/kayak-blog-pp4).

#### Extra variables added to the env file.

* The below variables where added after the intial deploment 
* ```os.environ.setdefault("EMAIL_HOST_PASS", "your_email_password")``` sets the default values for the email host user and password environment variables. Which are used to configure the email sending functionality for the forgot password feature when deploying your application to Heroku.

## Final Deployment 

1. Create a runtime.txt `python-3.8.13`
2. Create a Profile `web: gunicorn your_project_name.wsgi`
3. When development is complete change the debug setting to: `DEBUG = False` in settings.py
4. In Heroku settings, delete the config vars for `DISABLE_COLLECTSTATIC = 1`

</details>

[Back to Table of Contents](#table-of-contents)

## Forking This Project

* To fork this project by following the steps below:

1. Open [GitHub](https://github.com/hughes84/my-blog-pp4.git)
2. Find the 'Fork' button at the top right of the page
3. Once you click the button the fork will be in your repository

## Cloning This Project

* Clone this project by following the steps:

1. Open [GitHub](https://github.com/Marceillo/kayak-blog-pp4).
2. You will be provided with three options to choose from: HTTPS, SSH, or GitHub CLI. Click the clipboard icon to copy the URL of your preferred option.
3. Once you click the button, the fork will be in your repository (if you chose to fork it).
4. Open a new terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type `git clone` followed by pasting the URL copied in step 2.
7. Press 'Enter' to clone the project.

[Back to Table of Contents](#table-of-contents)

To clone and set up this project, follow these steps:

1. When you are in the repository, find the "Code" tab and click it.
2. To the left of the green "Code" button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change the directory to the location where you want the cloned directory to be created.
4. Type `git clone`, and then paste the URL that you copied from GitHub. Press 'Enter' to create a local clone.

5. To get the project to work, install the required dependencies using the command below:

   ```bash
   pip3 install -r requirements.txt
6. This step is to set up the environment file so that the project knows what variables that needs to be used for it to work. Environment variables are usually hidden due to sensitive information. It's very important that you don't push the env.py file to Github (this can be secured by adding env.py to the .gitignore-file). The variables that are declared in the env.py file needs to be added to the Heroku config vars. Don't forget to do necessary migrations before trying to run the server.

* ```python3 manage.py migrate``` - This will do the necessary migrations.
* ```python3 manage.py runserver``` - If everything i setup correctly the project is now live locally.


## Credits

* I have used differant  website and content during this process I found that dajango documentation was the best and the more common sites like stack overflow.
* I took insperation with the readme structure from the LMS readme and added more to the readme.
* Took some inspiration from the readme files below and adjusted it to meet my project.
  [Marcus Erikssons PP4](https://github.com/worldofmarcus/project-portfolio-4/blob/main/README.md#existing-features) 
* I started the project with the help of the LMS as a starting point and one base template then changed it to meet the project needs. 

* [django-extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
* [Coolors web site](https://coolors.co/palettes/trendin)
* [Book on django](https://www.amazon.de/-/en/Antonio-Mel%C3%A9-ebook/dp/B0CPN3H5YW#:~:text=Django%205%20By%20Example%20is,step%2Dby%2Dstep%20approach)
* [examples of projects](https://codeinstitute.net/de/student-projects/https://github.com/hogbergmarkus/golfers-dream)  
* [guide to the Github Agile Tool](https://www.youtube.com/watch?v=U_dMihBgUNY&list=PL_7334VduOHsrWzhu5Ta2lrkp016kcBWY&index=34)
* [ERD youtube](https://www.youtube.com/watch?v=xsg9BDiwiJE)
* [User account create Django](https://youtu.be/Ev5xgwndmf)
* [Website for django blog](https://djangocentral.com/building-a-blog-application-with-django/#database-models)
* [Website stackoverflow](https://stackoverflow.com)
* [Forms stackoverflow](https://stackoverflow.com/questions/1727564/how-to-create-a-userprofile-form-in-django-with-first-name-last-name-modificati)
* [Forgot Password](https://stackoverflow.com/questions/67545932/how-can-i-send-a-reset-password-email-on-django)
* [Logo design](https://logo.com/dashboard/your-logo-files)
* [Images and mp4 video used pexels](https://www.pexels.com)
* [Images used unsplash](https://unsplash.com/)
* [widgets in djano used in forms blog ](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/)
* [search function](https://blog.csdn.net/bbwangj/article/details/98026817)
* [Django documentation](https://docs.djangoproject.com/)
* [Django Queryset API](https://docs.djangoproject.com/en/stable/ref/models/querysets/)
* [Django Pagination](https://docs.djangoproject.com/en/stable/topics/pagination/)
* [Django Q objects](https://docs.djangoproject.com/en/stable/topics/db/queries/#complex-lookups-with-q-objects)


temp email 
https://temp-mail.org/en/

### Content

* [YouTube Graph Models](https://www.youtube.com/watch?v=qzrE7cfc_3Q&t=357s)
* [You Tube link](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
* [Youtube Bootstrap](https://www.youtube.com/watch?v=-qfEOE4vtxE)


## Acknowledgements

* I used at first the the structure layout of the lms readme and added more to it.
 

[Back to Table of Contents](#table-of-contents)
