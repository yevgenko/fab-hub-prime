"""A collection of Fabric commands for setting up remote repository workflow as inspired by Joe Maller's a web-focused Git workflow."""

VERSION = (0, 1, 0)

__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__author__ = "Yevgen Viktorov"
__contact__ = "yeevgen@gmail.com"
__homepage__ = "http://github.com/yeevgen/fab-hub-prime/"
__docformat__ = "restructuredtext"

from fabric.api import *
from fab_hub_prime.system import *
