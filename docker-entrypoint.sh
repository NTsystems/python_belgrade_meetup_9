#!/bin/sh
set -e

if [ "$1" = 'python' -a "$(id -u)" = '0' ]; then
    chown -R ntsystems:ntsystems .
    pip3 install -r requirements.txt

    wait-for-it.sh -t 0 cassandra:9042 -- echo "Cassandra started!"
    exec gosu ntsystems "$0" "$@"
fi

exec "$@"
