#!/usr/bin/python2
import web

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class Index:
	def GET(self):
            return render.hello_form()

        def POST(self):
            form = web.input(name="Nobody", greet = "Hello", fileUpload={})
            greeting = ":%s: %s:" %(form.greet, form.name)
            web.debug(form['fileUpload'].filename) #filename
            web.debug(form['fileUpload'].value) #filename
            web.debug(form['fileUpload'].file.read()) #filename
#            raise web.seeother('/hello')

            return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()
