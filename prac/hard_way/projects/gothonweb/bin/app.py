import web

urls = (
	'/(.*)', 'hello'
)

app = web.application(urls, globals())
db = web.database(dbn='postgres', user='username', pw='password', db='dbname')
render = web.template.render('templates/')

class hello:
	def GET(self, name):
#		greeting = "Hello World"
#		return render.index(greeting = greeting)
#		print render.hello('haha')
#		i = web.input(name=None)
		return render.hello(name)

if __name__ == "__main__":
	app.run()
