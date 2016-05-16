import os
import web
from web.form import Form, Button
from markdown import markdown

from blog import manage


urls = (
    "/", "Home" ,
    "/home", "Home",
    "/add", "Add",
    "/added", "Preview",
    "/manage", "Manage",   
    #"/favicon.ico", "favicon"
)

app = web.application(urls, globals())
render = web.template.render("templates/")
rendertemp = web.template.render("templates/","template.html")

# Globals variables for use throughout program
curPost = None

class Home(object):
    """The Home Page with the articles in
    descending chronological order."""
    def GET(self):
        posts = []
        for title in manage.getPostList():
            posts.append(manage.getPost(title))
            
        posts = manage.sortPostList(posts)
        return render.template(render.home(posts))

class Add(object):
    """Add an article to the site."""
    def GET(self):
        # Empty the cache
        curPost = None
        return render.template(render.add())
            
    def POST(self):
        form = web.input(title=None, content=None, image={})

        #print form #debug
        #print "Content:",form.content #debug
        #print "Image:", form.image, form.image.value #debug
        
        if form.image.value == u"": fname = None
        else:
            #print form.image.filename #debug
            # Check for Extension
            if u"." in form.image.filename:
                extension = u""
                for l in form.image.filename[::-1]: 
                    extension += l
                    if l == u".": break
            else: extension = u""
            
            fname = os.path.join("static", "data", "__images", form.title.replace(" ","_")+extension[::-1])
            #print "fname:", fname, "extension:", extension #debug
            
            # Save the image
            imgfile = open(fname, "wb")
            imgfile.write(form.image.value)
            imgfile.close()
        
        if form.title and form.content:
            global curPost
            curPost = manage.Post(
                    form.title,
                    markdown(form.content),
                    fname
                )
            #print curPost
            web.seeother("/added")
            #return render.template(render.preview(
            #        form.title,
            #        form.image,
            #        markdown(form.content)
            #    ))
            

                
class Preview(object):
    """
    Preview the newly added post and confirm 
    """
    def GET(self):
        #global curPost
        #if curPost.img == u'':
        #    curPost.img = None
        args = (
            curPost.title,
            curPost.img,
            curPost.content,
            Button("Confirm", id="confirm", value="confirm", class_="button"),
            Button("Reject", id="reject", value="reject", class_="button")
        )
        #print args #debug
        return render.template(render.preview(*args))
      
    def POST(self):
        form = web.input() 
        if form[form.keys()[0]] == "confirm": confirm = True
        else: confirm = False
        
        #print "Preview Form Keys:", form.keys() #debug
        #print "Preview form:", form #debug
        #print confirm, reject #debug
              
        if not confirm:
            if curPost.img: os.remove(curPost.img) # Remove the image
            web.seeother("/add") 
            # Need to add functionality so that the user can edit the 
            # same data that they just wrote rather than showing them
            # empty fields
            
            # Since we are emptying curPost after adding it will be a
            # good move to check if it has something before rendering
            # the "/add" page.
            
        if confirm:
            global curPost
            #print curPost.__str__() #debug
            # Add the new post
            manage.addPost(curPost)
            web.seeother("/home")
        
class Manage(object):
    """Manage added articles:
    * Remove articles
    * Edit articles (to be developed later)"""
    def GET(self):
        try:
            return render.manage()
        except:
            web.seeother("/home")

if __name__ == "__main__":
    app.run()
