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
from festHelpers import WavFile, render
import subprocess
from mongoengine import *

connect('herald-beta', host='dbh46.mongolab.com', port=27467,
        username="herald-beta-user", password='HeraldHacknetBeta')

# Hello World test task
@task()
def testRunning():
    return "Hello World"

# Task that does what my fest server did
@task()
def tts(text, name):
    wav = render(text)
    new_file = WavFile()
    new_file.name = name
    new_file.wav = wav
    new_file.content_type = 'audio/vnd.wave'
    new_file.save()
    return name
