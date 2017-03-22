# IoT, Python and Cassandra: A Match Made in Heaven

This repository contains the source code used in lecture titled "IoT, Python and Cassandra: A Match
Made in Heaven", presented at 9th Python Belgrade meetup.

## Prerequisites

- [Docker][www:docker]
- [Docker compose][www:docker-compose]

## Usage

The service is packed as a [Docker][www:docker] container, and it is executed by starting up an
instance of a pre-built image with an accompanying [Cassandra][www:cassandra] using the following
command:

```
docker-compose up -d
```

[www:cassandra]: http://cassandra.apache.org/
[www:docker]: https://www.docker.com
[www:docker-compose]: https://docs.docker.com/compose/
