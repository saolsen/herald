Herald
======
Herald is a text to speech and speech to text processing api and
toolkit.

Roadmap
-------

* Text-To-Speech api
* Python library that uses said api
* Some applications built on the system
* Speech-To-Text api

Architecture
------------

The system has 3 main components.

* Web frontend
* Celery/rabbitMQ message queue
* Processing servers (festival and cmusphinx)

On the frontend there's a python webapp that implements the REST
api. This webapp sends messages when it needs some files processed tts
or stt to the rabbitMQ queue (via celery). Then on the backend
processing servers run celery worker daemons that listen to the
rabbitMQ queue and processes jobs. Celery makes all of this trivially easy.

Breaking it out this way lets us scale the parts independantly. If we
have lots of requests we can scale the web frontend. If there are lots
of files to process we can add in more instances of the festival or
cmusphinx servers. These will also all run on their own instances on
rackspace cloud (or some other hosting service) (currently on the beta
server all three processes run on one server)


Development
-----------
### Environment
You need to set up virtualenv.

    $ virtualenv --no-site-packages heraldenv
    $ source heraldenv/bin/activate
    $ pip install -r requirements.txt

Add whatever library's your code depends on to requierments.txt

### Source Control

If you guys want to help work on this (which I hope you do) Then I'd
like you each to make a branch called your name. Once you want to add
some code to the main repo send a pull request (through github) set
the base branch to dev and the head branch to yours. This way we can
review everything as it goes in.

### Running Locally

You need to install a few things to run the whole project locally.

* Festival
* python-virtualenv
* rabbitmq-server

To set up rabbitMQ to work with herald

    $ rabbitmqctl add_user herald_user dlareh
    $ rabbitmqctl add_vhost herald_queue
    $ rabbitmqctl set_permissions -p herald_queue herald_user "" ".*" ".*"

To run simply run

    $ fab run_local //not setup yet

Or to start each process individually

* Web

        $ python /src/web/webmain.py

* worker

        $ cd /src/
        $ sudo celeryd --loglevel=INFO

### Pushing to the testing server

I'm using Fabric, to push simply run

    $ fab deploy:testing

(If your using the virtialenv environment fabric should be included)

### Directory Layout

tbd
