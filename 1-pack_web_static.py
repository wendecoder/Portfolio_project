#!/usr/bin/python3
# It generates archive tgz file using Fabric

from fabric.api import *
from datetime import datetime
import os.path
import os


def do_pack():
    """
    generates archive for web_static
    """
    Time = datetime.now()
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")
    name = 'versions/flask_app_' + Time.strftime("%Y%m%d%H%M%S") + ".tgz"
    print('Packing flask_app to ' + name)
    result = local("tar -cvzf {} flask_app".format(name))
    if result is None:
        return None
    size = os.stat(name).st_size
    print('web_static packed: {} -> {}Bytes'.format(name, size))
    return name
