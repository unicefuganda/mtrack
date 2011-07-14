#from setuptools import setup, find_packages
from setuptools import find_packages
from distutils.core import setup

setup(
    name='rapidsms-mtrack',
    version='0.1',
    license="BSD",

    install_requires = [
        "django",
        'django-eav',
        'django-extensions',
        "django-nose",
        'django-tablib'
        'django-uni-form',
        "djappsettings"
        "djtables",
        "python-dateutil",
        "rapidsms",
        'rapidsms-auth',
        'rapidsms-contact',
        'rapidsms-generic',
        'rapidsms-httprouter',
        'rapidsms-polls',
        'rapidsms-script',
        'rapidsms-unregister',
        'tablib',
        'uganda-common',
        'xlrd',
    ],

    dependency_links = [
        "http://github.com/mvpdev/django-eav/tarball/master#egg=django-eav",
        "http://github.com/daveycrockett/rapidsms-polls/tarball/master#egg=rapidsms-polls",
        "http://github.com/daveycrockett/rapidsms-httprouter/tarball/master#egg=rapidsms-httprouter",
        "http://github.com/daveycrockett/rapidsms-unregister/tarball/master#egg=rapidsms-unregister",
        "http://github.com/mossplix/simple_locations/tarball/master#egg=simple-locations",
        "http://github.com/daveycrockett/rapidsms-polls/tarball/master#egg=rapidsms-polls",
        "http://github.com/mossplix/rapidsms-contact/tarball/master#egg=rapidsms-contact",
        "http://github.com/daveycrockett/rapidsms-generic/tarball/master#egg=rapidsms-generic",
        "http://github.com/daveycrockett/rapidsms-script/tarball/master#egg=rapidsms-script",
        "http://github.com/mossplix/uganda_common/tarball/master#egg=uganda-common",
        "http://github.com/daveycrockett/auth/tarball/master#egg=rapidsms-auth",
    ],

    scripts = [],

    description='The mTrack ACT tracking system deployed in Uganda.',
    long_description=open('README.rst').read(),
    author='UNICEF Uganda',
    author_email='mtrack-dev@dimagi.com',

    url='http://github.com/unicefuganda/mtrack',
    download_url='http://github.com/unicefuganda/mtrack/downloads',

    include_package_data=True,

    packages=find_packages(),
    package_data={'ureport':['templates/*/*.html','templates/*/*/*.html','static/*/*']},
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
