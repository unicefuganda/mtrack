RapidSMS Uganda Common
======================
This module contains some common utilities used across RapidSMS (applications).

Dependecies
===========
Uganda Common reuses code that can be found in. Include the following on your python/django PATH
- rapidsms (mostly needed for custom template tags, this lets you have on-the-fly features such as tabs)
- dango-eav
- rapidsms-generic (common UI elements in the RapidSMS framework e.g. time slider, map renderer, and lots of others)

Code Structure
==============

* templates (a directory)
* cache_manager.py
* context_processors.py
* forms.py
* reports.py
* utils.py


Features
========
Using Uganda common, the following functions can be re-used across your project. This is a piece by piece teardown
analysis of rapidsms-uganda-common and what you can do with it.

The *cache_manager.py*


The *forms.py* module currently has a class that creates a DateRange form.

The *reports.py* module has utilities that  

The *utils.py* python module has the following awesomeness:

* basic datetime computation with functions that will allow you to calendar related output from
python objects (such as model instances), they include:

    * previous calendar week
    * previous calendar month
    * and a number of others (please use the help() function to learn more about the modules, some inline documentation has
been added)
=======
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
* ./manage.py loaddata locations healthmodels
* ./manage.py mtrack_init 
* update any relevant settings in settings.py or localsettings.py
* ./manage.py runserver 

Vagrant
=======
* git clone git://github.com/unicefuganda/mtrack.git
* cd mtrack
* git submodule init
* git submodule update
* vagrant up
* vagrant ssh
* cd /vagrant
* sudo ./setup

South Specific
==============
Please uncomment the `south` in the `INSTALLED_APPS` list.

* run syncdb
* for first time usage, create a migration
  `./manage.py schemamigration <app_name> --initial`

Next step, is to apply the migration
  `./manage.py migrate <app_name>`

GOTCHAS: If a relation already exists you'll get exception errors informing you about this, so don't worry. Just establish a good team workflow when developing using South.

* for any new changes made to you models (relations) at a "column" and "row" level, you can be a little picky
   `./manage.py schemamigration <app_name> --auto`
 
Available options you have when running migrations on models are

* --initial
* --auto
* --empty
* --add-model
* --add-field
* --add-index

TIP: If you doing this by hand for `n` number of applications is hard, you can always write a script on top of you South to iterative comb through your project directory to do this for you.
