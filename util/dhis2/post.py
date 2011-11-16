"""
TODO: merge this back into dimagi/utils/post once it's working
"""

from __future__ import absolute_import
import os
from urlparse import urlparse
import httplib
import subprocess
import tempfile
from subprocess import PIPE
from restkit import Resource, BasicAuth

def post_authenticated_data(data, url, username, password, headers=None):
    """
    Post basic authenticated data, using restkit
    """ 
    auth = BasicAuth(username, password)
    r = Resource(url, filters=[auth, ])
    if headers is not None:
        return (r.post(payload=data, headers=headers).body_string(), None)
    return (r.post(payload=data).body_string(), None)
    
def post_authenticated_file(filename, url, username, password, headers=None):
    """
    Post basic authenticated file, using restkit
    """ 
    file = open(filename, "r")
    try:
        return post_authenticated_data(file.read(), url, username, password, headers)
    finally:
        file.close()
    
