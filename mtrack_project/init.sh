./manage.py syncdb --noinput
./manage.py migrate
./manage.py loaddata locations
./manage.py loaddata healthmodels
./manage.py mtrack_init
