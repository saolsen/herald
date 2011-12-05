#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    fabfile.py
    ~~~~~~~~

    Fabric configuration file, should be usefull in running and deploying this
    app because there are so many different parts.

    :author: Stephen Olsen
    :copyright: (c) 2011 Herald
"""

from fabric.api import run

def run_stack_local():
    """
    This will run the full herald stack locally.
    It will start up an instance of festival, the celeryd server and the django
    local server. To be usefull in debugging it will start up a tmux instance and
    run each daemon in a session so that you can view all debugging information.
    """
    pass

def push_to_beta():
    """
    This will log into the beta server, pull down the beta branch of the github repo
    and (re)start all the daemons in production mode.
    - nginx
    - gunicorn
    - celeryd
    - festival --server
    """
    pass
