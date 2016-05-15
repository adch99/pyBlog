from bin.app import app
from nose.tools import assert_equal

# Test Utility for verifying HTTP requests
def testResponse(url, method="GET", status="200 OK", data=None, contains=None, output=None):
    resp = app.request(url, method=method, data=data)
    
    # check status
    assert_equal(resp.status, status)
    
    # check whether it contains "contains"
    if contains: assert contains in resp.data
    
    # check exact output
    if output: assert_equal(resp.data, output) 
