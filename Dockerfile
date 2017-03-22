FROM phusion/baseimage:0.9.19
MAINTAINER Nebojsa Mrkic <nebojsa.mrkic@ntsystems.rs>

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Install dependencies
RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip \
    python3-dev \
    python3-pip

# Copy the required source
RUN mkdir -p /opt/meetup
ADD ./requirements.txt /opt/meetup/requirements.txt

# Initialize app
WORKDIR /opt/meetup
RUN pip3 install -r requirements.txt

# Add needed files
ADD ./run.sh /opt/meetup/
ADD ./models.py /opt/meetup/models.py
ADD ./api.py /opt/meetup/api.py
ADD ./index.html /opt/meetup/index.html

# Add runits
RUN mkdir /etc/service/meetup
ADD ./run.sh /etc/service/meetup/run
RUN chmod +x /etc/service/meetup/run


# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

