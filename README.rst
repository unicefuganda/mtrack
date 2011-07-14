Mtrack
======
Mtrack is a repository containing additional code to integrate many of the previous mhealth functionality found within CVS (http://www.github.com/daveycrockett/rapidsms-cvs), FIND (http://ugmoh.buildafrica.org), and the soon-to-be-developed MotherReminder system, in an attempt to create a wholistic Mhealth suite.

Insta
This is a RapidSMS project to reinforce existing logistics management systems through the use of text messaging. 

Requirements
============
This has only been tested on Linux: Ubuntu Lucid Lynx 10.0.4 LTS

* git
* postgres
* pip

You can install all of the above by running:
> sudo apt-get install git-core postgresql python-psycopg2 couchdb

Install Django 1.2.5. Don't use apt-get on Lucid, it'll give you 1.1
Install pip >=0.6.3. Don't use apt-get on Lucid, it'll give you 0.3.1

Installation
============
* git clone git://github.com/unicefuganda/mtrack.git
* cd mtrack
* pip install -r pip-requires.txt
* git submodule init
* git submodule update
* cd mtrack_project
* cp localsettings.py.example localsettings.py
* ./manage.py syncdb
* ./manage.py migrate
TODO: explain how to load fixtures here
* update any relevant settings in settings.py or localsettings.py
* ./manage.py runserver 

