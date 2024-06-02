# BrewFind - Django web application 


[![MIT License](https://img.shields.io/github/license/Rmariner25/moengage_brewery)](https://github.com/Rmariner25/moengage_breweryp/blob/main/LICENSE)

A Django web application to query Open Brewery DB, view, and post reviews. 

## Current features

* Users can query breweries based on by_city, by_type, and by_name params (provided they are logged in).
* Users can post reviews.
* Advance login features such as reset password/forgot password.
* User can edit their profile.
* Django-admin for admin site.
* Utilizes AWS RDS (PostgreSQL).

## Screenshots

Brewery-details:

![Brewery-details page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/details_page.jpg)
<br>

Search page (logged in):

![Search page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/search_page.jpg) 
<br>

Home page:

![Home page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/home_page.jpg) 
<br>

Profile page:

![Profile page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/profile_page.jpg)
<br>

Sign-up page:

![Sign-up page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/signup_page.jpg)
<br>
## Configuring AWS RDS 

Adding shortly.

## Running the project locally

### Pre-requisites:

* Make sure you have [Python 3](https://www.python.org/downloads/) and pip installed on your system.

### Steps:

1. First, clone the repository to your local machine: 
  
   ```bash
   git clone https://github.com/Rmariner25/django_web_app.git
   ```
  
2. Then cd into the folder `django_web_app`(base directory):

   ```bash
   cd django_web_app
   ```

3. Install virtual environment and activate it:
* For Windows:
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
   ```
* For Ubuntu Linux:
   ```bash
   sudo apt install virtualenv
   virtualenv -p python3 venv
   source venv/bin/activate
   ```
  
4. Install the dependencies as in `requirements.txt`:
  
   ```bash
   pip install -r requirements.txt
   ```
  
5. Run the development server:</li>

   ```bash
   python manage.py runserver
   ```

6. Now, copy the url http://127.0.0.1:8000 and paste it in your web browser's address bar. 

### Superuser:

7. To log into admin at http://127.0.0.1:8000/admin create a super user:

   ```bash
   python manage.py createsuperuser
   ```