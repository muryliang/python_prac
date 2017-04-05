import web

urls = ("/", "index")

render = web.template.render("templates/")
class index(object) :
    def GET(self):
        greeting = "hello world"
        return render.hello("hello")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
