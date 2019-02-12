try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description':'My Project',
	'author': 'oneuu',
	'url': 'URL to get it at.', 
	'download_url': 'Where to download it.', 
	'author_email': 'qi.1014@hotmail.com',
	'version': '0.1',
	'install_requires': ['nose'], 
	'packages': ['lyx'],
	'scripts': [],
	'name': 'justtest'
}

setup(**config)
