#!/bin/python

from nose.tools import *
import os
# Testing the IO part i.e. saving the post as a pickle 
# and loading it back for rendering.

from blog import manage as mg

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
    
def teardown():
    if os.path.isfile("data/Test_Title"):
        os.remove("data/Test_Title")
