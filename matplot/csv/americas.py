import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Centeral America', ['bz', 'cr', 'ft', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl','co','ec','gf',
    'gy','pe', 'py','sr','uy','we'])

wm.render_to_file('/tmp/americas.svg')
