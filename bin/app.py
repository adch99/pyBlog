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
        
        if form.title and form.content:
            return render.template(render.added(
                    form.title,
                    form.image,
                    markdown(form.content)
                ))
                
class Preview(object):
    """
    Preview the newly added post and confirm 
    """
        
class Manage(object):
    """Manage added articles:
    * Remove articles
    * Edit articles (to be developed later)"""
    def GET(self):
        if manage:
            return render.manage()


if __name__ == "__main__":
    app.run()
