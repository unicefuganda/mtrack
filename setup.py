<<<<<<< HEAD
from setuptools import setup

setup(
    name='uganda_common',
    version='0.1',
    license="BSD",

    install_requires = ["rapidsms"],

    description='A suite of utility functions for Uganda RSMS deployments.',
    long_description='',
    author='UNICEF Uganda T4D',
    author_email='mossplix@gmail.com',

    url='http://github.com/mossplix/uganda_common',
    download_url='http://github.com/mossplix/uganda_common/downloads',

    include_package_data=True,

    packages=['uganda_common'],

=======
from setuptools import setup, find_packages
from setuptools import find_packages
from distutils.core import setup

setup(
    name='rapidsms-mtrack',
    version='0.1',
    license="BSD",

    install_requires=[
        "django",
        'django-eav',
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
    author_email='mtrack-dev@dimagi.com',

    url='http://github.com/unicefuganda/mtrack',
    download_url='http://github.com/unicefuganda/mtrack/downloads',

    include_package_data=True,

    packages=find_packages(),
>>>>>>> 2557787d6e66fe3c7fc15d9c293660ac2d2236c1
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
<<<<<<< HEAD
    ]
=======
    ],
>>>>>>> 2557787d6e66fe3c7fc15d9c293660ac2d2236c1
)
