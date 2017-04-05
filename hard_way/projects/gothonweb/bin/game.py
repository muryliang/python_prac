import web
from gothonweb import map

urls = (
        '/', 'index',
        '/game', 'game',
        )

app = web.application(urls, globals())
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room':None})
    web.config._session = session
else:
    session  = web.config._session

render = web.template.render('templates/', base='layout')

class index(object):
    def GET(self):
        session.room = map.START
        web.seeother('/game')

class game(object):
    def GET(self):
        if session.room:
            return render.show_room(session.room)
        else:
            return render.you_die()

    def POST(self):
        form = web.input(action=None)
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother('/game')
if __name__ == "__main__":
    app.run()
