#!/usr/bin/python3
# It generates archive tgz file using Fabric
# deployes webstatic onto my webservers

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['44.200.114.1', '3.239.120.245']
env.key_filename = '~/.ssh/id_rsa'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    uploads archive file from local to my webservers
    """

    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        print("New version deployed!")
        return True
    except Exception:
        return False
