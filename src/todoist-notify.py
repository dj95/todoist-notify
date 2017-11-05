#!/bin/env python3
#
# todoist-notify
#
# (c) 2017 - Daniel Jankowski


import json
import os
import todoist
import sys


CONFIG_PATH = '~/.config/todoist-notify/config.json'


def read_config():
    # expand the user directory
    path = os.path.expanduser(CONFIG_PATH)

    # check if the config file exists...
    if not os.path.isfile(path):
        # ...else print an error message...
        print('No such file or directory! Cannot find the config file!')

        # ...and shut down with an error
        sys.exit(1)

    # open the config file in reading mode
    with open(path, 'r') as fp:
        # load the config file as json object to create a dict
        config = json.load(fp)

    # return the config dict
    return config


def main():
    # read the config file
    config = read_config()

    # initialize the todoistDaemon
    daemon = todoist.TodoistDaemon(config)

    # start it
    daemon.start()


if __name__ == '__main__':
    main()
