#!/bin/python
import codecs
import os

# Contains functions for managing posts of the blog
# It can -
# * Add a post
# * Remove a post
# * Edit a post**

'''
class PostDoesntExist(Exception):
    """Post with given title doesn't exist."""
    def __init__(self, title):
        print "Post %s doesn't exist" % title

class PostAlreadyExists(Exception):
    """Post with a given filename already exists."""
    def __init__(self, title):
        print "Post with title %s already exists." % title
'''

class Post(object):

    def __init__(self, title, content, img=None):
        """Generates Post object when title, markdownized content
        and optionally an image source is given."""
        self.title = title
        self.content = content
        self.img = img
        
    def __str__(self):
        return {
            "title": self.title,
            "content": self.content,
            "Image": self.img
            }

def addPost(post):
    """Adds a post to the blog by saveing it to the file."""
    try:
        path = os.path.join("data",post.title)
        if os.path.isfile(path):
             raise PostAlreadyExists(post.title)
        datafile = open(path, mode="w", encoding="utf-8")
    except PostAlreadyExists:
        pass
    else:
        
    
    
def rmPost(post):
    """Removes a post from the blog by removing the file."""
    try:
        path = os.path.join("data", post.title)
        if not os.path.isfile(path):
            raise PostDoesNotExist(post.title)
        # delete_file(path)
        os.remove(path)
        
    except:
        pass
