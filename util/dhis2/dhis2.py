"""
Script to proof-of-concept DHIS2 integration.
Here, we're just trying to get some fake HMIS033B data into apps.dhis2.org

"""
from post import post_authenticated_file

response = post_authenticated_file('payload.xml', "http://apps.dhis2.org/demo/api/dataValueSets", 'admin','CHANGEME', headers={"Content-Type":"application/xml"})
# todo: change the payload for the go.ug site
#response = post_authenticated_file('payload.xml', "http://hmis1.health.go.ug/api/dataValueSets", 'pilot','CHANGEME', headers={"Content-Type":"application/xml"})
print response
