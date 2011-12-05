#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    fest workers
    ~~~~~~~~

    These are the celery workers that interact with the festival server daemon

    :author: Stephen Olsen
    :copyright: (c) 2011 Herald
"""

from celery.task import task

# Hello World test task
@task()
def testRunning():
    return "Hello World"
