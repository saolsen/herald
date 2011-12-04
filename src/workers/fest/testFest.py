#!/usr/bin/env python

# I want to see if I can import a module here from the celeryconfig or whatever

from celery.task import task

@task
def add(x, y):
    return x + y
