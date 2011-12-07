#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    fest helpers
    ~~~~~~~~

    These are helper functions for working with festival

    :author: Stephen Olsen
    :copyright: (c) 2011 Herald
"""
import subprocess
import mongoengine

def render(text):
        """
        Runs the text through festival
        """
        process = subprocess.Popen(['festival_client', '--ttw'], shell=False,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        wav = process.communicate(text)[0] #Communicate returns a tple, (stdout,stderr)
        return wav

# mongo model for storing wav files
class WavFile(mongoengine.Document):
    name = mongoengine.StringField()
    wav = mongoengine.FileField()
