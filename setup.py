#from setuptools import setup, find_packages
from setuptools import find_packages
from distutils.core import setup

setup(
    name='rapidsms-mtrack',
    version='0.1',
    license="BSD",

    install_requires=[
        "django",
        'django-extensions',
        "django-nose",
        'django-tablib',
        'django-uni-form',
        "djappsettings",
        "djtables",
        "python-dateutil",
        'tablib',
        'xlrd',
        'psycopg2',
        'django-mptt',
        'python-digest==1.7',
        'django-digest==1.13',
    ],

    dependency_links=[
        "http://github.com/mvpdev/django-eav/tarball/master#egg=django-eav",
    ],

    scripts=[],

    description='The mTrack ACT tracking system deployed in Uganda.',
    long_description=open('README.rst').read(),
    author='UNICEF Uganda',
    #author_email='mtrack-dev@dimagi.com',
    author_email='sekiskylink@gmail.com',

    url='http://github.com/unicefuganda/mtrack',
    download_url='http://github.com/unicefuganda/mtrack/downloads',

    include_package_data=True,

    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
