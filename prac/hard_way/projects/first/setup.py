# -*- coding:utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
		'description': 'My Project',
		'author': 'sora',
		'url': 'URL to get it at.',
		'download_url': 'Where to download it.',
		'author_email': 'My email.',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['sora']
		'scripts': [],
		'name': 'projectname'
}

setup(**config)
print 'I am in setup.py'
