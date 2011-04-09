import os.path
from fabric.api import run
from fabric.contrib import files

def ssh_add_key(pub_key_file):
  """ Adds a ssh key from passed file to user's authorized_keys on server. """
  with open(os.path.normpath(pub_key_file), 'rt') as f:
    ssh_key = f.read()
  run('mkdir -p .ssh')
  run('umask 066 && touch .ssh/authorized_keys')
  files.append('.ssh/authorized_keys', ssh_key)
