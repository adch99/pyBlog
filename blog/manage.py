#!/bin/python
import os
import pickle

# Contains functions for managing posts of the blog
# It can -
# * Add a post
# * Remove a post
# * Edit a post**

class InvalidPost(Exception):
    """Post given is invalid. It is either False or None."""
    def __init__(self, post):
        print "The Post object is invalid: ", post

class PostDoesNotExist(Exception):
    """Post with given title doesn't exist."""
    def __init__(self, title):
        print "Post \'%s\' doesn't exist" % title

class PostAlreadyExists(Exception):
    """Post with a given filename already exists."""
    def __init__(self, title):
        print "Post with title \'%s\' already exists." % title

#
# Post Class
#
class Post(object):
    """
    Post object containing title, markdownised content and optionally an image.
    """
    # add timestamp
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
            }.__str__()

#
# Post Functions
#

def addPost(post):
    """
    Adds a post to the blog by saving it to the file.
    Returns None if no error.
    """
    try:
        # is it a valid Post?
        if not post: raise InvalidPost(post)
        
        # Does Post with same name already exist?
        path = os.path.join("data", post.title.replace(" ","_"))
        if os.path.isfile(path):
             raise PostAlreadyExists(post.title)
    
    except PostAlreadyExists:
        pass
    
    else:
        # Store Post as pickle in datafile
        datafile = open(path, mode="wb")
        val = pickle.dump(post, datafile)
        datafile.close()
        return val
         
def rmPost(post):
    """
    Removes a post from the blog by removing the file.
    Returns None if no errors.
    """
    
    try:
        path = os.path.join("data", post.title.replace(" ","_")) # In order to avoid confusion with the OS
        if not os.path.isfile(path):
            raise PostDoesNotExist(post.title)
        
    except:
        pass
        
    else:
        return os.remove(path) # deletes file
        
def getPost(title):
    """
    Returns the post with the given title as a Post object. 
    """
    try:
        path = os.path.join("data",title)
        if not os.path.isfile(path):
            raise PostDoesNotExist(title)
            
    except PostDoesNotExist:
        print "PostDoesNotExist"
        pass
        
    else:
        datafile = open(path, mode="rb")
        post = pickle.load(datafile)
        datafile.close()
        return post
        
def getPostList():
    """
    Returns a list of titles of saved Posts.
    Use getPost(title) to get the actual post.
    """
    posts = os.listdir("data")
    return posts
