#!/bin/sh

flask db migrate
flask db upgrade

python app.py