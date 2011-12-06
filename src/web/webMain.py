# -*- coding: utf-8 -*-
"""
    Herald
    ~~~~~~~~

    This is the main web process for the herald API

    :author: Stephen Olsen
    :copyright: (c) 2011 Herald
"""
#flask stuff
from flask import Flask, request, session, url_for, redirect, \
    render_template, abort, g, flash
import mongoengine
#celery workers
import sys
sys.path.append('../')
sys.path.append('./')
import workers.fest.workers as fest
#import subprocess
#from boto.s3.connection import S3Connection
#from boto.s3.key import Key

# configuration
# pymongo connection is threadsafe, we define it globally
# We will have to redo this when we have a production environment up
mongoengine.connect('herald-beta', host='dbh46.mongolab.com', port=27467,
                    username="herald-beta-user", password='HeraldHacknetBeta')

# create our little application :)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve():
    """
    Hey look it works!
    """
    return "So that part is good."

@app.route('/tts', methods=['POST'])
def testit():
    """
    Take some text, turn it into speech, same as the fest server
    """
    text = request.form['text']
    name = request.form['name']

    t = fest.tts.delay(text, name)
    return t.get()

if __name__ == '__main__':
    # Make sure that festival is running
    app.run(host="0.0.0.0")
