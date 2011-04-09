#!/usr/bin/env python
import os
import codecs
try:
  from setuptools import setup, find_packages
except ImportError:
  from ez_setup import use_setuptools
  use_setuptools()
  from setuptools import setup, find_packages

import fab_hub_prime as distmeta

if os.path.exists("README.rst"):
  long_description = codecs.open('README.rst', "r", "utf-8").read()
else:
  long_description = "See http://github.com/yeevgen/fab-hub-prime/tree/master"

install_requires = ['Fabric >=1.0.0', 'GitPython', 'argparse', 'jinja2']

setup(
  name="fab-hub-prime",
  version=distmeta.__version__,
  description="A collection of Fabric commands for setting up remote repository workflow as inspired by Joe Maller's a web-focused Git workflow.",
  author=distmeta.__author__,
  author_email=distmeta.__contact__,
  url=distmeta.__homepage__,
  platforms=["any"],
  license="BSD",
  packages=find_packages(),
  install_requires=install_requires,
  zip_safe=False,
  classifiers=[
    # Picked from
    # http://pypi.python.org/pypi?:action=list_classifiers
    "Development Status :: 1 - Planning",
    #"Development Status :: 2 - Pre-Alpha",
    #"Development Status :: 3 - Alpha",
    #"Development Status :: 4 - Beta",
    #"Development Status :: 5 - Production/Stable",
    #"Development Status :: 6 - Mature",
    #"Development Status :: 7 - Inactive",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Topic :: Software Development :: Version Control",
  ],
  long_description=long_description,
)
