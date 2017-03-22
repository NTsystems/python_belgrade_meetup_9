# Python Belgrade meetup #9
IoT, Python and Cassandra: A Match Made in Heaven

## Prerequisites
  - [Docker](https://www.docker.com) Install using your OS package manager or find installation instructions on web.
  - [DockerCompose](https://docs.docker.com/compose/) You can find installation instructions on provided link.
  - [Python 3.5 or greater](https://www.python.org) Should already be installed, if not instalation can be found on provided link.
  - [Virtualenv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) Use pip package manager to install to your OS.


## Get started

During development we have been using python 3.5. Creating virtual environment for python 3.5 whith virtualenvwrapper run
```mkvirtualenv python_belgrade_meetup_9 --python=/usr/bin/python3.5```
Install requirements
```pip install -r requirements.txt```
Start cassandra with docker compose
```docker-compose up -d cassandra```
Start tornado server from console
```python api.py```
Browse to http://localhost:8888/ for web page

#### Start in docker
In project folder start docker compose by running command
```docker-compose up -d```
To rebuild docker image use command
```docker-compose build```
Browse to http://localhost:8888/ for web page
