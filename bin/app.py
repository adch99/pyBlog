import web

from blog import manage

urls = (
    "/home", "Home",
    "/add", "Add",
    "/manage", "Manage",
    "/favicon.ico", "favicon"
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
        if form.title and form.content:
            return render.template(render.added(form.title, form.content))
        

class Manage(object):
    """Manage added articles:
    * Remove articles
    * Edit articles (to be developed later)"""
    def GET(self):
        if manage:
            return render.manage()

class favicon(object):
    """For serving the favicon.ico"""
    def GET(self):
        return web.seeother("/static/favicon.ico")        

if __name__ == "__main__":
    app.run()
