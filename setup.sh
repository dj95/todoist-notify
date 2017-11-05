#!/bin/bash

# copy the project folder to the correct directory
cp -R ../todoist-notify /opt/.

# create the config dir
mkdir -p ~/.config/todoist-notify

# copy the default config to the correct place
cp /opt/todoist-notify/conf/config.json.default ~/.config/todoist-notify/config.json

# copy the systemd-user-service
cp /opt/todoist-notify/todoist-notify.service ~/.config/systemd/user/.

# create a shortcut for the client
sudo ln -s /opt/todoist-notify/src/todoist-client.py /usr/local/bin/todoist-client
