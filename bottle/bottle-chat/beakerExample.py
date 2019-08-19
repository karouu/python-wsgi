import bottle
from bottle.ext import beaker

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = beaker.middleware.SessionMiddleware(bottle.app(), session_opts)

@bottle.route('/test')
def test():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = s.get('test',0) + 1
    s.save()
    return 'Test counter: %d' % s['test']

bottle.run(host='0.0.0.0', port='8081',app=app)
