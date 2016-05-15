from blog import manage
from bin import app
from tests import utils

from nose.tools import *

# Check whether all urls are OK
def testURLs():
    """One of the URLs seems to be not OK."""
    utils.testResponse("/home", contains="main-container")
    utils.testResponse("/add", contains="form")
