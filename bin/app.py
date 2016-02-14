import web

from blog import manage

urls = (
    "/home", "Home",
    "/add", "Add",
    "/manage", "Manage",
)

app = web.application(urls, globals())
render = web.template.render("templates/", "template.html")

class Home(object):
    """The Home Page with the articles in
    descending chronological order."""
    def GET(self):
        posts = []
        for title in manage.getPostList():
            posts.append(manage.getPost(title))
        return render.home(posts)

class Add(object):
    """Add an article to the site."""
    def GET(self):
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
        

if __name__ == "__main__":
    app.run()
