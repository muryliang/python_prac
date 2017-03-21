import web

urls = (
    '/', 'index'
    )

render = web.template.render('templates/')

class index(object):
    def GET(self):
        name = 'Bob'
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
