# BrewFind - Django web application 


[![MIT License](https://img.shields.io/github/license/Rmariner25/moengage_brewery)](https://github.com/Rmariner25/moengage_brewery/blob/main/LICENSE)

A Django web application to query Open Brewery DB, view, and post reviews. 

## Current features

* Users can query breweries by all, by_name, by_city, by_postal, and by_type params.
* Search autocomplete feature.
* Users can rate breweries and post reviews.
* Google maps on brewery-details page
* Caching breweries data and search results to optimize page response time.
* Advance login features such as reset password/forgot password.
* User can edit their profile.


## Screenshots

Brewery-details page:

![Brewery-details page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/details_page.jpg)
<br>

Reviews section:
![Reviews section](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/reviews_section.jpg)
<br>

Search-autocomplete:

![Search-autocomplete](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/search_autocomplete.jpg)
<br>

Search page:

![Search page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/search_page.jpg) 
<br>

Home page:

![Home page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/home_page.jpg) 
<br>

Profile page:

![Profile page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/profile_page.jpg)
<br>

Login page:

![Log-in page](https://github.com/Rmariner25/moengage_brewery/blob/main/Screenshots/login_page.jpg)
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
