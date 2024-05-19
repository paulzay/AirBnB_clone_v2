#!/usr/bin/python3
"""documentation"""
from fabric.api import put, env, cd, sudo, task, run, local
import os
env.hosts = ['18.234.192.140', '100.27.12.25']
env.user = 'ubuntu'


def do_pack():
    """function doc"""
    local("mkdir -p versions")
    timestring = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = '{}{}'.format("web_static_", timestring)
    local(f"tar -cvzf versions/{filename}.tgz web_static")
    archive_name = '{}{}'.format(filename, ".tgz")
    archive_path = f"versions/{archive_name}"

    if archive_name:
        return archive_path
    return None


def do_deploy(archive_path):
    """documentation block"""
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))

        print("New version deployed!")
        return True
    except ValueError:
        return False


def deploy():
    """comment"""
    archive_path = do_pack()
    if not os.path.exists(archive_path):
        return False

    retval = do_deploy(archive_path)
    return retval
