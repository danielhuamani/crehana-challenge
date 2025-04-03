#!/bin/sh
exec "$@"

exec fastapi dev ./src/main.py --host 0.0.0.0