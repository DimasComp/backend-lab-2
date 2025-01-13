#!/bin/sh

flask db migrate && echo "Migration done" || echo "Migration failed"
flask db upgrade && echo "Upgrade done" || echo "Upgrade failed"

python app.py