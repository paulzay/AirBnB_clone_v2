#!/usr/bin/python3
"""compressing with fabric"""
from fabric.api import local
import datetime


def do_pack():
    """function doc"""
    local("mkdir -p versions")
    timestring = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = '{}{}'.format("web_static_", timestring)
    local(f"tar -cvf {filename}.tgz web_static/")
    archive_name = '{}{}'.format(filename, ".tgz")
    # local(f"echo {archive_name}")
    archive_path = f"versions/{archive_name}"

    if archive_name:
        local(f"mv {archive_name} versions")
        return archive_path
    return None
