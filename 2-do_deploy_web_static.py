#!/usr/bin/python3
"""documentation"""
from fabric.api import run, put
import os

def do_deploy(archive_path):
    """documentation block"""
    env.hosts = ['18.234.192.140', '100.27.12.25']
    env.user = 'ubuntu'

    if not os.path.exists(archive_path):
        return False
    try:
        parts = archive_path.split("/")
        filename = parts[-1]
        decomp = filename.split(".")
        fl = decomp[-2]

        put(archive_path, "/tmp/")

        # decompress the tgz
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(filename, fl))
        # delete the archive from server
        run("sudo rm {}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(filename, fl))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fl))
        # delete symbolic link
        run("rm -rf /data/web_static/current")
        # create new symbolic link
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(fl))
        print("New version deployed!")
        return True
    except:
        return False
