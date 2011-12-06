#!/bin/sh
tmux new-session -d -s heraldrunner
tmux new-window -t heraldrunner:1 -n 'Festival' 'festival --server'
tmux new-window -t heraldrunner:2 -n 'Celery' 'celeryd'
tmux new-window -t heraldrunner:3 -n 'Web' 'python web/webMain.py'

tmux select-window -t heraldrunner:1
tmux -2 attach-session -t heraldrunner
