import web

urls = (
    "/home", "Home",
    "/add", "Add",
    "/manage", "Manage",
)

render = web.template.render("templates/", "layout.html")

class Home(object):
    """The Home Page with the articles in
    descending chronological order."""
    def GET(self):
        if home:
            return render.home()

class Add(object):
    """Add an article to the site."""
    def GET(self):
        if add:
            return render.add()
            
    def POST(self):
        if form.title and form.content:
            return render.added(form.title, form.content)
        

class Manage(object):
    """Manage added articles:
    * Remove articles
    * Edit articles (to be developed later)"""
    def GET(self):
        if manage:
            return render.manage()
        


