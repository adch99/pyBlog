import web
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
        return render.template(render.home(posts))

class Add(object):
    """Add an article to the site."""
    def GET(self):
        return render.template(render.add())
            
    def POST(self):
        form = web.input(title=None, content=None, image=None)

        print form #debug
        print form.content #debug
        
        if form.image == u"": form.image = None
        
        if form.title and form.content:
            global curPost
            curPost = manage.Post(
                    form.title,
                    form.image,
                    markdown(form.content)
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
            curPost.content
        )
        print args
        return render.template(render.preview(*args))
      
    def POST(self):
        form = web.input(confirm=False, reject=False)
        
        # Edge case scenario where "confirm and reject" is true or
        # "not confirm and not reject" is true
        try:
            pass
        except "Something is amiss":
            pass
            
        
        if form.reject:
            web.seeother("/add") 
            # Need to add functionality so that the user can edit the 
            # same data that they just wrote rather than showing them
            # empty fields
            
            # Since we are emptying curPost after adding it will be a
            # good move to check if it has something before rendering
            # the "/add" page.
            
        if form.confirm:
            # Add the new post
            manage.addPost(curPost)
            # Empty the cache
            curPost = None
        
class Manage(object):
    """Manage added articles:
    * Remove articles
    * Edit articles (to be developed later)"""
    def GET(self):
        if manage:
            return render.manage()


if __name__ == "__main__":
    app.run()
