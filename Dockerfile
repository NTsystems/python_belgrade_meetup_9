FROM python:3.5.3-slim
MAINTAINER Nebojsa Mrkic <nebojsa.mrkic@ntsystems.rs>

RUN groupadd -r ntsystems && useradd -r -g ntsystems ntsystems

ENV GOSU_VERSION 1.7
RUN set -x \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
    && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
    && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true \
    && apt-get purge -y --auto-remove ca-certificates wget

COPY [ "docker-entrypoint.sh", "wait-for-it.sh", "/usr/local/bin/" ]
COPY ./app /opt/app

WORKDIR /opt/app
EXPOSE 8888

ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD [ "python", "api.py" ]
