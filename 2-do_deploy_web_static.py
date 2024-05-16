#!/usr/bin/python3
"""documentation"""
from fabric.api import put, env, cd, sudo, task, run


def do_deploy(archive_path):
    """documentation block"""
    env.hosts = ['ubuntu@18.234.192.140', 'ubuntu@100.27.12.25']
    # upload the archive
    if not archive_path:
        return False
    parts = archive_filename.split("/")
    filename = parts[-1]
    decomp = file_name.split(".")
    fl = decomp[-2]

    put("{archive_path}", "/tmp/")
    run("mkdir -p /data/web_static/releases/{fl}")
    # decompress the tgz
    run("tar -xzf /tmp/{fl}.tgz -C /data/web_static/releases/{fl}")
    # delete the archive from server
    run("sudo rm {filename}.tgz")
    run("mv /data/web_static/releases/filename/web_static/* \
        /data/web_static/releases/{fl}/")
    run("rm -rf /data/web_static/releases/{fl}/web_static")
    # delete symbolic link
    run("rm -rf /data/web_static/current")
    # create new symbolic link
    run('ln -s /data/web_static/releases/{fl}/ /data/web_static/current')
