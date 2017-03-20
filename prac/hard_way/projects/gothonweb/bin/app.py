import web

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class Index:
	def GET(self):
            form = web.input(name="Nobody", greet=None)
            if form.greet:
                greeting = "Hello, %s and %s" %(form.name, form.greet)
                return render.hello(greeting = greeting)
            else:
                return "Error, we need a greet name"

if __name__ == "__main__":
	app.run()
