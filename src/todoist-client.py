#!/bin/env python3
#
# todoist-notify
#
# (c) 2017 - Daniel Jankowski


import json
import os
import socket
import sys

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf


def connect():
    # initialize the unix socket connection to the daemon
    sock = socket.socket(
            socket.AF_UNIX,
            socket.SOCK_STREAM
            )

    # save the server address
    server_address = os.path.expanduser('~/.todoist.sock')

    try:
        # try to connect to the address
        sock.connect(server_address)
    except socket.error:
        # if an error appeared, print it...
        print('Cannot connect to the server')

        # ...and exit the application with an error
        sys.exit(1)

    # return the socket connection
    return sock


def send_notification(name, content, image):
    # create a new notification with
    notification = Notify.Notification.new(
            "{}".format(name),            # title
            content,                      # body
            "dialog-information"          # type
            )

    # use the GdkPixbuf image
    notification.set_icon_from_pixbuf(image)
    notification.set_image_from_pixbuf(image)

    # show the notification
    notification.show()


def main():
    # initialize connection to libnotify.
    Notify.init("Todoist")

    # use GdkPixbuf to create the proper image type
    image = GdkPixbuf.Pixbuf.new_from_file(
            os.path.dirname(
                os.path.realpath(__file__)
                ) + "/../assets/logo.png"
            )

    # connect to the unix socket and save it
    sock = connect()

    # send the request for project data
    sock.send(
            'getData'.encode('utf-8')
            )

    # raise the timeout if the server needs time to respond
    sock.settimeout(5.0)

    try:
        # try to receive the data
        data = sock.recv(4096)
    except:
        # if it fails, print and error message...
        print('An error happened')

        # ...and exit the application with an error
        sys.exit(1)

    # if we received the data successfully, decode it to a dictionary
    data = json.loads(data.decode('utf-8'))

    # iterate through the projects
    for project in data:
        # clear the content
        content = ''

        # if the project has no tasks...
        if len(data[project]) < 1:
            # ...skip the project
            continue

        # else iterate through the tasks
        for task in data[project]:
            # build the notification body with the task names
            content += task + '\n'

        # send the notification for each project
        send_notification(project, content, image)


if __name__ == '__main__':
    main()

