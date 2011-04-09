import os.path
from fabric.api import env, local, run, cd
from fabric.contrib import files

def ssh_add_key(pub_key_file):
  """ Adds a ssh key from passed file to user's authorized_keys on server. """
  with open(os.path.normpath(pub_key_file), 'rt') as f:
    ssh_key = f.read()
  run('mkdir -p .ssh')
  run('touch .ssh/authorized_keys')
  files.append('.ssh/authorized_keys', ssh_key)

def set_umask(umask='022'):
  files.append('.bash_profile', 'umask %s' % umask)

def hub_init(remote='live'):
  #TODO: check if remote exists and can be overwritten or expanded
  #TODO: check if path exists, warn user and use it
  conf = env.conf[remote]
  run('mkdir -p %s' % conf['REPO_DIR'])
  with cd(conf['REPO_DIR']):
    run('git --bare init')
    #put(os.path.join(os.path.split(__file__)[0], 'hook_templates/git/post-update'), 'hooks')
    files.upload_template('post-update', 'hooks/post-update', conf, True,
        template_dir=os.path.join(os.path.split(__file__)[0], 'hook_templates/git'))
    run('chmod +x hooks/post-update')
  local('git remote add %s ssh://%s%s' % (remote, env.host_string, conf['REPO_DIR']))
