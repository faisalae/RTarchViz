# RTarchViz

## Introduction

(Real-Time Architectural Visualizations)

Market for 3d assets in Unreal Engine for arch viz

Users can register and then both buy and sell assets using the application

### Target Audience


## Apps
### Account App
Reused accounts app created in one of the Lessons
It included a custom Email Authentication Backend for authenticating users based on email address instead of django's default username. Also, it contained views and templates for login, registration, profile, and logout as well as forms for registration and login.

I extended the app in the following ways:
- Added EditProfileForm that extends forms.ModelForm and allows authenticated user to edit their email, username, name, date of birth, bio, and address. The update profile view passes in the instance of user data as argument to the form which prefills all form fields with correct user information.
- Created change_password view that integrates django's built in PasswordChangeForm to provide a simple password change form available to users. The form is available from user's profile page. The view also updates the session hash appropriately to prevent a pasword change from loggin out the session.
- Removed the app's custom password validation on registration form as django's built in password validation is more sufficient.
- Integrated password reset via email for cases when user forgets their password and cannot login. Also, created custom templates for the password reset stages

#### Password Validation
Using Django's Built in Password validation:
- password can't be too similar to your other personal information. (on password change)
- password must contain at least 8 characters.
- password can't be a commonly used password.
- password can't be entirely numeric.

#### ToDo
- prevent password_reset access to logged in users. Currently using django's built in password reset views and not sure how to do this without rewriting the views using `is_authenticated`
- Split the long registration into two forms or use ajax to split it up for better user experience. As it is now, the registration form requires user to fill in lots of fields in one go. 1st page: email, username, password. 2nd page: bio, dob, address.

#### Issues/Bugs

### Pages App
Static pages like the homepage and about

### Blog
Blog app for latest news and tutorials. Managed only by is_staff (company staff) who can add, edit, and delete posts.

Super User needs to designate the user a staff member in the django admin as well add the user to the STAFF group to have add/edit/delete blog post permissions.

Blog posts use Disqus for comments
#### ToDo:
- Add link to admin from STAFF member profile page.

#### Issues/Bugs
- title model field is unique but case sensitive. Can accept both 'Post 1' and 'post 1' but if both added will get MultipleObjectsReturned exception. (clean title by changing first letters to uppercase except for 'the', 'a', etc.)
- Disqus doesn't seem to be configured correctly or does not work well on localhost. It loads the comments, but doesn't connect with my Disqus API. Try to investigate this once deployed to heroku server. Make sure to change site name in admin.

## Production Deployment

### Heroku
Project is deployed to Heroku and uses a free trier of Postgres add-on for the database.

The project's settings.py contains production specific settings...

#### Live Demo
[https://rtarchviz.herokuapp.com/](https://rtarchviz.herokuapp.com/)

#### Environment Variables
requires setting the following ENVIRONMENT VARIABLES in Heroku Settings:
```
DATABASE_URL=<link to your provisioned Heroku Postgres db or other>
ENV=production
SECRET_KEY=<your django secret key>

```

optional ENVIRONMENT VARIABLES:
```
EMAIL_HOST_USER=<email address>
EMAIL_HOST_PASSWORD=<email password>
```
The above is needed for emailing password recovery links to users. May require changing security settings in your email client. If not set, the password recovery links will be printed to console instead.

#### Packages
Some packages that needed to be inmplemented for Production:
- dj-database-url for Postgresql db connection on Heroku
- gunicorn for serving the app on Heroku
- whitenoise to allow the web app to serve its own static
files

### Travis CI
Travis Continous Integrations is used to test builds before they're deployed to Heroku. Automated test will be implemented to run on builds to make sure app's code is performing as expected to minimize the risk of a broken production app.

## 3rd Party Apps/Packages Used:
- django-bootstrap4: [docs](http://django-bootstrap4.readthedocs.io/en/latest/index.html)

## Other Todo
#### Bootstrap Forms
- disable error message on top of form or change erros to only indicate the form fields that are invalid  (same error messages appear under appropriate form fields)

#### Other
- Create 404 page