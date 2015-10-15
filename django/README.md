
Started this project on Debian Stretch like:

  sudo apt-get install python3-django python3-djangorestframework virtualenv

  virtualenv env
  source env/bin/activate

  django-admin startproject tutorial
  cd tutorial
  django-admin startapp quickstart
  cd ..

(I'm not sure virtualenv is really needed here.)
