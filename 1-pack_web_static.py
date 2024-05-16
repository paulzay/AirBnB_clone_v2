#!/usr/bin/python3
"""compressing with fabric"""
from fabric.api import run
import shutil
import datetime

def do_pack():
    """function doc"""
    local("mkdir -p versions")
    timestring = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = '{}{}'.format("web_static", timestring)
    archive_name = local("shutil.make_archive(filename, 'tar', 'web_static')")
    # shutil.make_archive(filename, 'tar', 'web_static')
    # archive_name = f"web_static_{timestring}.tgz"
    archive_path = f"versions/{archive_name}"

    if archive_name:
        local("mv archive_name /versions")
        return archive_path
    return None
