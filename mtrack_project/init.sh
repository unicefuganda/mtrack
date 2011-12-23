./manage.py syncdb --noinput
./manage.py migrate
./manage.py loaddata locations
./manage.py loaddata healthmodels
./manage.py mtrack_init
./manage.py check_script_progress -e 7 -l 20

