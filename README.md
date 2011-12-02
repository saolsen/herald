Herald
======
Herald is a text to speech and speech to text processing api and
toolkit.

Roadmap
-------
Text-To-Speech api
Python library that uses said api
Some applications built on the system
Speech-To-Text api

Architecture
------------

The system has 3 main components.

* Web frontend
* Worker daemon and queue
* Processing servers (festival and cmusphinx)

On the frontend there's a python webapp that implements the REST
api.

In the middle there's a python celery worker daemon that responds to
requests from the web frontend, runs jobs on the festival and sphinx
servers and lets the webfront know when jobs are done.
In the back there are web servers built on top of festival and
cmusphinx that let us use all their functionality via a web api.

Breaking it out this way lets us scale the parts independantly. If we
have lots of requests we can scale the web frontend. If there are too
many jobs to process we can up the celery worker daemons and if there
are lots and lots of files to process we can add in more instances of
the festival or cmusphinx servers. These will also all run on their
own instances on rackspace cloud (or some other hosting service)
(currently on the beta server all three processes run on one server)

Development
-----------

### Source Control

If you guys want to help work on this (which I hope you do) Then I'd
like you each to make a branch called your name. Once you want to add
some code to the main repo send a pull request (through github) set
the base branch to dev and the head branch to yours. This way we can
review everything as it goes in.

### Running Locally

You need to install a few things to run the whole project locally.
Festival
python-virtualenv
To run simply run

    $ fab run_local

### Pushing to the testing server

I'm using Fabric, to push simply run

    $ fab deploy:testing

(If your using the virtialenv environment fabric should be included)

### Directory Layout

tbd
