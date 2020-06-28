import re
from setuptools import setup

with open('README.md') as f:
	readme = f.read()

with open('PogoOCR/__init__.py') as f:
	version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read()).group(1)

with open('requirements.txt') as f:
	requirements = f.splitlines()

setup(
	name="PogoOCR",
	version=version,
	author="Jay Turner",
	author_email="jay@trainerdex.co.uk",
	description="A Python tool for running OCR on Pokemon Screenshots",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/TrainerDex/PogoOCR",
	packages=setuptools.find_packages(),
	install_requires=requirements,
	python_requires='>=3.6',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
