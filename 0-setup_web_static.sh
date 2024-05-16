#!/usr/bin/env bash
# prepare the webserver

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    sudo apt-get update -y
    sudo apt install nginx -y
    sudo ufw allow 'Nginx HTTP'
    sudo service nginx restart
else
  echo "Nginx is already installed."
fi

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "testing this setup" > /data/web_static/releases/test/index.html

if [[ -L /data/web_static/current ]]; then
        rm -f /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sed -i '/server_name _;/a \         location /hbnb_static\/ {\n\t\t alias \/data\/web_static\/current\/;\n\t\t autoindex off;\n \t } ' /etc/nginx/sites-available/default
sudo service nginx restart