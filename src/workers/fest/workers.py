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
    filename = render_text(text, name)

    #saved_file = WavFile(name)
    #local_file = open(filename, 'r')
    #saved_file.wav = local_file
    #saved_file.save()
    #local_file.close()

    return filename

# helpers
def render_text(text, name):
    """
    Takes the text, runs in through festival, saves it as _id.wav
    returns the filename
    """
    # I'm thinking that there's a better way to do this without saving the wav file
    # locally first
    subprocess.call('echo "' + text + '" | festival_client --ttw | cat > '
                    + name + '.wav', shell=True)
    return name + ".wav"

# mongo model
class WavFile(Document):
    name = StringField()
    wav = FileField()
