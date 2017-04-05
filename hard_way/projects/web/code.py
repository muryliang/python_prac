import web

urls = (
    '/', 'index',
	'/add','add'
    )

render = web.template.render('templates/')
db=web.database(dbn='mysql', user='sora', pw='123456', db='dbs')

class index(object):
	def GET(self):
		todos=db.select('todo')
		return render.index(todos)

class add(object):
	def POST(self):
		i = web.input()
		n = db.insert('todo', title=i.title)
		raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
