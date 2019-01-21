import os
import re
from setuptools import setup

def get_property(property, package):
	result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(property), open(package + '/__init__.py').read())
	return result.group(1)

from os import path
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md')) as f:
	long_description = f.read()

# Scripts
scripts = []
for dirname, dirnames, filenames in os.walk('scripts'):
	for filename in filenames:
		if filename.endswith('.py'):
			scripts.append(os.path.join(dirname, filename))

setup(name = 'sgdml',
			version = get_property('__version__', 'sgdml'),
			description = 'Reference implementation of the GDML and sGDML force field models.',
			long_description = long_description,
			long_description_content_type = 'text/markdown',
			classifiers=[
					'Development Status :: 4 - Beta',
					'Environment :: Console',
					'Intended Audience :: Science/Research'
					'Intended Audience :: Education'
					'Intended Audience :: Developers'  
					'License :: OSI Approved :: MIT License'
					'Operating System :: MacOS :: MacOS X',
					'Operating System :: POSIX',
					'Programming Language :: Python :: 2 :: Only',
					'Topic :: Scientific/Engineering :: Chemistry',
					'Topic :: Scientific/Engineering :: Physics',
					'Topic :: Software Development :: Libraries :: Python Modules'],
			url = 'http://www.gdml.ml',
			author = 'Stefan Chmiela',
			author_email = 'noreply@chmiela.com',
			license = 'MIT',
			packages = ['sgdml', 'sgdml.utils', 'sgdml.intf'],
			install_requires = [
					'numpy >= 1.13.0',
					'scipy >= 1.1.0',
					'ase >= 3.16.2'],
			entry_points={
					'console_scripts': ['sgdml=sgdml.cli:main', 'sgdml-get=sgdml.get:main']},
			scripts=scripts,
			include_package_data=True,
			zip_safe=False)