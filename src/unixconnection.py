#!/bin/env python3
#
# todoist-notify
#
# (c) 2017 - Daniel Jankowski


import json
import os
import socket
import sys
import time

from threading import Thread, Event


class TodoistSocketThread(Thread):

    def __init__(self, callback):
        # call the constructor of the Thread object
        super().__init__()

        # create a stop event
        self.stop_event = Event()

        # save the unix socket address
        self.server_address = '/home/neo/.todoist.sock'
        
        # save the callback to the TodoisDaemon
        self.__callback = callback

        # try to create a new unix socket
        try:
            self.__socket = socket.socket(
                    socket.AF_UNIX,
                    socket.SOCK_STREAM
                    )
            # bind the socket to the path
            self.__socket.bind(self.server_address)

            # set the timeout
            self.__socket.settimeout(0.1)
        except Exception as e: # If this doesnt work...
            # ...remove the existing file
            os.remove(self.server_address)

            #  create the socket
            self.__socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            
            # and bind it to the file
            self.__socket.bind(self.server_address)

            # set the timeout for the socket
            self.__socket.settimeout(0.1)

    def __shutdown(self):
        # close the socket on shutdown
        self.__socket.close()

        # and remove the file
        os.remove(self.server_address)

    def run(self):
        # listen on the socket for a new connection
        self.__socket.listen(1)

        # while we do not stop the application, run this main loop
        while not self.stop_event.is_set():
            try:
                # try to accept a connection
                connection, client_address = self.__socket.accept()
            except:
                # if we dont get a connection, continue and retry
                # this happens as long as we wait for a connection
                continue

            # if we accept a connection...
            try:
                # ...try to receive a datastream
                data = connection.recv(1024)
            except:
                # else wait for a reconnect
                continue

            # decode the binary stream to a string
            data = data.decode('utf-8')

            # if the command we got is 'getData'...
            if data == 'getData':
                # ...call the callback and get the project information
                projects = self.__callback.get_projects()

                # dump the project information as json string
                projects_json = json.dumps(projects)

                # send the json project information as binary stream
                connection.send(
                        projects_json.encode('utf-8')
                        )

        # run shutdown function if we want to exit the program
        self.__shutdown()
