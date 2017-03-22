# python_belgrade_meetup_9
IoT, Python and Cassandra: A Match Made in Heaven

# Requirements:
    You will need folowing software to get started.
  - [Docker](https://www.docker.com) Use installer for your OS.
  - [DockerCompose](https://docs.docker.com/compose/) Use installer for your OS.
  - [Python 2.7 or grater](https://www.python.org) Use installer for your OS.
  - [Virtualenv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) Use pip package manager to install to your OS.


# Get started

## Developing example we have been using python 3.5 but it will work with python 2.7

Creating virtual environment for python 3.5 whith virtualenvwrapper run
```mkvirtualenv python_belgrade_meetup_9 --python=/usr/bin/python3.5```

Creating virtual environment for system python run
run ```mkvirtualenv python_belgrade_meetup_9```

## Install requirements
Run ```pip install -r requirements.txt```

## Project contains docker and docker-compose files

### Start project in docker
To start docker compose and build docker image run
```docker-compose up -d```


### Start cassandra in docker and run project from console
To start project from command line start run only cassandra in docker
```docker-compose up -d cassandra```

Start tornado server from command line run
```python api.py```


