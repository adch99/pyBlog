#!/bin/python

from nose.tools import *
import os
# Testing the IO part i.e. saving the post as a pickle 
# and loading it back for rendering.
# As well as the user input being processed properly.

from blog import manage as mg
from bin import app
import web
from bs4 import BeautifulSoup

def setup():
    if os.path.isfile("data/Test_Title"):
        os.remove("data/Test_Title")

def test_io_without_img():
    args = ("Test Title",
            "This is a test text. \nThis should be working."
            )
    p = mg.Post(*args)
    mg.addPost(p)
    out = mg.getPost(p.title.replace(" ","_"))
    assert_equal(p.title, out.title)
    assert_equal(p.content, out.content)
    assert_equal(p.img, out.img)
    
def test_home():
      """/home is not working"""
      resp = app.app.request("/hello")
      assert_equal(resp.status, "200 OK")
      assert "main-container" in resp.data
    
def test_add_without_img():
    """Post is processed incorrectly without image."""
    data = {
        "title": u"My title",
        "content": u"This is *some content.* And here is some **more**.",
        "image": u""
    }
    resp = app.app.request("/add", method="POST", data=data)
    assert_equal(resp.status, "200 OK")
    print "open error:", resp
    soup = BeautifulSoup(resp.data, "html.parser")
    
    maincontainer = soup.find_all("div", class_="main-container")[0]
    assert_equal(maincontainer.h1.text, u"My Title")
    assert_equal(maincontainer.p.text, u"This is <em>some content.</em> And here is <strong>more</strong>.")
    assert "img" not in resp.data
    
    
def teardown():
    if os.path.isfile("data/Test_Title"):
        os.remove("data/Test_Title")