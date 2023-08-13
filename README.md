# Blog_app-

--> This is a blogging app made using flask, postgres and render as the hosting service.

--> In this app, you can login or register and create a new account. 

--> Can create Blog posts which will get listed in the website.

--> You can also update or delete your Blog posts.

--> You can also reset the password if forgot but only after setting below variables in your secret file:
EMAIL_USER=your_gmail
EMAIL_PASS=your_app_password_for_your_google_account(setup manually)
MAIL_PORT=587
MAIL_SERVER=smtp.googlemail.com

Here is the live link:
    https://flask-blog-app-ccj2.onrender.com

IF the link is broken, contact me up Keshavsharma1419@gmail.com.

Instructions to clone:
  - Copy the repo link and clone it one your pc using    git clone repo_link
  - Install a virtual env using    python -m pip venv env
  - Activate the env using env/scripts/activate  (if on windows)
  - Install all the requirements using   python -m pip install -r requirements.txt
  - Add the required env variables to a secret file (.env):
FLASK_DEBUG=False
SECRET_KEY=your secret key by secrets package
SQLALCHEMY_DATABASE_URI= sqlite:///site.db  or  any  dbms you want to connect(link)
  - In the terminal, run python run.py and app will start
If any problem in running app, contact me here (Keshavsharma1419@gmail.com).



