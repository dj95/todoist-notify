#!/bin/env python3
#
# todoist-notify
#
# (c) 2017 - Daniel Jankowski


import time

from pytodoist import todoist
from threading import Thread, Event
from unixconnection import TodoistSocketThread


class TodoistDaemon(Thread):

    def __init__(self, config):
        # call the constructor of the Thread object
        super().__init__()
    
        # create a stop event
        self.stop_event = Event()

        # log in to todoist in order to make api calls
        self.__user = todoist.login(
                config['username'],
                config['password']
                )

        # initialize the TodoistSocket for unix connections
        self.__socket_thread = TodoistSocketThread(self)

        # some variables we need later on
        self.__timeout = 10.0
        self.__projects = None

    def __shutdown(self):
        # stop the socket connection thread
        self.__socket_thread.stop_event.set()

    def get_projects(self):
        return self.__projects

    def run(self):
        # start the unix socket thread
        self.__socket_thread.start()

        # while we do not stop the application, run this main loop 
        while not self.stop_event.is_set():
            # empty dict for the projects
            downloaded_projects = {}

            # get the projects from the todoist api
            projects = self.__user.get_projects()

            # iterate through all projects
            for project in projects:
                # empty dict for tasks
                downloaded_tasks = []

                # iterate through all tasks...
                for task in project.get_tasks():
                    # ...and append the to the tasks list
                    downloaded_tasks.append(task.content)

                # save the task list as value to the project name as key
                downloaded_projects[project.name] = downloaded_tasks
                
            # save all projects and tasks as dict
            self.__projects = downloaded_projects

            #NOTE: for debugging purposes
            print('Got todoist data')

            # dont do too much api calls per minute. sleep a second
            time.sleep(self.__timeout)

        # run shutdown function if we want to exit the program
        self.__shutdown()
