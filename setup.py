# Setup file for blog project
try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A web.py app that makes a simple blog.',
	'author': 'Aditya Chincholi',
	'url': 'url to get it at',
	'download_url': 'Where to download it',
	'author_email': 'adityachincholi@gmail.com',
	'version': '0.1',
	'install_requires': ['nose', 'web.py'],
	'packages': ['blog'],
	'scripts': []
	'name': 'Blog'
}

setup(**config)
